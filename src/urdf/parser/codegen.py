from __future__ import annotations

import difflib
import json
import keyword
import re
from pathlib import Path
from typing import Iterable, Sequence

from . import (
    Inertia,
    JointDefinition,
    JointLimit,
    LinkDefinition,
    Origin,
    RobotDefinition,
    parse_urdf,
)

_CLASS_BY_JOINT_TYPE = {
    "continuous": "ContinuousJoint",
    "fixed": "FixedJoint",
    "floating": "FloatingJoint",
    "planar": "PlanarJoint",
    "prismatic": "PrismaticJoint",
    "revolute": "RevoluteJoint",
}


def _load_robot_names() -> dict[str, tuple[str, str, str, str]]:
    """Load robot metadata configuration from assets/robots.json.

    Returns:
        A dictionary mapping lowercase robot names to a tuple of (class_prefix, constant_prefix, display_name, description).

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the configuration file is invalid JSON or lacks required fields.
    """
    parser_dir = Path(__file__).resolve().parent
    project_dir = parser_dir.parent.parent.parent
    config_path = project_dir / "assets" / "robots.json"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Robot metadata configuration file not found at '{config_path}'. "
            "This file is required to resolve robot names."
        )

    try:
        with config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Failed to parse '{config_path}': invalid JSON format."
        ) from exc

    names: dict[str, tuple[str, str, str, str]] = {}
    for key, cfg in data.items():
        class_prefix = cfg.get("class_prefix")
        constant_prefix = cfg.get("constant_prefix")
        display_name = cfg.get("display_name")
        description = cfg.get("description")

        if (
            not class_prefix
            or not constant_prefix
            or not display_name
            or not description
        ):
            raise ValueError(
                f"Missing required fields in configuration for '{key}' in '{config_path}'. "
                "Each entry must define 'class_prefix', 'constant_prefix', 'display_name', and 'description'."
            )

        names[key.lower()] = (class_prefix, constant_prefix, display_name, description)

    return names


_G1_LINK_NAMES = (
    "pelvis",
    "pelvis_contour_link",
    "left_hip_pitch_link",
    "left_hip_roll_link",
    "left_hip_yaw_link",
    "left_knee_link",
    "left_ankle_pitch_link",
    "left_ankle_roll_link",
    "right_hip_pitch_link",
    "right_hip_roll_link",
    "right_hip_yaw_link",
    "right_knee_link",
    "right_ankle_pitch_link",
    "right_ankle_roll_link",
    "waist_yaw_fixed_link",
    "torso_link",
    "logo_link",
    "head_link",
    "waist_support_link",
    "imu_in_torso",
    "imu_in_pelvis",
    "d435_link",
    "mid360_link",
    "left_shoulder_pitch_link",
    "left_shoulder_roll_link",
    "left_shoulder_yaw_link",
    "left_elbow_link",
    "left_wrist_roll_rubber_hand",
    "right_shoulder_pitch_link",
    "right_shoulder_roll_link",
    "right_shoulder_yaw_link",
    "right_elbow_link",
    "right_wrist_roll_rubber_hand",
)

_G1_JOINT_NAMES = (
    "pelvis_contour_joint",
    "left_hip_pitch_joint",
    "left_hip_roll_joint",
    "left_hip_yaw_joint",
    "left_knee_joint",
    "left_ankle_pitch_joint",
    "left_ankle_roll_joint",
    "right_hip_pitch_joint",
    "right_hip_roll_joint",
    "right_hip_yaw_joint",
    "right_knee_joint",
    "right_ankle_pitch_joint",
    "right_ankle_roll_joint",
    "waist_yaw_fixed_joint",
    "waist_yaw_joint",
    "logo_joint",
    "head_joint",
    "waist_support_joint",
    "imu_in_torso_joint",
    "imu_in_pelvis_joint",
    "d435_joint",
    "mid360_joint",
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "left_wrist_roll_joint",
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
    "right_wrist_roll_joint",
)


def export_robot_definition_code(
    urdf_path: str | Path,
    *,
    class_prefix: str | None = None,
    constant_prefix: str | None = None,
) -> str:
    """Export a URDF as a Python robot definition."""
    definition = parse_urdf(urdf_path)

    if class_prefix is None or constant_prefix is None:
        robot_names = _load_robot_names()
        urdf_stem = Path(urdf_path).stem.lower()

        if urdf_stem in robot_names:
            key = urdf_stem
        elif definition.name in robot_names:
            key = definition.name
        else:
            raise ValueError(
                f"Robot metadata not found for '{urdf_stem}' (definition name: '{definition.name}') in assets/robots.json. "
                "This metadata is required to generate the robot definition when class_prefix or constant_prefix are not provided."
            )

        known_class, known_constant, known_display, known_description = robot_names[key]
        class_name = class_prefix or known_class
        constant_name = constant_prefix or known_constant
        display_name = known_display
    else:
        class_name = class_prefix
        constant_name = constant_prefix
        display_name = _display_name(class_name)

    return _render_module(
        definition,
        class_prefix=class_name,
        constant_prefix=constant_name,
        display_name=display_name,
    )


def write_robot_definition_code(
    urdf_path: str | Path,
    output_path: str | Path,
    *,
    class_prefix: str | None = None,
    constant_prefix: str | None = None,
) -> None:
    """Write a Python robot definition generated from a URDF."""
    code = export_robot_definition_code(
        urdf_path,
        class_prefix=class_prefix,
        constant_prefix=constant_prefix,
    )
    output_file = Path(output_path)
    output_file.write_text(code, encoding="utf-8")

    # Check if we are writing to the library models directory
    resolved_output = output_file.resolve()
    models_dir = Path(__file__).resolve().parents[1] / "robots" / "models"
    if resolved_output.parent == models_dir.resolve():
        regenerate_registry_files()


def extract_model_info(file_path: Path) -> dict[str, str] | None:
    """Extract class prefix, constant prefix, and display name from a generated robot model file.

    Args:
        file_path: The path to the Python file of the robot model.

    Returns:
        A dictionary containing the extracted 'module_name', 'class_prefix', 'constant_prefix', and
        'display_name', or None if it's not a valid generated robot model.
    """
    content = file_path.read_text(encoding="utf-8")

    # Class prefix from the class definition inheriting from LinkId
    match_class = re.search(r"class\s+([A-Za-z0-9_]+)LinkId\(LinkId\):", content)
    if not match_class:
        return None
    class_prefix = match_class.group(1)

    # Constant prefix from the linkage definition
    match_const = re.search(r"([A-Z0-9_]+)_LINKAGE\s*=\s*Linkage", content)
    if not match_const:
        return None
    constant_prefix = match_const.group(1)

    # Display name from the skeleton docstring
    match_display = re.search(
        r'"""The kinematic chain for the\s+(.*?)\s+robot\."""', content
    )
    if match_display:
        display_name = match_display.group(1).strip()
    else:
        display_name = _display_name(class_prefix)

    return {
        "module_name": file_path.stem,
        "class_prefix": class_prefix,
        "constant_prefix": constant_prefix,
        "display_name": display_name,
    }


def _render_models_init(models: list[dict[str, str]]) -> str:
    lines = [
        "# Generated by urdf.parser.codegen. Do not edit manually.",
        '"""Generated robot model definitions."""',
        "from __future__ import annotations",
        "",
    ]
    for m in models:
        mod = m["module_name"]
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        lines.append(f"from .{mod} import (")
        lines.append(f"    {const},")
        lines.append(f"    {const}_ARTICULATION,")
        lines.append(f"    {const}_LINKAGE,")
        lines.append(f"    {cls}Joint,")
        lines.append(f"    {cls}JointId,")
        lines.append(f"    {cls}Link,")
        lines.append(f"    {cls}LinkId,")
        lines.append(")")

    lines.append("")
    lines.append("__all__ = [")
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        display = m["display_name"]
        lines.append(f"    # {display}")
        lines.append(f'    "{const}",')
        lines.append(f'    "{const}_ARTICULATION",')
        lines.append(f'    "{const}_LINKAGE",')
        lines.append(f'    "{cls}Joint",')
        lines.append(f'    "{cls}JointId",')
        lines.append(f'    "{cls}Link",')
        lines.append(f'    "{cls}LinkId",')
    lines.append("]")
    return "\n".join(lines) + "\n"


def _render_registry(models: list[dict[str, str]]) -> str:
    import_sections = []
    for m in models:
        mod = m["module_name"]
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        import_sections.append(
            f"from .models.{mod} import (\n    {const},\n    {cls}JointId,\n    {cls}LinkId,\n)"
        )

    imports_str = "\n".join(import_sections)

    enum_members = []
    for m in models:
        const = m["constant_prefix"]
        description = m.get("description", f"The {m['display_name']} robot.")
        enum_members.append(
            f'    {const} = {json.dumps(const.lower())}\n    """{description}"""'
        )

    enum_members_str = "\n\n".join(enum_members)

    aliases = []
    for m in models:
        cls = m["class_prefix"]
        display = m["display_name"]
        aliases.append(
            f'type {cls}Robot = Robot[{cls}LinkId, {cls}JointId]\n"""The robot type for the {display} robot."""\n\ntype {cls}Skeleton = Skeleton[{cls}LinkId, {cls}JointId]\n"""The skeleton type for the {display} robot."""'
        )

    aliases_str = "\n\n".join(aliases)

    robot_instances = []
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        display = m["display_name"]
        robot_instances.append(
            f'{const}_ROBOT = Robot[{cls}LinkId, {cls}JointId](\n    id=RobotId.{const},\n    name={json.dumps(display)},\n    skeleton={const},\n)\n"""The robot model for the {display} robot."""'
        )

    robot_instances_str = "\n\n".join(robot_instances)

    dict_entries = []
    for m in models:
        const = m["constant_prefix"]
        dict_entries.append(f"    str(RobotId.{const}): {const}_ROBOT,")

    dict_entries_str = "\n".join(dict_entries)

    overloads_get_robot = []
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        display = m["display_name"]
        overloads_get_robot.append(
            f'@overload\ndef get_robot(robot_id: Literal[RobotId.{const}]) -> {cls}Robot:\n    """Return the robot model for the {display} robot."""\n    ...'
        )

    overloads_get_robot_str = "\n\n\n".join(overloads_get_robot)

    overloads_get_skeleton = []
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        display = m["display_name"]
        overloads_get_skeleton.append(
            f'@overload\ndef get_skeleton(\n    robot_id: Literal[RobotId.{const}],\n) -> {cls}Skeleton:\n    """Return the skeleton for the {display} robot."""\n    ...'
        )

    overloads_get_skeleton_str = "\n\n\n".join(overloads_get_skeleton)

    code = f"""# Generated by urdf.parser.codegen. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Literal, overload

from urdf.kinematics.kinematic_chain import JointId, LinkId, Skeleton

{imports_str}


class RobotId(StrEnum):
    \"\"\"Identifiers for built-in robot definitions.\"\"\"

{enum_members_str}


@dataclass(frozen=True, kw_only=True)
class Robot[LinkIdT: LinkId, JointIdT: JointId]:
    \"\"\"A robot model with kinematics and metadata.\"\"\"

    id: str
    \"\"\"The identifier of the robot.\"\"\"

    name: str
    \"\"\"The human-readable name of the robot.\"\"\"

    skeleton: Skeleton[LinkIdT, JointIdT]
    \"\"\"The kinematic chain of the robot.\"\"\"


type AnyRobot = Robot[Any, Any]
\"\"\"A robot whose concrete link and joint identifier types are erased.\"\"\"

{aliases_str}

type AnySkeleton = Skeleton[Any, Any]
\"\"\"A skeleton whose concrete link and joint identifier types are erased.\"\"\"

{robot_instances_str}

_BUILT_IN_ROBOT_IDS = frozenset(str(robot_id) for robot_id in RobotId)
_ROBOTS: dict[str, AnyRobot] = {{
{dict_entries_str}
}}


{overloads_get_robot_str}


@overload
def get_robot(robot_id: str) -> AnyRobot:
    \"\"\"Return the robot model for the given robot identifier.\"\"\"
    ...


def get_robot(robot_id: str) -> AnyRobot:
    \"\"\"Return the robot model for the given robot identifier.\"\"\"
    try:
        return _ROBOTS[str(robot_id)]
    except KeyError as exc:
        raise KeyError(f"No robot registered for {{robot_id!r}}.") from exc


{overloads_get_skeleton_str}


@overload
def get_skeleton(robot_id: str) -> AnySkeleton:
    \"\"\"Return the skeleton for the given robot identifier.\"\"\"
    ...


def get_skeleton(robot_id: str) -> AnySkeleton:
    \"\"\"Return the skeleton for the given robot identifier.\"\"\"
    return get_robot(robot_id).skeleton


def register_robot(robot: AnyRobot, *, replace: bool = False) -> None:
    \"\"\"Register a robot definition for runtime lookup.\"\"\"
    robot_id = str(robot.id)
    if not robot_id:
        raise ValueError("Robot IDs cannot be empty.")
    if robot_id in _ROBOTS and not replace:
        raise ValueError(f"A robot is already registered for {{robot_id!r}}.")
    _ROBOTS[robot_id] = robot


def unregister_robot(robot_id: str, *, allow_builtin: bool = False) -> AnyRobot:
    \"\"\"Remove and return a runtime robot definition.\"\"\"
    normalized_id = str(robot_id)
    if normalized_id in _BUILT_IN_ROBOT_IDS and not allow_builtin:
        raise ValueError(f"Cannot unregister built-in robot {{normalized_id!r}}.")
    try:
        return _ROBOTS.pop(normalized_id)
    except KeyError as exc:
        raise KeyError(f"No robot registered for {{robot_id!r}}.") from exc


def registered_robot_ids() -> frozenset[str]:
    \"\"\"Return the identifiers of all registered robots.\"\"\"
    return frozenset(_ROBOTS)
"""
    return code


def _render_robots_init(models: list[dict[str, str]]) -> str:
    import_models = []
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        import_models.append(f"    {const},")
        import_models.append(f"    {const}_ARTICULATION,")
        import_models.append(f"    {const}_LINKAGE,")
        import_models.append(f"    {cls}Joint,")
        import_models.append(f"    {cls}JointId,")
        import_models.append(f"    {cls}Link,")
        import_models.append(f"    {cls}LinkId,")

    import_models_str = "\n".join(import_models)

    import_registry = []
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        import_registry.append(f"    {const}_ROBOT,")
        import_registry.append(f"    {cls}Robot,")
        import_registry.append(f"    {cls}Skeleton,")

    import_registry_str = "\n".join(import_registry)

    all_exports = [
        "AnyRobot",
        "AnySkeleton",
        "Robot",
        "RobotId",
    ]
    for m in models:
        const = m["constant_prefix"]
        cls = m["class_prefix"]
        all_exports.extend(
            [
                const,
                f"{const}_ARTICULATION",
                f"{const}_LINKAGE",
                f"{const}_ROBOT",
                f"{cls}Joint",
                f"{cls}JointId",
                f"{cls}Link",
                f"{cls}LinkId",
                f"{cls}Robot",
                f"{cls}Skeleton",
            ]
        )
    all_exports.extend(
        [
            "get_robot",
            "get_skeleton",
            "register_robot",
            "registered_robot_ids",
            "unregister_robot",
        ]
    )

    # Sort exports alphabetically
    all_exports.sort()
    all_exports_str = ",\n".join(f'    "{name}"' for name in all_exports)

    code = f"""# Generated by urdf.parser.codegen. Do not edit manually.
\"\"\"Robots module containing all generated robot model definitions.\"\"\"
from __future__ import annotations

from .models import (
{import_models_str}
)
from .registry import (
    AnyRobot,
    AnySkeleton,
    Robot,
    RobotId,
{import_registry_str}
    get_robot,
    get_skeleton,
    register_robot,
    registered_robot_ids,
    unregister_robot,
)

__all__ = [
{all_exports_str},
]
"""
    return code


def regenerate_registry_files() -> None:
    """Regenerate the models __init__.py, registry.py, and robots __init__.py files."""
    parser_dir = Path(__file__).resolve().parent
    robots_dir = parser_dir.parent / "robots"
    models_dir = robots_dir / "models"

    # Load names configuration to get the description
    robot_names = _load_robot_names()

    # Find all Python files in models/ excluding __init__.py
    model_files = sorted(models_dir.glob("*.py"))
    models = []
    for f in model_files:
        if f.name == "__init__.py":
            continue
        info = extract_model_info(f)
        if info is not None:
            mod_name = info["module_name"]
            cfg = robot_names.get(mod_name)
            if cfg is not None:
                info["description"] = cfg[3]
            else:
                info["description"] = f"The {info['display_name']} robot."
            models.append(info)

    # Sort models by module_name to keep generation deterministic
    models.sort(key=lambda m: m["module_name"])

    # 1. Regenerate src/urdf/robots/models/__init__.py
    models_init_code = _render_models_init(models)
    (models_dir / "__init__.py").write_text(models_init_code, encoding="utf-8")

    # 2. Regenerate src/urdf/robots/registry.py
    registry_code = _render_registry(models)
    (robots_dir / "registry.py").write_text(registry_code, encoding="utf-8")

    # 3. Regenerate src/urdf/robots/__init__.py
    robots_init_code = _render_robots_init(models)
    (robots_dir / "__init__.py").write_text(robots_init_code, encoding="utf-8")

    # Format all files under robots_dir if ruff is available
    import shutil
    import subprocess

    ruff_path = shutil.which("ruff")
    if ruff_path:
        try:
            subprocess.run(
                [ruff_path, "format", str(robots_dir)],
                capture_output=True,
                check=True,
            )
        except Exception:
            pass


def sync_assets() -> None:
    """Synchronize all URDF assets with the generated Python definitions and registry."""
    parser_dir = Path(__file__).resolve().parent
    src_dir = parser_dir.parent
    project_dir = src_dir.parent.parent
    assets_dir = project_dir / "assets"

    if not assets_dir.exists():
        raise FileNotFoundError(f"Assets directory not found at {assets_dir}")

    models_dir = src_dir / "robots" / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    urdf_files = sorted(assets_dir.glob("*.urdf"))
    for urdf_file in urdf_files:
        name = urdf_file.stem.lower()
        output_file = models_dir / f"{name}.py"
        write_robot_definition_code(urdf_file, output_file)

    # Finally, regenerate registry files
    regenerate_registry_files()


def _render_module(
    definition: RobotDefinition,
    *,
    class_prefix: str,
    constant_prefix: str,
    display_name: str,
) -> str:
    link_members = _enum_members(
        (link.name for link in definition.links), suffix="_link"
    )
    joint_members = _enum_members(
        (joint.name for joint in definition.joints), suffix="_joint"
    )
    joint_classes = _used_joint_classes(definition.joints)

    sections = [
        _render_imports(joint_classes),
        _render_enum(
            f"{class_prefix}LinkId",
            "LinkId",
            f"Link identifiers for the {display_name} robot.",
            (
                (
                    link.name,
                    link_members[link.name],
                    _identifier_docstring(link.name, "link"),
                )
                for link in definition.links
            ),
        ),
        _render_enum(
            f"{class_prefix}JointId",
            "JointId",
            f"Joint identifiers for the {display_name} robot.",
            (
                (
                    joint.name,
                    joint_members[joint.name],
                    _identifier_docstring(joint.name, "joint"),
                )
                for joint in definition.joints
            ),
        ),
        _render_aliases(class_prefix, display_name, joint_classes),
        _render_link_specs(class_prefix, display_name, definition.links, link_members),
        _render_joint_specs(
            class_prefix,
            display_name,
            definition.joints,
            link_members,
            joint_members,
        ),
        _render_constants(class_prefix, constant_prefix, display_name),
    ]
    return "\n\n\n".join(sections) + "\n"


def _render_imports(joint_classes: Sequence[str]) -> str:
    names = [
        "Articulation",
        *joint_classes,
        "JointId",
        "Link",
        "LinkId",
        "Linkage",
        "Skeleton",
    ]
    imports = "\n".join(f"    {name}," for name in sorted(set(names)))
    return f"""from __future__ import annotations

from urdf.kinematics import (
{imports}
)
from urdf.robots.utils import (
    JointSpec,
    LinkSpec,
    joint_from_spec,
    link_from_spec,
)"""


def _render_enum(
    class_name: str,
    base_name: str,
    docstring: str,
    members: Iterable[tuple[str, str, str]],
) -> str:
    lines = [f"class {class_name}({base_name}):", f'    """{docstring}"""', ""]
    for value, member, member_docstring in members:
        lines.extend(
            [
                f"    {member}: str = {_quote(value)}",
                f'    """{member_docstring}"""',
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def _render_aliases(
    class_prefix: str, display_name: str, joint_classes: Sequence[str]
) -> str:
    joint_union = "\n    | ".join(
        f"{joint_class}[{class_prefix}LinkId, {class_prefix}JointId]"
        for joint_class in joint_classes
    )
    return f"""type {class_prefix}Link = Link[{class_prefix}LinkId]
\"\"\"A link in the {display_name} robot.\"\"\"

type {class_prefix}Joint = (
    {joint_union}
)
\"\"\"A joint in the {display_name} robot.\"\"\"

type {class_prefix}JointSpec = JointSpec[{class_prefix}LinkId]
\"\"\"URDF-derived data for a joint in the {display_name} robot.\"\"\""""


def _render_link_specs(
    class_prefix: str,
    display_name: str,
    links: Sequence[LinkDefinition],
    members: dict[str, str],
) -> str:
    lines = [f"_LINK_SPECS: dict[{class_prefix}LinkId, LinkSpec] = {{"]
    for link in links:
        lines.extend(
            [
                f"    {class_prefix}LinkId.{members[link.name]}: (",
                f"        {_quote(link.name)},",
                f"        {_format_float(link.mass)},",
                f"        {_format_origin(link.origin)},",
                *_format_optional_inertia_lines(link.inertia),
                "    ),",
            ]
        )
    lines.extend(
        [
            "}",
            f'"""URDF-derived link specifications for the {display_name} robot."""',
        ]
    )
    return "\n".join(lines)


def _render_joint_specs(
    class_prefix: str,
    display_name: str,
    joints: Sequence[JointDefinition],
    link_members: dict[str, str],
    joint_members: dict[str, str],
) -> str:
    lines = [f"_JOINT_SPECS: dict[{class_prefix}JointId, {class_prefix}JointSpec] = {{"]
    for joint in joints:
        lines.extend(
            [
                f"    {class_prefix}JointId.{joint_members[joint.name]}: (",
                f"        {_quote(joint.name)},",
                f"        {_quote(joint.type)},",
                f"        {class_prefix}LinkId.{link_members[joint.parent]},",
                f"        {class_prefix}LinkId.{link_members[joint.child]},",
                f"        {_format_origin(joint.origin)},",
                f"        {_format_tuple(joint.axis) if joint.axis is not None else 'None'},",
                f"        {_format_limit(joint.limit)},",
                "    ),",
            ]
        )
    lines.extend(
        [
            "}",
            f'"""URDF-derived joint specifications for the {display_name} robot."""',
        ]
    )
    return "\n".join(lines)


def _render_constants(
    class_prefix: str, constant_prefix: str, display_name: str
) -> str:
    return f"""{constant_prefix}_LINKAGE = Linkage[{class_prefix}LinkId](
    links={{
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    }},
)
\"\"\"The linkage for the {display_name} robot.\"\"\"

{constant_prefix}_ARTICULATION = Articulation[
    {class_prefix}LinkId, {class_prefix}JointId
](
    joints={{
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    }},
)
\"\"\"The articulation for the {display_name} robot.\"\"\"

{constant_prefix} = Skeleton[{class_prefix}LinkId, {class_prefix}JointId](
    linkage={constant_prefix}_LINKAGE,
    articulation={constant_prefix}_ARTICULATION,
)
\"\"\"The kinematic chain for the {display_name} robot.\"\"\""""


def _used_joint_classes(joints: Sequence[JointDefinition]) -> list[str]:
    used = {_CLASS_BY_JOINT_TYPE[joint.type] for joint in joints}
    order = [
        "FixedJoint",
        "FloatingJoint",
        "RevoluteJoint",
        "ContinuousJoint",
        "PrismaticJoint",
        "PlanarJoint",
    ]
    return [joint_class for joint_class in order if joint_class in used]


def _format_origin(origin: Origin) -> str:
    return f"({_format_tuple(origin.xyz)}, {_format_tuple(origin.rpy)})"


def _format_optional_inertia_lines(inertia: Inertia | None) -> list[str]:
    if inertia is None:
        return ["        None,"]
    values = (
        inertia.ixx,
        inertia.ixy,
        inertia.ixz,
        inertia.iyy,
        inertia.iyz,
        inertia.izz,
    )
    return [
        "        (",
        *[f"            {_format_float(value)}," for value in values],
        "        ),",
    ]


def _format_limit(limit: JointLimit | None) -> str:
    if limit is None:
        return "None"
    return _format_tuple((limit.lower, limit.upper, limit.effort, limit.velocity))


def _format_tuple(values: Sequence[float]) -> str:
    return "(" + ", ".join(_format_float(value) for value in values) + ")"


def _format_float(value: float) -> str:
    return repr(float(value))


def _quote(value: str) -> str:
    return json.dumps(value)


def _identifier_docstring(identifier: str, kind: str) -> str:
    known_names = _G1_LINK_NAMES if kind == "link" else _G1_JOINT_NAMES
    normalized = _normalized_identifier(identifier)
    match = max(
        known_names,
        key=lambda candidate: difflib.SequenceMatcher(
            None,
            normalized,
            _normalized_identifier(candidate),
        ).ratio(),
    )
    similarity = difflib.SequenceMatcher(
        None,
        normalized,
        _normalized_identifier(match),
    ).ratio()
    if similarity >= 0.82:
        description = _humanize_identifier(match)
        return f"The {description} {kind}."
    return f"{kind.capitalize()} with ID {identifier}."


def _enum_members(names: Iterable[str], *, suffix: str) -> dict[str, str]:
    members: dict[str, str] = {}
    used: set[str] = set()
    for name in names:
        base = name[: -len(suffix)] if name.endswith(suffix) else name
        member = _upper_snake(base)
        if not member or member[0].isdigit() or keyword.iskeyword(member.lower()):
            member = f"_{member}"
        candidate = member
        index = 2
        while candidate in used:
            candidate = f"{member}_{index}"
            index += 1
        used.add(candidate)
        members[name] = candidate
    return members


def _pascal_case(value: str) -> str:
    return "".join(word.capitalize() for word in _identifier_words(value)) or "Robot"


def _upper_snake(value: str) -> str:
    return "_".join(word.upper() for word in _identifier_words(value)) or "ROBOT"


def _display_name(value: str) -> str:
    return " ".join(_identifier_words(value))


def _humanize_identifier(value: str) -> str:
    value = re.sub(r"_(?:link|joint)$", "", value)
    return " ".join(_identifier_words(value)).lower()


def _normalized_identifier(value: str) -> str:
    return re.sub(r"_(?:link|joint)$", "", value).lower()


def _identifier_words(value: str) -> list[str]:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", value)
    return [word for word in re.split(r"[^0-9A-Za-z]+", value) if word]
