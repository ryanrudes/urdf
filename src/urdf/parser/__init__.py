from __future__ import annotations

import keyword
import re
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True, kw_only=True)
class Origin:
    """A URDF origin expressed as xyz translation and rpy rotation."""

    xyz: tuple[float, float, float] = (0.0, 0.0, 0.0)
    """The translation component of the origin."""

    rpy: tuple[float, float, float] = (0.0, 0.0, 0.0)
    """The roll-pitch-yaw rotation component of the origin."""


@dataclass(frozen=True, kw_only=True)
class Inertia:
    """A URDF inertia matrix represented by its six unique entries."""

    ixx: float
    """The moment of inertia about the x-axis."""

    ixy: float
    """The product of inertia about the x- and y-axes."""

    ixz: float
    """The product of inertia about the x- and z-axes."""

    iyy: float
    """The moment of inertia about the y-axis."""

    iyz: float
    """The product of inertia about the y- and z-axes."""

    izz: float
    """The moment of inertia about the z-axis."""


@dataclass(frozen=True, kw_only=True)
class LinkDefinition:
    """A link parsed from a URDF file."""

    name: str
    """The URDF link name."""

    mass: float
    """The mass of the link."""

    origin: Origin
    """The inertial origin of the link."""

    inertia: Inertia | None
    """The inertia tensor of the link, if one is specified."""


@dataclass(frozen=True, kw_only=True)
class JointLimit:
    """A scalar joint limit parsed from a URDF joint."""

    lower: float
    """The lower position limit."""

    upper: float
    """The upper position limit."""

    effort: float
    """The effort limit."""

    velocity: float
    """The velocity limit."""


@dataclass(frozen=True, kw_only=True)
class JointDefinition:
    """A joint parsed from a URDF file."""

    name: str
    """The URDF joint name."""

    type: str
    """The URDF joint type."""

    parent: str
    """The URDF parent link name."""

    child: str
    """The URDF child link name."""

    origin: Origin
    """The joint origin relative to the parent link frame."""

    axis: tuple[float, float, float] | None
    """The joint axis, if the joint is axis-defined."""

    limit: JointLimit | None
    """The joint limit, if the joint has scalar limits."""


@dataclass(frozen=True, kw_only=True)
class RobotDefinition:
    """A robot definition parsed from a URDF file."""

    name: str
    """The URDF robot name."""

    links: tuple[LinkDefinition, ...]
    """The links in the robot."""

    joints: tuple[JointDefinition, ...]
    """The joints in the robot."""


_SUPPORTED_JOINT_TYPES = {
    "fixed",
    "revolute",
    "continuous",
    "prismatic",
    "planar",
    "floating",
}
_AXIS_DEFINED_JOINT_TYPES = {"revolute", "continuous", "prismatic", "planar"}
_LIMITED_JOINT_TYPES = {"revolute", "prismatic"}
_LIMITLESS_SCALAR_JOINT_TYPES = {"continuous"}


_CLASS_BY_JOINT_TYPE = {
    "fixed": "FixedJoint",
    "floating": "FloatingJoint",
    "revolute": "RevoluteJoint",
    "continuous": "ContinuousJoint",
    "prismatic": "PrismaticJoint",
    "planar": "PlanarJoint",
}


def parse_urdf(path: str | Path) -> RobotDefinition:
    """Parse a URDF file into a robot definition.

    Args:
        path: The path to the URDF file.

    Returns:
        The parsed RobotDefinition object.

    Raises:
        ValueError: If the root XML tag is not <robot> or contains malformed data.
    """
    root = ET.parse(path).getroot()
    if root.tag != "robot":
        raise ValueError(f"Expected a URDF <robot> root, got <{root.tag}>.")

    robot_name = root.attrib.get("name", Path(path).stem)
    links = tuple(_parse_link(element) for element in root.findall("link"))
    joints = tuple(_parse_joint(element) for element in root.findall("joint"))

    return RobotDefinition(name=robot_name, links=links, joints=joints)


def export_robot_definition_code(
    urdf_path: str | Path,
    *,
    class_prefix: str | None = None,
    constant_prefix: str | None = None,
) -> str:
    """Export Python robot definition code from a URDF file.

    Args:
        urdf_path: The path to the URDF file.
        class_prefix: The prefix to use for generated Python classes. Defaults to a PascalCase version of the URDF
            robot name.
        constant_prefix: The prefix to use for generated Python constants. Defaults to an upper snake case version of
            the generated class prefix.

    Returns:
        Python source code defining the robot's typed link identifiers, joint identifiers, linkage, articulation, and
        skeleton.
    """
    from .codegen import export_robot_definition_code as export_code

    return export_code(
        urdf_path,
        class_prefix=class_prefix,
        constant_prefix=constant_prefix,
    )


def write_robot_definition_code(
    urdf_path: str | Path,
    output_path: str | Path,
    *,
    class_prefix: str | None = None,
    constant_prefix: str | None = None,
) -> None:
    """Write Python robot definition code exported from a URDF file.

    Args:
        urdf_path: The path to the URDF file.
        output_path: The path to write the generated Python module to.
        class_prefix: The prefix to use for generated Python classes.
        constant_prefix: The prefix to use for generated Python constants.
    """
    from .codegen import write_robot_definition_code as write_code

    write_code(
        urdf_path,
        output_path,
        class_prefix=class_prefix,
        constant_prefix=constant_prefix,
    )


def regenerate_registry_files() -> None:
    """Regenerate the models __init__.py, registry.py, and robots __init__.py files."""
    from .codegen import regenerate_registry_files as regen

    regen()


def sync_assets() -> None:
    """Synchronize all URDF assets with the generated Python definitions and registry."""
    from .codegen import sync_assets as sync

    sync()


def _parse_link(element: ET.Element) -> LinkDefinition:
    """Parse a link element from a URDF XML definition.

    Args:
        element: The XML element for the link.

    Returns:
        The parsed LinkDefinition containing name, mass, origin, and inertia.
    """
    name = _required_attr(element, "name")
    inertial = element.find("inertial")
    if inertial is None:
        return LinkDefinition(name=name, mass=0.0, origin=Origin(), inertia=None)

    origin = _parse_origin(inertial.find("origin"))

    mass_element = inertial.find("mass")
    mass = (
        _float_attr(mass_element, "value", default=0.0)
        if mass_element is not None
        else 0.0
    )

    inertia_element = inertial.find("inertia")
    inertia = _parse_inertia(inertia_element) if inertia_element is not None else None

    return LinkDefinition(name=name, mass=mass, origin=origin, inertia=inertia)


def _parse_joint(element: ET.Element) -> JointDefinition:
    """Parse a joint element from a URDF XML definition.

    Args:
        element: The XML element for the joint.

    Returns:
        The parsed JointDefinition containing parent, child, origin, and limits.

    Raises:
        ValueError: If the joint type is unsupported or missing required children/attributes.
    """
    name = _required_attr(element, "name")
    joint_type = _required_attr(element, "type")
    if joint_type not in _SUPPORTED_JOINT_TYPES:
        raise ValueError(f"Joint {name!r} has unsupported type {joint_type!r}.")

    parent = _required_attr(_required_child(element, "parent"), "link")
    child = _required_attr(_required_child(element, "child"), "link")
    origin = _parse_origin(element.find("origin"))

    axis_element = element.find("axis")
    axis = (
        _parse_float_tuple(axis_element.attrib.get("xyz", "1 0 0"))
        if axis_element is not None
        else None
    )
    if axis is None and joint_type in _AXIS_DEFINED_JOINT_TYPES:
        axis = (1.0, 0.0, 0.0)

    limit_element = element.find("limit")
    limit = _parse_limit(limit_element) if limit_element is not None else None
    if joint_type in _LIMITED_JOINT_TYPES and limit is None:
        raise ValueError(
            f"Joint {name!r} of type {joint_type!r} is missing a <limit> element."
        )

    return JointDefinition(
        name=name,
        type=joint_type,
        parent=parent,
        child=child,
        origin=origin,
        axis=axis,
        limit=limit,
    )


def _parse_origin(element: ET.Element | None) -> Origin:
    """Parse an origin XML element into an Origin dataclass.

    Args:
        element: The XML element for the origin, or None.

    Returns:
        The parsed Origin object, defaulting to identity if None.
    """
    if element is None:
        return Origin()
    xyz = _parse_float_tuple(element.attrib.get("xyz", "0 0 0"))
    rpy = _parse_float_tuple(element.attrib.get("rpy", "0 0 0"))
    return Origin(xyz=xyz, rpy=rpy)


def _parse_inertia(element: ET.Element) -> Inertia:
    """Parse an inertia XML element into an Inertia dataclass.

    Args:
        element: The XML element for the inertia.

    Returns:
        The parsed Inertia object containing the six unique matrix entries.
    """
    return Inertia(
        ixx=_float_attr(element, "ixx"),
        ixy=_float_attr(element, "ixy"),
        ixz=_float_attr(element, "ixz"),
        iyy=_float_attr(element, "iyy"),
        iyz=_float_attr(element, "iyz"),
        izz=_float_attr(element, "izz"),
    )


def _parse_limit(element: ET.Element) -> JointLimit:
    """Parse a joint limit XML element into a JointLimit dataclass.

    Args:
        element: The XML element for the limit.

    Returns:
        The parsed JointLimit object containing lower, upper, effort, and velocity limits.
    """
    return JointLimit(
        lower=_float_attr(element, "lower", default=0.0),
        upper=_float_attr(element, "upper", default=0.0),
        effort=_float_attr(element, "effort"),
        velocity=_float_attr(element, "velocity"),
    )


def _render_module(
    definition: RobotDefinition, *, class_prefix: str, constant_prefix: str
) -> str:
    link_enum_members = _enum_members(
        (link.name for link in definition.links), suffixes=("_link", "_link_link")
    )
    joint_enum_members = _enum_members(
        (joint.name for joint in definition.joints), suffixes=("_joint", "_joint_joint")
    )

    link_enum = _render_link_enum(class_prefix, definition.links, link_enum_members)
    joint_enum = _render_joint_enum(class_prefix, definition.joints, joint_enum_members)
    link_specs = _render_link_specs(class_prefix, definition.links, link_enum_members)
    joint_specs = _render_joint_specs(
        class_prefix, definition.joints, link_enum_members, joint_enum_members
    )
    used_joint_classes = _used_joint_classes(definition.joints)

    imports = _render_imports(used_joint_classes)
    aliases = _render_aliases(class_prefix, constant_prefix, used_joint_classes)
    helpers = _render_helpers(class_prefix)
    constants = _render_constants(class_prefix, constant_prefix)

    return (
        "\n\n".join(
            [
                imports,
                link_enum,
                joint_enum,
                aliases,
                helpers,
                link_specs,
                joint_specs,
                constants,
            ]
        )
        + "\n"
    )


def _render_imports(used_joint_classes: Sequence[str]) -> str:
    kinematics_imports = [
        "Articulation",
        *used_joint_classes,
        "JointEffortLimits",
        "JointId",
        "JointPositionLimits",
        "Link",
        "LinkId",
        "Linkage",
        "Skeleton",
    ]
    unique_imports = sorted(set(kinematics_imports))
    return textwrap.dedent(
        f"""
        from __future__ import annotations

        import numpy as np
        from scipy.spatial.transform import Rotation

        from urdf.core.types import RigidTransform
        from urdf.dynamics import InertiaTensor
        from urdf.kinematics import (
        {chr(10).join(f"    {name}," for name in unique_imports)}
        )
        """
    ).strip()


def _render_link_enum(
    class_prefix: str,
    links: Sequence[LinkDefinition],
    members: dict[str, str],
) -> str:
    lines = [
        f"class {class_prefix}LinkId(LinkId):",
        f'    """Link identifiers for the {class_prefix} robot."""',
        "",
    ]
    for link in links:
        member = members[link.name]
        lines.extend(
            [
                f'    {member} = "{link.name}"',
                f'    """The {_humanize_name(link.name)} link."""',
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def _render_joint_enum(
    class_prefix: str,
    joints: Sequence[JointDefinition],
    members: dict[str, str],
) -> str:
    lines = [
        f"class {class_prefix}JointId(JointId):",
        f'    """Joint identifiers for the {class_prefix} robot."""',
        "",
    ]
    for joint in joints:
        member = members[joint.name]
        lines.extend(
            [
                f'    {member} = "{joint.name}"',
                f'    """The {_humanize_name(joint.name)} joint."""',
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def _render_aliases(
    class_prefix: str, constant_prefix: str, used_joint_classes: Sequence[str]
) -> str:
    joint_union = "\n    | ".join(
        f"{name}[{class_prefix}LinkId, {class_prefix}JointId]"
        for name in used_joint_classes
    )
    return textwrap.dedent(
        f'''
        type {class_prefix}Link = Link[{class_prefix}LinkId]
        """A link in the {class_prefix} robot."""

        type {class_prefix}Joint = (
            {joint_union}
        )
        """A joint in the {class_prefix} robot."""

        type InertiaSpec = tuple[float, float, float, float, float, float]
        """URDF inertia entries ordered as ixx, ixy, ixz, iyy, iyz, izz."""

        type OriginSpec = tuple[tuple[float, float, float], tuple[float, float, float]]
        """URDF origin entries ordered as xyz and rpy."""

        type LinkSpec = tuple[str, float, OriginSpec, InertiaSpec | None]
        """URDF-derived inertial data for a link."""

        type JointLimitSpec = tuple[float, float, float, float]
        """URDF joint limits ordered as lower, upper, effort, and velocity."""

        type JointSpec = tuple[
            str,
            {class_prefix}LinkId,
            {class_prefix}LinkId,
            OriginSpec,
            tuple[float, float, float] | None,
            JointLimitSpec | None,
        ]
        """URDF-derived data for a joint."""
        '''
    ).strip()


def _render_helpers(class_prefix: str) -> str:
    return (
        textwrap.dedent(
            f'''
        def _transform(origin: OriginSpec = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))) -> RigidTransform:
            """Create a rigid transform from URDF xyz/rpy values."""
            xyz, rpy = origin
            return RigidTransform.from_components(
                translation=np.array(xyz),
                rotation=Rotation.from_euler("xyz", np.array(rpy), degrees=False),
            )


        def _inertia(spec: InertiaSpec | None) -> InertiaTensor:
            """Create an inertia tensor from URDF inertia entries."""
            if spec is None:
                return InertiaTensor.zero()
            ixx, ixy, ixz, iyy, iyz, izz = spec
            return InertiaTensor.from_entries(ixx=ixx, ixy=ixy, ixz=ixz, iyy=iyy, iyz=iyz, izz=izz)


        def _link(link_id: {class_prefix}LinkId, spec: LinkSpec) -> {class_prefix}Link:
            """Create a link from a URDF-derived link spec."""
            name, mass, origin, inertia = spec
            return Link[{class_prefix}LinkId](
                id=link_id,
                name=name,
                mass=mass,
                origin=_transform(origin),
                inertia=_inertia(inertia),
            )


        def _joint(joint_id: {class_prefix}JointId, spec: JointSpec) -> {class_prefix}Joint:
            """Create a joint from a URDF-derived joint spec."""
            name, parent, child, origin, axis, limits = spec
            origin_transform = _transform(origin)
            match joint_id:
        '''
        ).rstrip()
        + "\n"
        + _render_joint_factory_cases(class_prefix)
    )


def _render_joint_factory_cases(class_prefix: str) -> str:
    return textwrap.dedent(
        f"""
                case _ if axis is None:
                    return FixedJoint[{class_prefix}LinkId, {class_prefix}JointId](
                        id=joint_id,
                        name=name,
                        parent=parent,
                        child=child,
                        origin=origin_transform,
                    )
                case _:
                    if limits is None:
                        return ContinuousJoint[{class_prefix}LinkId, {class_prefix}JointId](
                            id=joint_id,
                            name=name,
                            parent=parent,
                            child=child,
                            origin=origin_transform,
                            axis=np.array(axis),
                            limits=JointEffortLimits(effort=0.0, velocity=0.0),
                        )
                    lower, upper, effort, velocity = limits
                    return RevoluteJoint[{class_prefix}LinkId, {class_prefix}JointId](
                        id=joint_id,
                        name=name,
                        parent=parent,
                        child=child,
                        origin=origin_transform,
                        axis=np.array(axis),
                        limits=JointPositionLimits(lower=lower, upper=upper, effort=effort, velocity=velocity),
                    )
        """
    ).strip()


def _render_link_specs(
    class_prefix: str,
    links: Sequence[LinkDefinition],
    members: dict[str, str],
) -> str:
    lines = [f"_LINK_SPECS: dict[{class_prefix}LinkId, LinkSpec] = {{"]
    for link in links:
        lines.append(
            f"    {class_prefix}LinkId.{members[link.name]}: {_format_link_spec(link)},"
        )
    lines.extend(
        [
            "}",
            f'"""URDF-derived link specifications for the {class_prefix} robot."""',
        ]
    )
    return "\n".join(lines)


def _render_joint_specs(
    class_prefix: str,
    joints: Sequence[JointDefinition],
    link_members: dict[str, str],
    joint_members: dict[str, str],
) -> str:
    lines = [f"_JOINT_SPECS: dict[{class_prefix}JointId, JointSpec] = {{"]
    for joint in joints:
        lines.append(
            f"    {class_prefix}JointId.{joint_members[joint.name]}: "
            f"{_format_joint_spec(class_prefix, joint, link_members)},"
        )
    lines.extend(
        [
            "}",
            f'"""URDF-derived joint specifications for the {class_prefix} robot."""',
        ]
    )
    return "\n".join(lines)


def _render_constants(class_prefix: str, constant_prefix: str) -> str:
    return textwrap.dedent(
        f'''
        {constant_prefix}_LINKAGE = Linkage[{class_prefix}LinkId](
            links={{link_id: _link(link_id, spec) for link_id, spec in _LINK_SPECS.items()}},
        )
        """The linkage for the {class_prefix} robot."""

        {constant_prefix}_ARTICULATION = Articulation[{class_prefix}LinkId, {class_prefix}JointId](
            joints={{joint_id: _joint(joint_id, spec) for joint_id, spec in _JOINT_SPECS.items()}},
        )
        """The articulation for the {class_prefix} robot."""

        {constant_prefix} = Skeleton[{class_prefix}LinkId, {class_prefix}JointId](
            linkage={constant_prefix}_LINKAGE,
            articulation={constant_prefix}_ARTICULATION,
        )
        """The kinematic chain for the {class_prefix} robot."""
        '''
    ).strip()


def _used_joint_classes(joints: Sequence[JointDefinition]) -> list[str]:
    classes = {_CLASS_BY_JOINT_TYPE[joint.type] for joint in joints}
    order = [
        "FixedJoint",
        "FloatingJoint",
        "RevoluteJoint",
        "ContinuousJoint",
        "PrismaticJoint",
        "PlanarJoint",
    ]
    return [name for name in order if name in classes]


def _format_link_spec(link: LinkDefinition) -> str:
    return f"({link.name!r}, {_format_float(link.mass)}, {_format_origin(link.origin)}, {_format_inertia(link.inertia)})"


def _format_joint_spec(
    class_prefix: str,
    joint: JointDefinition,
    link_members: dict[str, str],
) -> str:
    return (
        "("
        + ", ".join(
            [
                repr(joint.name),
                f"{class_prefix}LinkId.{link_members[joint.parent]}",
                f"{class_prefix}LinkId.{link_members[joint.child]}",
                _format_origin(joint.origin),
                _format_tuple(joint.axis) if joint.axis is not None else "None",
                _format_limit(joint.limit),
            ]
        )
        + ")"
    )


def _format_origin(origin: Origin) -> str:
    return f"({_format_tuple(origin.xyz)}, {_format_tuple(origin.rpy)})"


def _format_inertia(inertia: Inertia | None) -> str:
    if inertia is None:
        return "None"
    return _format_tuple(
        (inertia.ixx, inertia.ixy, inertia.ixz, inertia.iyy, inertia.iyz, inertia.izz)
    )


def _format_limit(limit: JointLimit | None) -> str:
    if limit is None:
        return "None"
    return _format_tuple((limit.lower, limit.upper, limit.effort, limit.velocity))


def _format_tuple(values: Sequence[float] | None) -> str:
    if values is None:
        return "None"
    return "(" + ", ".join(_format_float(value) for value in values) + ")"


def _format_float(value: float) -> str:
    return repr(float(value))


def _enum_members(names: Iterable[str], *, suffixes: Sequence[str]) -> dict[str, str]:
    members: dict[str, str] = {}
    used: set[str] = set()
    for name in names:
        member = _upper_snake(_strip_known_suffixes(name, suffixes=suffixes))
        if not member or member[0].isdigit() or keyword.iskeyword(member.lower()):
            member = f"_{member}"
        original = member
        index = 2
        while member in used:
            member = f"{original}_{index}"
            index += 1
        used.add(member)
        members[name] = member
    return members


def _strip_known_suffixes(name: str, *, suffixes: Sequence[str]) -> str:
    for suffix in suffixes:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def _pascal_case(value: str) -> str:
    words = _identifier_words(value)
    return "".join(word.capitalize() for word in words) or "Robot"


def _upper_snake(value: str) -> str:
    words = _identifier_words(value)
    return "_".join(word.upper() for word in words) or "ROBOT"


def _identifier_words(value: str) -> list[str]:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", value)
    return [word for word in re.split(r"[^0-9A-Za-z]+", value) if word]


def _humanize_name(value: str) -> str:
    return " ".join(
        _identifier_words(_strip_known_suffixes(value, suffixes=("_link", "_joint")))
    ).lower()


def _parse_float_tuple(value: str) -> tuple[float, float, float]:
    parts = tuple(float(part) for part in value.split())
    if len(parts) != 3:
        raise ValueError(
            f"Expected exactly three floating-point values, got {value!r}."
        )
    return parts


def _float_attr(
    element: ET.Element, name: str, *, default: float | None = None
) -> float:
    value = element.attrib.get(name)
    if value is None:
        if default is not None:
            return default
        raise ValueError(
            f"Element <{element.tag}> is missing required attribute {name!r}."
        )
    return float(value)


def _required_attr(element: ET.Element, name: str) -> str:
    value = element.attrib.get(name)
    if value is None:
        raise ValueError(
            f"Element <{element.tag}> is missing required attribute {name!r}."
        )
    return value


def _required_child(element: ET.Element, tag: str) -> ET.Element:
    child = element.find(tag)
    if child is None:
        raise ValueError(f"Element <{element.tag}> is missing required child <{tag}>.")
    return child
