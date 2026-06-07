from __future__ import annotations

from typing import Literal, cast

import numpy as np
from scipy.spatial.transform import Rotation

from urdf.core.types import RigidTransform
from urdf.dynamics import InertiaTensor
from urdf.kinematics import (
    AnyJoint,
    ContinuousJoint,
    FixedJoint,
    FloatingJoint,
    JointEffortLimits,
    JointId,
    JointPositionLimits,
    Link,
    LinkId,
    PlanarJoint,
    PrismaticJoint,
    RevoluteJoint,
)

type InertiaSpec = tuple[float, float, float, float, float, float]
"""URDF inertia entries ordered as ixx, ixy, ixz, iyy, iyz, izz."""

type OriginSpec = tuple[tuple[float, float, float], tuple[float, float, float]]
"""URDF origin entries ordered as xyz and rpy."""

type LinkSpec = tuple[str, float, OriginSpec, InertiaSpec | None]
"""URDF-derived inertial data for a link."""

type JointLimitSpec = tuple[float, float, float, float]
"""URDF joint limits ordered as lower, upper, effort, and velocity."""

type JointTypeSpec = Literal[
    "continuous",
    "fixed",
    "floating",
    "planar",
    "prismatic",
    "revolute",
]
"""A supported URDF joint type."""

type JointSpec[LinkIdT: LinkId] = tuple[
    str,
    JointTypeSpec,
    LinkIdT,
    LinkIdT,
    OriginSpec,
    tuple[float, float, float] | None,
    JointLimitSpec | None,
]
"""URDF-derived data for a joint."""

type FixedOrRevoluteJointSpec[LinkIdT: LinkId] = tuple[
    str,
    LinkIdT,
    LinkIdT,
    OriginSpec,
    tuple[float, float, float] | None,
    JointLimitSpec | None,
]
"""URDF-derived data for a fixed or revolute joint."""


def transform_from_origin(
    origin: OriginSpec = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
) -> RigidTransform:
    """Create a rigid transform from URDF xyz/rpy values.

    Args:
        origin: The translation (xyz) and rotation (rpy roll-pitch-yaw) specification.

    Returns:
        The instantiated RigidTransform.
    """
    xyz, rpy = origin
    return RigidTransform.from_components(
        translation=np.array(xyz),
        rotation=Rotation.from_euler("xyz", np.array(rpy), degrees=False),
    )


def inertia_from_spec(spec: InertiaSpec | None) -> InertiaTensor:
    """Create an inertia tensor from URDF inertia entries.

    Args:
        spec: The six unique inertia matrix entries (ixx, ixy, ixz, iyy, iyz, izz), or None.

    Returns:
        The instantiated InertiaTensor, defaulting to zero if spec is None.
    """
    if spec is None:
        return InertiaTensor.zero()
    ixx, ixy, ixz, iyy, iyz, izz = spec
    return InertiaTensor.from_entries(
        ixx=ixx,
        ixy=ixy,
        ixz=ixz,
        iyy=iyy,
        iyz=iyz,
        izz=izz,
    )


def link_from_spec[LinkIdT: LinkId](
    link_id: LinkIdT,
    spec: LinkSpec,
) -> Link[LinkIdT]:
    """Create a link from a URDF-derived link spec.

    Args:
        link_id: The unique identifier for the link.
        spec: The link specification containing name, mass, origin, and inertia.

    Returns:
        The instantiated Link object.
    """
    name, mass, origin, inertia = spec
    return Link[LinkIdT](
        id=link_id,
        name=name,
        mass=mass,
        origin=transform_from_origin(origin),
        inertia=inertia_from_spec(inertia),
    )


def joint_from_spec[LinkIdT: LinkId, JointIdT: JointId](
    joint_id: JointIdT,
    spec: JointSpec[LinkIdT] | FixedOrRevoluteJointSpec[LinkIdT],
) -> AnyJoint[LinkIdT, JointIdT]:
    """Create a joint from a URDF-derived joint spec.

    Args:
        joint_id: The unique identifier for the joint.
        spec: The joint specification. It can be a full JointSpec (7-tuple) or
            a FixedOrRevoluteJointSpec (6-tuple, which infers fixed if axis is None, otherwise revolute).

    Returns:
        The instantiated concrete Joint object (e.g., FixedJoint, RevoluteJoint, PrismaticJoint, etc.).

    Raises:
        ValueError: If an axial joint is missing an axis, if a limited joint is missing limits,
            or if the joint type is unsupported.
    """
    if len(spec) == 6:
        name, parent, child, origin, axis, limits = spec
        joint_type: JointTypeSpec = "fixed" if axis is None else "revolute"
    else:
        name, joint_type, parent, child, origin, axis, limits = spec

    common = {
        "id": joint_id,
        "name": name,
        "parent": parent,
        "child": child,
        "origin": transform_from_origin(origin),
    }
    if joint_type == "fixed":
        return FixedJoint[LinkIdT, JointIdT](**common)
    if joint_type == "floating":
        return FloatingJoint[LinkIdT, JointIdT](**common)
    if axis is None:
        raise ValueError(
            f"Joint {joint_id!r} of type {joint_type!r} is missing an axis."
        )

    axial = {**common, "axis": np.array(axis)}
    if joint_type == "planar":
        return PlanarJoint[LinkIdT, JointIdT](**axial)
    if limits is None:
        raise ValueError(
            f"Joint {joint_id!r} of type {joint_type!r} is missing limits."
        )

    lower, upper, effort, velocity = limits
    if joint_type == "continuous":
        return ContinuousJoint[LinkIdT, JointIdT](
            **axial,
            limits=JointEffortLimits(effort=effort, velocity=velocity),
        )

    bounded_limits = JointPositionLimits(
        lower=lower,
        upper=upper,
        effort=effort,
        velocity=velocity,
    )
    if joint_type == "revolute":
        return RevoluteJoint[LinkIdT, JointIdT](**axial, limits=bounded_limits)
    if joint_type == "prismatic":
        return PrismaticJoint[LinkIdT, JointIdT](**axial, limits=bounded_limits)
    raise ValueError(f"Unsupported joint type {cast(str, joint_type)!r}.")


__all__ = [
    "FixedOrRevoluteJointSpec",
    "InertiaSpec",
    "JointLimitSpec",
    "JointSpec",
    "JointTypeSpec",
    "LinkSpec",
    "OriginSpec",
    "inertia_from_spec",
    "joint_from_spec",
    "link_from_spec",
    "transform_from_origin",
]
