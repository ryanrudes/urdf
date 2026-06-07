from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Literal

from urdf.core.types import RigidTransform, Vec3
from urdf.dynamics import InertiaTensor


class JointType(StrEnum):
    """The type of joint that connects two links."""

    REVOLUTE = "revolute"
    """A hinge joint that rotates along the axis and has a limited range specified by the upper and lower limits."""

    CONTINUOUS = "continuous"
    """A continuous hinge joint that rotates around the axis and has no upper and lower limits."""

    PRISMATIC = "prismatic"
    """A sliding joint that slides along the axis and has a limited range specified by the upper and lower limits."""

    FIXED = "fixed"
    """A fixed joint that does not move."""

    FLOATING = "floating"
    """A floating joint that allows motion for all 6 degrees of freedom."""

    PLANAR = "planar"
    """A planar joint that allows motion in a plane perpendicular to the axis."""


class LinkId(StrEnum):
    """Base class for link identifiers."""


class JointId(StrEnum):
    """Base class for joint identifiers."""


@dataclass(frozen=True, kw_only=True)
class Link[LinkIdT: LinkId]:
    """A link in a kinematic chain."""

    id: LinkIdT
    """The identifier of the link within a skeleton."""

    name: str
    """The name of the link."""

    mass: float = 0.0
    """The mass of the link."""

    origin: RigidTransform = field(default_factory=RigidTransform.identity)
    """The position and orientation of the link's center of mass frame relative to the link frame."""

    inertia: InertiaTensor = field(default_factory=InertiaTensor.zero)
    """The inertia tensor of the link."""


@dataclass(frozen=True, kw_only=True)
class JointDynamics:
    """The dynamics of a joint."""

    damping: float = 0.0
    """The physical damping value of the joint.

    For prismatic joints, this is expressed in newton-seconds per metre [N∙s/m].
    For revolute joints, this is expressed in newton-metre-seconds per radian [N∙m∙s/rad].
    """

    friction: float = 0.0
    """The physical static friction value of the joint.

    For prismatic joints, this is expressed in newtons [N].
    For revolute joints, this is expressed in newton-metres [N∙m].
    """


@dataclass(frozen=True, kw_only=True)
class JointEffortLimits:
    """The effort and velocity limits of a joint."""

    effort: float
    """The effort limit of the joint.

    For revolute and continuous joints, the effort limit is expressed in newton-metres [N∙m].
    For prismatic joints, the effort limit is expressed in newtons [N].
    """

    velocity: float
    """The bound of the magnitude of the joint velocity.

    For revolute and continuous joints, the velocity limit is expressed in radians per second [rad/s].
    For prismatic joints, the velocity limit is expressed in metres per second [m/s].
    """


@dataclass(frozen=True, kw_only=True)
class JointPositionLimits(JointEffortLimits):
    """The effort, velocity, and position limits of a bounded scalar joint."""

    lower: float
    """The lower position limit of the joint.

    For revolute joints, the lower limit is expressed in radians [rad].
    For prismatic joints, the lower limit is expressed in metres [m].
    """

    upper: float
    """The upper position limit of the joint.

    For revolute joints, the upper limit is expressed in radians [rad].
    For prismatic joints, the upper limit is expressed in metres [m].
    """


@dataclass(frozen=True, kw_only=True)
class Joint[LinkIdT: LinkId, JointIdT: JointId]:
    """A joint that connects two links."""

    id: JointIdT
    """The identifier of the joint within a skeleton."""

    name: str
    """The name of the joint."""

    type: JointType
    """The type of joint."""

    parent: LinkIdT
    """The identifier of the parent link."""

    child: LinkIdT
    """The identifier of the child link."""

    origin: RigidTransform = field(default_factory=RigidTransform.identity)
    """The transform from the parent link frame to the joint frame.

    The child link frame is located at the joint frame unless the consuming model defines an additional child offset.
    """

    dynamics: JointDynamics = field(default_factory=JointDynamics)
    """The dynamics of the joint."""


@dataclass(frozen=True, kw_only=True)
class AxialJoint[LinkIdT: LinkId, JointIdT: JointId](Joint[LinkIdT, JointIdT]):
    """A joint defined with an axis."""

    axis: Vec3
    """The joint axis specified in the joint frame.

    This is the axis of rotation for revolute and continuous joints, the axis of translation for prismatic joints,
    and the surface normal for planar joints. The axis is specified in the joint frame of reference.
    """


@dataclass(frozen=True, kw_only=True)
class ScalarAxialJoint[LinkIdT: LinkId, JointIdT: JointId](
    AxialJoint[LinkIdT, JointIdT]
):
    """A one-degree-of-freedom joint defined by a scalar coordinate along or around an axis."""


@dataclass(frozen=True, kw_only=True)
class NonAxialJoint[LinkIdT: LinkId, JointIdT: JointId](Joint[LinkIdT, JointIdT]):
    """A joint that does not use an axis in its definition."""


@dataclass(frozen=True, kw_only=True)
class RevoluteJoint[LinkIdT: LinkId, JointIdT: JointId](
    ScalarAxialJoint[LinkIdT, JointIdT]
):
    """A revolute joint that rotates around an axis and has lower and upper position limits."""

    type: Literal[JointType.REVOLUTE] = JointType.REVOLUTE
    """The type of the joint."""

    limits: JointPositionLimits
    """The effort, velocity, and position limits of the joint."""


@dataclass(frozen=True, kw_only=True)
class ContinuousJoint[LinkIdT: LinkId, JointIdT: JointId](
    ScalarAxialJoint[LinkIdT, JointIdT]
):
    """A continuous joint that rotates around an axis and has no lower or upper position limits."""

    type: Literal[JointType.CONTINUOUS] = JointType.CONTINUOUS
    """The type of the joint."""

    limits: JointEffortLimits
    """The effort and velocity limits of the joint."""


@dataclass(frozen=True, kw_only=True)
class PrismaticJoint[LinkIdT: LinkId, JointIdT: JointId](
    ScalarAxialJoint[LinkIdT, JointIdT]
):
    """A prismatic joint that slides along an axis and has lower and upper position limits."""

    type: Literal[JointType.PRISMATIC] = JointType.PRISMATIC
    """The type of the joint."""

    limits: JointPositionLimits
    """The effort, velocity, and position limits of the joint."""


@dataclass(frozen=True, kw_only=True)
class PlanarJoint[LinkIdT: LinkId, JointIdT: JointId](AxialJoint[LinkIdT, JointIdT]):
    """A planar joint that allows motion in a plane perpendicular to the axis."""

    type: Literal[JointType.PLANAR] = JointType.PLANAR
    """The type of the joint."""


@dataclass(frozen=True, kw_only=True)
class FixedJoint[LinkIdT: LinkId, JointIdT: JointId](NonAxialJoint[LinkIdT, JointIdT]):
    """A fixed joint that rigidly connects the parent link to the child link."""

    type: Literal[JointType.FIXED] = JointType.FIXED
    """The type of the joint."""


@dataclass(frozen=True, kw_only=True)
class FloatingJoint[LinkIdT: LinkId, JointIdT: JointId](
    NonAxialJoint[LinkIdT, JointIdT]
):
    """A floating joint that allows motion for all 6 degrees of freedom."""

    type: Literal[JointType.FLOATING] = JointType.FLOATING
    """The type of the joint."""


type AnyJoint[LinkIdT: LinkId, JointIdT: JointId] = (
    RevoluteJoint[LinkIdT, JointIdT]
    | ContinuousJoint[LinkIdT, JointIdT]
    | PrismaticJoint[LinkIdT, JointIdT]
    | PlanarJoint[LinkIdT, JointIdT]
    | FixedJoint[LinkIdT, JointIdT]
    | FloatingJoint[LinkIdT, JointIdT]
)
"""Any concrete joint type in a kinematic chain."""


@dataclass(frozen=True, kw_only=True)
class Linkage[LinkIdT: LinkId]:
    """A collection of links that are connected to form a kinematic chain."""

    links: dict[LinkIdT, Link[LinkIdT]]
    """The links in the kinematic chain, keyed by identifier."""

    def __post_init__(self) -> None:
        """Validate that each link is keyed by its own identifier."""
        for link_id, link in self.links.items():
            if link.id != link_id:
                raise ValueError(
                    f"Link key {link_id!r} does not match link.id {link.id!r}."
                )

    def __getitem__(self, link_id: LinkIdT) -> Link[LinkIdT]:
        """Return the link with the given identifier."""
        return self.links[link_id]

    def __contains__(self, link_id: object) -> bool:
        """Return whether the linkage contains the given link identifier."""
        return link_id in self.links


@dataclass(frozen=True, kw_only=True)
class Articulation[LinkIdT: LinkId, JointIdT: JointId]:
    """A collection of joints that are connected to form a kinematic chain."""

    joints: dict[JointIdT, AnyJoint[LinkIdT, JointIdT]]
    """The joints in the kinematic chain, keyed by identifier."""

    def __post_init__(self) -> None:
        """Validate that each joint is keyed by its own identifier."""
        for joint_id, joint in self.joints.items():
            if joint.id != joint_id:
                raise ValueError(
                    f"Joint key {joint_id!r} does not match joint.id {joint.id!r}."
                )

    def __getitem__(self, joint_id: JointIdT) -> AnyJoint[LinkIdT, JointIdT]:
        """Return the joint with the given identifier."""
        return self.joints[joint_id]

    def __contains__(self, joint_id: object) -> bool:
        """Return whether the articulation contains the given joint identifier."""
        return joint_id in self.joints


@dataclass(frozen=True, kw_only=True)
class Skeleton[LinkIdT: LinkId, JointIdT: JointId]:
    """A skeleton is a collection of links and joints that are connected to form a kinematic chain."""

    linkage: Linkage[LinkIdT]
    """The links in the skeleton."""

    articulation: Articulation[LinkIdT, JointIdT]
    """The joints in the skeleton."""

    def __post_init__(self) -> None:
        """Validate that each joint references links that exist in the skeleton."""
        for joint in self.articulation.joints.values():
            if joint.parent not in self.linkage:
                raise ValueError(
                    f"Joint {joint.id!r} has parent {joint.parent!r}, which is not in the linkage."
                )

            if joint.child not in self.linkage:
                raise ValueError(
                    f"Joint {joint.id!r} has child {joint.child!r}, which is not in the linkage."
                )

    def parent_link(self, joint: Joint[LinkIdT, JointIdT]) -> Link[LinkIdT]:
        """Return the parent link of a joint."""
        return self.linkage[joint.parent]

    def child_link(self, joint: Joint[LinkIdT, JointIdT]) -> Link[LinkIdT]:
        """Return the child link of a joint."""
        return self.linkage[joint.child]
