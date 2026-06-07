from __future__ import annotations

from urdf.kinematics import (
    Articulation,
    FixedJoint,
    JointId,
    Link,
    LinkId,
    Linkage,
    RevoluteJoint,
    Skeleton,
)
from urdf.robots.utils import (
    JointSpec,
    LinkSpec,
    joint_from_spec,
    link_from_spec,
)


class UnitreeH1WithHandLinkId(LinkId):
    """Link identifiers for the Unitree H1 with Hand robot."""

    PELVIS: str = "pelvis"
    """The pelvis link."""

    LEFT_HIP_YAW: str = "left_hip_yaw_link"
    """The left hip yaw link."""

    LEFT_HIP_ROLL: str = "left_hip_roll_link"
    """The left hip roll link."""

    LEFT_HIP_PITCH: str = "left_hip_pitch_link"
    """The left hip pitch link."""

    LEFT_KNEE: str = "left_knee_link"
    """The left knee link."""

    LEFT_ANKLE: str = "left_ankle_link"
    """Link with ID left_ankle_link."""

    RIGHT_HIP_YAW: str = "right_hip_yaw_link"
    """The right hip yaw link."""

    RIGHT_HIP_ROLL: str = "right_hip_roll_link"
    """The right hip roll link."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch_link"
    """The right hip pitch link."""

    RIGHT_KNEE: str = "right_knee_link"
    """The right knee link."""

    RIGHT_ANKLE: str = "right_ankle_link"
    """Link with ID right_ankle_link."""

    TORSO: str = "torso_link"
    """The torso link."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch_link"
    """The left shoulder pitch link."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll_link"
    """The left shoulder roll link."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw_link"
    """The left shoulder yaw link."""

    LEFT_ELBOW: str = "left_elbow_link"
    """The left elbow link."""

    LEFT_HAND: str = "left_hand_link"
    """Link with ID left_hand_link."""

    L_HAND_BASE: str = "L_hand_base_link"
    """Link with ID L_hand_base_link."""

    L_THUMB_PROXIMAL_BASE: str = "L_thumb_proximal_base"
    """Link with ID L_thumb_proximal_base."""

    L_THUMB_PROXIMAL: str = "L_thumb_proximal"
    """Link with ID L_thumb_proximal."""

    L_THUMB_INTERMEDIATE: str = "L_thumb_intermediate"
    """Link with ID L_thumb_intermediate."""

    L_THUMB_DISTAL: str = "L_thumb_distal"
    """Link with ID L_thumb_distal."""

    L_INDEX_PROXIMAL: str = "L_index_proximal"
    """Link with ID L_index_proximal."""

    L_INDEX_INTERMEDIATE: str = "L_index_intermediate"
    """Link with ID L_index_intermediate."""

    L_MIDDLE_PROXIMAL: str = "L_middle_proximal"
    """Link with ID L_middle_proximal."""

    L_MIDDLE_INTERMEDIATE: str = "L_middle_intermediate"
    """Link with ID L_middle_intermediate."""

    L_RING_PROXIMAL: str = "L_ring_proximal"
    """Link with ID L_ring_proximal."""

    L_RING_INTERMEDIATE: str = "L_ring_intermediate"
    """Link with ID L_ring_intermediate."""

    L_PINKY_PROXIMAL: str = "L_pinky_proximal"
    """Link with ID L_pinky_proximal."""

    L_PINKY_INTERMEDIATE: str = "L_pinky_intermediate"
    """Link with ID L_pinky_intermediate."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_link"
    """The right shoulder pitch link."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_link"
    """The right shoulder roll link."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_link"
    """The right shoulder yaw link."""

    RIGHT_ELBOW: str = "right_elbow_link"
    """The right elbow link."""

    RIGHT_HAND: str = "right_hand_link"
    """Link with ID right_hand_link."""

    R_HAND_BASE: str = "R_hand_base_link"
    """Link with ID R_hand_base_link."""

    R_THUMB_PROXIMAL_BASE: str = "R_thumb_proximal_base"
    """Link with ID R_thumb_proximal_base."""

    R_THUMB_PROXIMAL: str = "R_thumb_proximal"
    """Link with ID R_thumb_proximal."""

    R_THUMB_INTERMEDIATE: str = "R_thumb_intermediate"
    """Link with ID R_thumb_intermediate."""

    R_THUMB_DISTAL: str = "R_thumb_distal"
    """Link with ID R_thumb_distal."""

    R_INDEX_PROXIMAL: str = "R_index_proximal"
    """Link with ID R_index_proximal."""

    R_INDEX_INTERMEDIATE: str = "R_index_intermediate"
    """Link with ID R_index_intermediate."""

    R_MIDDLE_PROXIMAL: str = "R_middle_proximal"
    """Link with ID R_middle_proximal."""

    R_MIDDLE_INTERMEDIATE: str = "R_middle_intermediate"
    """Link with ID R_middle_intermediate."""

    R_RING_PROXIMAL: str = "R_ring_proximal"
    """Link with ID R_ring_proximal."""

    R_RING_INTERMEDIATE: str = "R_ring_intermediate"
    """Link with ID R_ring_intermediate."""

    R_PINKY_PROXIMAL: str = "R_pinky_proximal"
    """Link with ID R_pinky_proximal."""

    R_PINKY_INTERMEDIATE: str = "R_pinky_intermediate"
    """Link with ID R_pinky_intermediate."""

    LOGO: str = "logo_link"
    """The logo link."""

    D435_LEFT_IMAGER: str = "d435_left_imager_link"
    """Link with ID d435_left_imager_link."""

    D435_RGB_MODULE: str = "d435_rgb_module_link"
    """Link with ID d435_rgb_module_link."""

    MID360: str = "mid360_link"
    """The mid360 link."""


class UnitreeH1WithHandJointId(JointId):
    """Joint identifiers for the Unitree H1 with Hand robot."""

    LEFT_HIP_YAW: str = "left_hip_yaw_joint"
    """The left hip yaw joint."""

    LEFT_HIP_ROLL: str = "left_hip_roll_joint"
    """The left hip roll joint."""

    LEFT_HIP_PITCH: str = "left_hip_pitch_joint"
    """The left hip pitch joint."""

    LEFT_KNEE: str = "left_knee_joint"
    """The left knee joint."""

    LEFT_ANKLE: str = "left_ankle_joint"
    """Joint with ID left_ankle_joint."""

    RIGHT_HIP_YAW: str = "right_hip_yaw_joint"
    """The right hip yaw joint."""

    RIGHT_HIP_ROLL: str = "right_hip_roll_joint"
    """The right hip roll joint."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch_joint"
    """The right hip pitch joint."""

    RIGHT_KNEE: str = "right_knee_joint"
    """The right knee joint."""

    RIGHT_ANKLE: str = "right_ankle_joint"
    """Joint with ID right_ankle_joint."""

    TORSO: str = "torso_joint"
    """Joint with ID torso_joint."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch_joint"
    """The left shoulder pitch joint."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll_joint"
    """The left shoulder roll joint."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw_joint"
    """The left shoulder yaw joint."""

    LEFT_ELBOW: str = "left_elbow_joint"
    """The left elbow joint."""

    LEFT_HAND: str = "left_hand_joint"
    """Joint with ID left_hand_joint."""

    L_BASE_LINK: str = "L_base_link_joint"
    """Joint with ID L_base_link_joint."""

    L_THUMB_PROXIMAL_YAW: str = "L_thumb_proximal_yaw_joint"
    """Joint with ID L_thumb_proximal_yaw_joint."""

    L_THUMB_PROXIMAL_PITCH: str = "L_thumb_proximal_pitch_joint"
    """Joint with ID L_thumb_proximal_pitch_joint."""

    L_THUMB_INTERMEDIATE: str = "L_thumb_intermediate_joint"
    """Joint with ID L_thumb_intermediate_joint."""

    L_THUMB_DISTAL: str = "L_thumb_distal_joint"
    """Joint with ID L_thumb_distal_joint."""

    L_INDEX_PROXIMAL: str = "L_index_proximal_joint"
    """Joint with ID L_index_proximal_joint."""

    L_INDEX_INTERMEDIATE: str = "L_index_intermediate_joint"
    """Joint with ID L_index_intermediate_joint."""

    L_MIDDLE_PROXIMAL: str = "L_middle_proximal_joint"
    """Joint with ID L_middle_proximal_joint."""

    L_MIDDLE_INTERMEDIATE: str = "L_middle_intermediate_joint"
    """Joint with ID L_middle_intermediate_joint."""

    L_RING_PROXIMAL: str = "L_ring_proximal_joint"
    """Joint with ID L_ring_proximal_joint."""

    L_RING_INTERMEDIATE: str = "L_ring_intermediate_joint"
    """Joint with ID L_ring_intermediate_joint."""

    L_PINKY_PROXIMAL: str = "L_pinky_proximal_joint"
    """Joint with ID L_pinky_proximal_joint."""

    L_PINKY_INTERMEDIATE: str = "L_pinky_intermediate_joint"
    """Joint with ID L_pinky_intermediate_joint."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_joint"
    """The right shoulder pitch joint."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_joint"
    """The right shoulder roll joint."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_joint"
    """The right shoulder yaw joint."""

    RIGHT_ELBOW: str = "right_elbow_joint"
    """The right elbow joint."""

    RIGHT_HAND: str = "right_hand_joint"
    """Joint with ID right_hand_joint."""

    R_BASE_LINK: str = "R_base_link_joint"
    """Joint with ID R_base_link_joint."""

    R_THUMB_PROXIMAL_YAW: str = "R_thumb_proximal_yaw_joint"
    """Joint with ID R_thumb_proximal_yaw_joint."""

    R_THUMB_PROXIMAL_PITCH: str = "R_thumb_proximal_pitch_joint"
    """Joint with ID R_thumb_proximal_pitch_joint."""

    R_THUMB_INTERMEDIATE: str = "R_thumb_intermediate_joint"
    """Joint with ID R_thumb_intermediate_joint."""

    R_THUMB_DISTAL: str = "R_thumb_distal_joint"
    """Joint with ID R_thumb_distal_joint."""

    R_INDEX_PROXIMAL: str = "R_index_proximal_joint"
    """Joint with ID R_index_proximal_joint."""

    R_INDEX_INTERMEDIATE: str = "R_index_intermediate_joint"
    """Joint with ID R_index_intermediate_joint."""

    R_MIDDLE_PROXIMAL: str = "R_middle_proximal_joint"
    """Joint with ID R_middle_proximal_joint."""

    R_MIDDLE_INTERMEDIATE: str = "R_middle_intermediate_joint"
    """Joint with ID R_middle_intermediate_joint."""

    R_RING_PROXIMAL: str = "R_ring_proximal_joint"
    """Joint with ID R_ring_proximal_joint."""

    R_RING_INTERMEDIATE: str = "R_ring_intermediate_joint"
    """Joint with ID R_ring_intermediate_joint."""

    R_PINKY_PROXIMAL: str = "R_pinky_proximal_joint"
    """Joint with ID R_pinky_proximal_joint."""

    R_PINKY_INTERMEDIATE: str = "R_pinky_intermediate_joint"
    """Joint with ID R_pinky_intermediate_joint."""

    LOGO: str = "logo_joint"
    """The logo joint."""

    D435_LEFT_IMAGER: str = "d435_left_imager_joint"
    """Joint with ID d435_left_imager_joint."""

    D435_RGB_MODULE: str = "d435_rgb_module_joint"
    """Joint with ID d435_rgb_module_joint."""

    MID360: str = "mid360_joint"
    """The mid360 joint."""


type UnitreeH1WithHandLink = Link[UnitreeH1WithHandLinkId]
"""A link in the Unitree H1 with Hand robot."""

type UnitreeH1WithHandJoint = (
    FixedJoint[UnitreeH1WithHandLinkId, UnitreeH1WithHandJointId]
    | RevoluteJoint[UnitreeH1WithHandLinkId, UnitreeH1WithHandJointId]
)
"""A joint in the Unitree H1 with Hand robot."""

type UnitreeH1WithHandJointSpec = JointSpec[UnitreeH1WithHandLinkId]
"""URDF-derived data for a joint in the Unitree H1 with Hand robot."""


_LINK_SPECS: dict[UnitreeH1WithHandLinkId, LinkSpec] = {
    UnitreeH1WithHandLinkId.PELVIS: (
        "pelvis",
        5.39,
        ((-0.0002, 4e-05, -0.04522), (0.0, 0.0, 0.0)),
        (
            0.044582,
            8.7034e-05,
            -1.9893e-05,
            0.0082464,
            4.021e-06,
            0.049021,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_HIP_YAW: (
        "left_hip_yaw_link",
        2.244,
        ((-0.04923, 0.0001, 0.0072), (0.0, 0.0, 0.0)),
        (
            0.0025731,
            9.159e-06,
            -0.00051948,
            0.0030444,
            1.949e-06,
            0.0022883,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_HIP_ROLL: (
        "left_hip_roll_link",
        2.232,
        ((-0.0058, -0.00319, -9e-05), (0.0, 0.0, 0.0)),
        (
            0.0020603,
            3.2115e-05,
            2.878e-06,
            0.0022482,
            -7.813e-06,
            0.0024323,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_HIP_PITCH: (
        "left_hip_pitch_link",
        4.152,
        ((0.00746, -0.02346, -0.08193), (0.0, 0.0, 0.0)),
        (
            0.082618,
            -0.00066654,
            0.0040725,
            0.081579,
            0.0072024,
            0.0060081,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_KNEE: (
        "left_knee_link",
        1.721,
        ((-0.00136, -0.00512, -0.1384), (0.0, 0.0, 0.0)),
        (
            0.012205,
            -6.8431e-05,
            0.0010862,
            0.012509,
            0.00022549,
            0.0020629,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_ANKLE: (
        "left_ankle_link",
        0.474,
        ((0.042575, -1e-06, -0.044672), (0.0, 0.0, 0.0)),
        (
            0.000159668,
            -5e-09,
            0.000141063,
            0.002900286,
            1.4e-08,
            0.002805438,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_HIP_YAW: (
        "right_hip_yaw_link",
        2.244,
        ((-0.04923, -0.0001, 0.0072), (0.0, 0.0, 0.0)),
        (
            0.0025731,
            -9.159e-06,
            -0.00051948,
            0.0030444,
            -1.949e-06,
            0.0022883,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_HIP_ROLL: (
        "right_hip_roll_link",
        2.232,
        ((-0.0058, 0.00319, -9e-05), (0.0, 0.0, 0.0)),
        (
            0.0020603,
            -3.2115e-05,
            2.878e-06,
            0.0022482,
            7.813e-06,
            0.0024323,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_link",
        4.152,
        ((0.00746, 0.02346, -0.08193), (0.0, 0.0, 0.0)),
        (
            0.082618,
            0.00066654,
            0.0040725,
            0.081579,
            -0.0072024,
            0.0060081,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_KNEE: (
        "right_knee_link",
        1.721,
        ((-0.00136, 0.00512, -0.1384), (0.0, 0.0, 0.0)),
        (
            0.012205,
            6.8431e-05,
            0.0010862,
            0.012509,
            -0.00022549,
            0.0020629,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_ANKLE: (
        "right_ankle_link",
        0.474,
        ((0.042575, 1e-06, -0.044672), (0.0, 0.0, 0.0)),
        (
            0.000159668,
            5e-09,
            0.000141063,
            0.002900286,
            -1.4e-08,
            0.002805438,
        ),
    ),
    UnitreeH1WithHandLinkId.TORSO: (
        "torso_link",
        21.189,
        ((0.000489, 0.002797, 0.20484), (0.0, 0.0, 0.0)),
        (
            0.51940891,
            -0.00057306,
            0.0021612,
            0.43662112,
            -0.00079496,
            0.13627422,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_link",
        1.033,
        ((0.005045, 0.053657, -0.015715), (0.0, 0.0, 0.0)),
        (
            0.0012985,
            -1.7333e-05,
            8.683e-06,
            0.00087279,
            3.9656e-05,
            0.00097338,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_link",
        0.793,
        ((0.000679, 0.00115, -0.094076), (0.0, 0.0, 0.0)),
        (
            0.0015742,
            2.298e-06,
            -7.2265e-05,
            0.0016973,
            -6.3691e-05,
            0.0010183,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_link",
        0.839,
        ((0.01365, 0.002767, -0.16266), (0.0, 0.0, 0.0)),
        (
            0.003664,
            -1.0671e-05,
            0.00034733,
            0.0040789,
            7.0213e-05,
            0.00066383,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_ELBOW: (
        "left_elbow_link",
        0.723,
        ((0.164862, 0.000118, -0.015734), (0.0, 0.0, 0.0)),
        (
            0.00049639,
            -3.3971e-05,
            0.000316026,
            0.006456355,
            4.929e-06,
            0.006450997,
        ),
    ),
    UnitreeH1WithHandLinkId.LEFT_HAND: (
        "left_hand_link",
        0.014,
        ((0.003993, -9.4e-05, 0.0), (0.0, 0.0, 0.0)),
        (
            3.449e-06,
            6e-09,
            0.0,
            1.917e-06,
            0.0,
            1.932e-06,
        ),
    ),
    UnitreeH1WithHandLinkId.L_HAND_BASE: (
        "L_hand_base_link",
        0.14143,
        ((-0.002551, -0.066047, -0.0019357), (0.0, 0.0, 0.0)),
        (
            0.0001234,
            2.1995e-06,
            -1.7694e-06,
            8.3835e-05,
            1.5968e-06,
            7.7231e-05,
        ),
    ),
    UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL_BASE: (
        "L_thumb_proximal_base",
        0.0018869,
        ((0.0048817, 0.00038782, -0.00722), (0.0, 0.0, 0.0)),
        (
            5.5158e-08,
            -1.1803e-08,
            -4.6743e-09,
            8.2164e-08,
            -1.3521e-09,
            6.7434e-08,
        ),
    ),
    UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL: (
        "L_thumb_proximal",
        0.0066101,
        ((0.021936, -0.01279, -0.0080386), (0.0, 0.0, 0.0)),
        (
            1.5693e-06,
            7.8339e-07,
            8.5959e-10,
            1.7356e-06,
            1.0378e-09,
            2.787e-06,
        ),
    ),
    UnitreeH1WithHandLinkId.L_THUMB_INTERMEDIATE: (
        "L_thumb_intermediate",
        0.0037844,
        ((0.0095531, 0.0016282, -0.0072002), (0.0, 0.0, 0.0)),
        (
            3.6981e-07,
            9.8603e-08,
            -2.8173e-12,
            3.2395e-07,
            -2.8028e-12,
            4.6532e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_THUMB_DISTAL: (
        "L_thumb_distal",
        0.003344,
        ((0.0092888, -0.004953, -0.0060033), (0.0, 0.0, 0.0)),
        (
            1.3632e-07,
            5.6787e-08,
            -9.1939e-11,
            1.4052e-07,
            1.2145e-10,
            2.0026e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_INDEX_PROXIMAL: (
        "L_index_proximal",
        0.0042405,
        ((0.0012971, -0.011934, -0.0059998), (0.0, 0.0, 0.0)),
        (
            6.6215e-07,
            1.8442e-08,
            1.3746e-12,
            2.1167e-07,
            -1.4773e-11,
            6.9402e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_INDEX_INTERMEDIATE: (
        "L_index_intermediate",
        0.0045682,
        ((0.0021753, -0.019567, -0.005), (0.0, 0.0, 0.0)),
        (
            7.6284e-07,
            -8.063e-08,
            3.6797e-13,
            9.4308e-08,
            1.5743e-13,
            7.8176e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_MIDDLE_PROXIMAL: (
        "L_middle_proximal",
        0.0042405,
        ((0.0012971, -0.011934, -0.0059999), (0.0, 0.0, 0.0)),
        (
            6.6215e-07,
            1.8442e-08,
            1.2299e-12,
            2.1167e-07,
            -1.4484e-11,
            6.9402e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_MIDDLE_INTERMEDIATE: (
        "L_middle_intermediate",
        0.0050397,
        ((0.001921, -0.020796, -0.0049999), (0.0, 0.0, 0.0)),
        (
            9.5823e-07,
            -1.1425e-07,
            -2.4186e-12,
            1.0646e-07,
            3.6974e-12,
            9.8385e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_RING_PROXIMAL: (
        "L_ring_proximal",
        0.0042405,
        ((0.0012971, -0.011934, -0.0059999), (0.0, 0.0, 0.0)),
        (
            6.6215e-07,
            1.8442e-08,
            9.6052e-13,
            2.1167e-07,
            -1.4124e-11,
            6.9402e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_RING_INTERMEDIATE: (
        "L_ring_intermediate",
        0.0045682,
        ((0.0021753, -0.019567, -0.005), (0.0, 0.0, 0.0)),
        (
            7.6285e-07,
            -8.0631e-08,
            3.3472e-14,
            9.4308e-08,
            -4.4773e-13,
            7.8176e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_PINKY_PROXIMAL: (
        "L_pinky_proximal",
        0.0042405,
        ((0.0012971, -0.011934, -0.0059999), (0.0, 0.0, 0.0)),
        (
            6.6215e-07,
            1.8442e-08,
            1.0279e-12,
            2.1167e-07,
            -1.4277e-11,
            6.9402e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.L_PINKY_INTERMEDIATE: (
        "L_pinky_intermediate",
        0.0036036,
        ((0.0024788, -0.016208, -0.0050001), (0.0, 0.0, 0.0)),
        (
            4.3923e-07,
            -4.1355e-08,
            1.2263e-12,
            7.0315e-08,
            3.1311e-12,
            4.4881e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_link",
        1.033,
        ((0.005045, -0.053657, -0.015715), (0.0, 0.0, 0.0)),
        (
            0.0012985,
            1.7333e-05,
            8.683e-06,
            0.00087279,
            -3.9656e-05,
            0.00097338,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_link",
        0.793,
        ((0.000679, -0.00115, -0.094076), (0.0, 0.0, 0.0)),
        (
            0.0015742,
            -2.298e-06,
            -7.2265e-05,
            0.0016973,
            6.3691e-05,
            0.0010183,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_link",
        0.839,
        ((0.01365, -0.002767, -0.16266), (0.0, 0.0, 0.0)),
        (
            0.003664,
            1.0671e-05,
            0.00034733,
            0.0040789,
            -7.0213e-05,
            0.00066383,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_ELBOW: (
        "right_elbow_link",
        0.723,
        ((0.164862, -0.000118, -0.015734), (0.0, 0.0, 0.0)),
        (
            0.00049639,
            3.3971e-05,
            0.000316026,
            0.006456355,
            -4.929e-06,
            0.006450997,
        ),
    ),
    UnitreeH1WithHandLinkId.RIGHT_HAND: (
        "right_hand_link",
        0.014,
        ((0.003993, 9.4e-05, 0.0), (0.0, 0.0, 0.0)),
        (
            3.449e-06,
            -6e-09,
            0.0,
            1.917e-06,
            0.0,
            1.932e-06,
        ),
    ),
    UnitreeH1WithHandLinkId.R_HAND_BASE: (
        "R_hand_base_link",
        0.14143,
        ((-0.0025264, -0.066047, 0.0019598), (0.0, 0.0, 0.0)),
        (
            0.00012281,
            2.1711e-06,
            1.7709e-06,
            8.3832e-05,
            -1.6551e-06,
            7.6663e-05,
        ),
    ),
    UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL_BASE: (
        "R_thumb_proximal_base",
        0.0018869,
        ((-0.0048064, 0.0009382, -0.00757), (0.0, 0.0, 0.0)),
        (
            5.816e-08,
            1.4539e-08,
            4.491e-09,
            7.9161e-08,
            -1.8727e-09,
            6.7433e-08,
        ),
    ),
    UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL: (
        "R_thumb_proximal",
        0.0066075,
        ((0.021932, 0.012785, -0.0080386), (0.0, 0.0, 0.0)),
        (
            1.5686e-06,
            -7.8296e-07,
            8.9143e-10,
            1.7353e-06,
            -1.0191e-09,
            2.786e-06,
        ),
    ),
    UnitreeH1WithHandLinkId.R_THUMB_INTERMEDIATE: (
        "R_thumb_intermediate",
        0.0037847,
        ((0.0095544, -0.0016282, -0.0071997), (0.0, 0.0, 0.0)),
        (
            3.6981e-07,
            -9.8581e-08,
            -4.7469e-12,
            3.2394e-07,
            1.0939e-12,
            4.6531e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_THUMB_DISTAL: (
        "R_thumb_distal",
        0.0033441,
        ((0.0092888, 0.0049529, -0.0060033), (0.0, 0.0, 0.0)),
        (
            1.3632e-07,
            -5.6788e-08,
            -9.2764e-11,
            1.4052e-07,
            -1.2283e-10,
            2.0026e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_INDEX_PROXIMAL: (
        "R_index_proximal",
        0.0042403,
        ((0.0012259, 0.011942, -0.0060001), (0.0, 0.0, 0.0)),
        (
            6.6232e-07,
            -1.5775e-08,
            1.8515e-12,
            2.1146e-07,
            -5.0828e-12,
            6.9398e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_INDEX_INTERMEDIATE: (
        "R_index_intermediate",
        0.0045683,
        ((0.0019697, 0.019589, -0.005), (0.0, 0.0, 0.0)),
        (
            7.6111e-07,
            8.7637e-08,
            -3.7751e-13,
            9.6076e-08,
            9.9444e-13,
            7.8179e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_MIDDLE_PROXIMAL: (
        "R_middle_proximal",
        0.0042403,
        ((0.001297, 0.011934, -0.0060001), (0.0, 0.0, 0.0)),
        (
            6.6211e-07,
            -1.8461e-08,
            1.8002e-12,
            2.1167e-07,
            -6.6808e-12,
            6.9397e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_MIDDLE_INTERMEDIATE: (
        "R_middle_intermediate",
        0.0050396,
        ((0.001921, 0.020796, -0.005), (0.0, 0.0, 0.0)),
        (
            9.5822e-07,
            1.1425e-07,
            -2.4791e-12,
            1.0646e-07,
            5.9173e-12,
            9.8384e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_RING_PROXIMAL: (
        "R_ring_proximal",
        0.0042403,
        ((0.001297, 0.011934, -0.0060002), (0.0, 0.0, 0.0)),
        (
            6.6211e-07,
            -1.8461e-08,
            1.5793e-12,
            2.1167e-07,
            -6.6868e-12,
            6.9397e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_RING_INTERMEDIATE: (
        "R_ring_intermediate",
        0.0045683,
        ((0.0021753, 0.019567, -0.005), (0.0, 0.0, 0.0)),
        (
            7.6286e-07,
            8.0635e-08,
            -6.1562e-13,
            9.431e-08,
            5.8619e-13,
            7.8177e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_PINKY_PROXIMAL: (
        "R_pinky_proximal",
        0.0042403,
        ((0.001297, 0.011934, -0.0060001), (0.0, 0.0, 0.0)),
        (
            6.6211e-07,
            -1.8461e-08,
            1.6907e-12,
            2.1167e-07,
            -6.9334e-12,
            6.9397e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.R_PINKY_INTERMEDIATE: (
        "R_pinky_intermediate",
        0.0035996,
        ((0.0024748, 0.016203, -0.0050031), (0.0, 0.0, 0.0)),
        (
            4.3913e-07,
            4.1418e-08,
            3.7168e-11,
            7.0247e-08,
            5.8613e-11,
            4.4867e-07,
        ),
    ),
    UnitreeH1WithHandLinkId.LOGO: (
        "logo_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1WithHandLinkId.D435_LEFT_IMAGER: (
        "d435_left_imager_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1WithHandLinkId.D435_RGB_MODULE: (
        "d435_rgb_module_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1WithHandLinkId.MID360: (
        "mid360_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
}
"""URDF-derived link specifications for the Unitree H1 with Hand robot."""


_JOINT_SPECS: dict[UnitreeH1WithHandJointId, UnitreeH1WithHandJointSpec] = {
    UnitreeH1WithHandJointId.LEFT_HIP_YAW: (
        "left_hip_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.PELVIS,
        UnitreeH1WithHandLinkId.LEFT_HIP_YAW,
        ((0.0, 0.0875, -0.1742), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.LEFT_HIP_ROLL: (
        "left_hip_roll_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_HIP_YAW,
        UnitreeH1WithHandLinkId.LEFT_HIP_ROLL,
        ((0.039468, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.LEFT_HIP_PITCH: (
        "left_hip_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_HIP_ROLL,
        UnitreeH1WithHandLinkId.LEFT_HIP_PITCH,
        ((0.0, 0.11536, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.14, 2.53, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.LEFT_KNEE: (
        "left_knee_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_HIP_PITCH,
        UnitreeH1WithHandLinkId.LEFT_KNEE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.26, 2.05, 300.0, 14.0),
    ),
    UnitreeH1WithHandJointId.LEFT_ANKLE: (
        "left_ankle_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_KNEE,
        UnitreeH1WithHandLinkId.LEFT_ANKLE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.52, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_HIP_YAW: (
        "right_hip_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.PELVIS,
        UnitreeH1WithHandLinkId.RIGHT_HIP_YAW,
        ((0.0, -0.0875, -0.1742), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_HIP_ROLL: (
        "right_hip_roll_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_HIP_YAW,
        UnitreeH1WithHandLinkId.RIGHT_HIP_ROLL,
        ((0.039468, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_HIP_ROLL,
        UnitreeH1WithHandLinkId.RIGHT_HIP_PITCH,
        ((0.0, -0.11536, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.14, 2.53, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_KNEE: (
        "right_knee_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_HIP_PITCH,
        UnitreeH1WithHandLinkId.RIGHT_KNEE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.26, 2.05, 300.0, 14.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_ANKLE: (
        "right_ankle_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_KNEE,
        UnitreeH1WithHandLinkId.RIGHT_ANKLE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.52, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.TORSO: (
        "torso_joint",
        "revolute",
        UnitreeH1WithHandLinkId.PELVIS,
        UnitreeH1WithHandLinkId.TORSO,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.35, 2.35, 200.0, 23.0),
    ),
    UnitreeH1WithHandJointId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_PITCH,
        ((0.0055, 0.15535, 0.42999), (0.43633, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.87, 2.87, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_PITCH,
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_ROLL,
        ((-0.0055, 0.0565, -0.0165), (-0.43633, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.34, 3.11, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_ROLL,
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_YAW,
        ((0.0, 0.0, -0.1343), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.3, 4.45, 18.0, 20.0),
    ),
    UnitreeH1WithHandJointId.LEFT_ELBOW: (
        "left_elbow_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_SHOULDER_YAW,
        UnitreeH1WithHandLinkId.LEFT_ELBOW,
        ((0.0185, 0.0, -0.198), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.25, 2.61, 18.0, 20.0),
    ),
    UnitreeH1WithHandJointId.LEFT_HAND: (
        "left_hand_joint",
        "revolute",
        UnitreeH1WithHandLinkId.LEFT_ELBOW,
        UnitreeH1WithHandLinkId.LEFT_HAND,
        ((0.2605, 0.0, -0.0185), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-3.0543261909900767, 3.0543261909900767, 6.0, 12.0),
    ),
    UnitreeH1WithHandJointId.L_BASE_LINK: (
        "L_base_link_joint",
        "fixed",
        UnitreeH1WithHandLinkId.LEFT_HAND,
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        ((0.003, 0.0, 0.0), (0.0, 0.0, 1.5707963267948966)),
        None,
        None,
    ),
    UnitreeH1WithHandJointId.L_THUMB_PROXIMAL_YAW: (
        "L_thumb_proximal_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL_BASE,
        ((-0.01696, -0.0691, 0.02045), (1.5708, -1.5708, 0.0)),
        (0.0, 0.0, 1.0),
        (-0.1, 1.3, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_THUMB_PROXIMAL_PITCH: (
        "L_thumb_proximal_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL_BASE,
        UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL,
        ((0.0099867, 0.0098242, -0.0089), (-1.5708, 0.0, 0.16939)),
        (0.0, 0.0, -1.0),
        (-0.1, 0.6, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_THUMB_INTERMEDIATE: (
        "L_thumb_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_THUMB_PROXIMAL,
        UnitreeH1WithHandLinkId.L_THUMB_INTERMEDIATE,
        ((0.04407, -0.034553, -0.0008), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 0.8, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_THUMB_DISTAL: (
        "L_thumb_distal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_THUMB_INTERMEDIATE,
        UnitreeH1WithHandLinkId.L_THUMB_DISTAL,
        ((0.020248, -0.010156, -0.0012), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.2, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_INDEX_PROXIMAL: (
        "L_index_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        UnitreeH1WithHandLinkId.L_INDEX_PROXIMAL,
        ((0.00028533, -0.13653, 0.032268), (-0.034907, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_INDEX_INTERMEDIATE: (
        "L_index_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_INDEX_PROXIMAL,
        UnitreeH1WithHandLinkId.L_INDEX_INTERMEDIATE,
        ((-0.0024229, -0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_MIDDLE_PROXIMAL: (
        "L_middle_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        UnitreeH1WithHandLinkId.L_MIDDLE_PROXIMAL,
        ((0.00028533, -0.1371, 0.01295), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_MIDDLE_INTERMEDIATE: (
        "L_middle_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_MIDDLE_PROXIMAL,
        UnitreeH1WithHandLinkId.L_MIDDLE_INTERMEDIATE,
        ((-0.0024229, -0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_RING_PROXIMAL: (
        "L_ring_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        UnitreeH1WithHandLinkId.L_RING_PROXIMAL,
        ((0.00028533, -0.13691, -0.0062872), (0.05236, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_RING_INTERMEDIATE: (
        "L_ring_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_RING_PROXIMAL,
        UnitreeH1WithHandLinkId.L_RING_INTERMEDIATE,
        ((-0.0024229, -0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_PINKY_PROXIMAL: (
        "L_pinky_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_HAND_BASE,
        UnitreeH1WithHandLinkId.L_PINKY_PROXIMAL,
        ((0.00028533, -0.13571, -0.025488), (0.10472, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.L_PINKY_INTERMEDIATE: (
        "L_pinky_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.L_PINKY_PROXIMAL,
        UnitreeH1WithHandLinkId.L_PINKY_INTERMEDIATE,
        ((-0.0024229, -0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_PITCH,
        ((0.0055, -0.15535, 0.42999), (-0.43633, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.87, 2.87, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_PITCH,
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_ROLL,
        ((-0.0055, -0.0565, -0.0165), (0.43633, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-3.11, 0.34, 40.0, 9.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_ROLL,
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_YAW,
        ((0.0, 0.0, -0.1343), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-4.45, 1.3, 18.0, 20.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_ELBOW: (
        "right_elbow_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_SHOULDER_YAW,
        UnitreeH1WithHandLinkId.RIGHT_ELBOW,
        ((0.0185, 0.0, -0.198), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.25, 2.61, 18.0, 20.0),
    ),
    UnitreeH1WithHandJointId.RIGHT_HAND: (
        "right_hand_joint",
        "revolute",
        UnitreeH1WithHandLinkId.RIGHT_ELBOW,
        UnitreeH1WithHandLinkId.RIGHT_HAND,
        ((0.2605, 0.0, -0.0185), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-3.0543261909900767, 3.0543261909900767, 6.0, 12.0),
    ),
    UnitreeH1WithHandJointId.R_BASE_LINK: (
        "R_base_link_joint",
        "fixed",
        UnitreeH1WithHandLinkId.RIGHT_HAND,
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        ((0.003, 0.0, 0.0), (3.141592653589793, 0.0, -1.5707963267948966)),
        None,
        None,
    ),
    UnitreeH1WithHandJointId.R_THUMB_PROXIMAL_YAW: (
        "R_thumb_proximal_yaw_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL_BASE,
        ((-0.01696, -0.0691, -0.02045), (1.5708, -1.5708, 0.0)),
        (0.0, 0.0, -1.0),
        (-0.1, 1.3, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_THUMB_PROXIMAL_PITCH: (
        "R_thumb_proximal_pitch_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL_BASE,
        UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL,
        ((-0.0088099, 0.010892, -0.00925), (1.5708, 0.0, 2.8587)),
        (0.0, 0.0, 1.0),
        (-0.1, 0.6, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_THUMB_INTERMEDIATE: (
        "R_thumb_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_THUMB_PROXIMAL,
        UnitreeH1WithHandLinkId.R_THUMB_INTERMEDIATE,
        ((0.04407, 0.034553, -0.0008), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 0.8, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_THUMB_DISTAL: (
        "R_thumb_distal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_THUMB_INTERMEDIATE,
        UnitreeH1WithHandLinkId.R_THUMB_DISTAL,
        ((0.020248, 0.010156, -0.0012), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.2, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_INDEX_PROXIMAL: (
        "R_index_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        UnitreeH1WithHandLinkId.R_INDEX_PROXIMAL,
        ((0.00028533, -0.13653, -0.032268), (-3.1067, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_INDEX_INTERMEDIATE: (
        "R_index_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_INDEX_PROXIMAL,
        UnitreeH1WithHandLinkId.R_INDEX_INTERMEDIATE,
        ((-0.0026138, 0.032026, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_MIDDLE_PROXIMAL: (
        "R_middle_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        UnitreeH1WithHandLinkId.R_MIDDLE_PROXIMAL,
        ((0.00028533, -0.1371, -0.01295), (-3.1416, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_MIDDLE_INTERMEDIATE: (
        "R_middle_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_MIDDLE_PROXIMAL,
        UnitreeH1WithHandLinkId.R_MIDDLE_INTERMEDIATE,
        ((-0.0024229, 0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_RING_PROXIMAL: (
        "R_ring_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        UnitreeH1WithHandLinkId.R_RING_PROXIMAL,
        ((0.00028533, -0.13691, 0.0062872), (3.0892, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_RING_INTERMEDIATE: (
        "R_ring_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_RING_PROXIMAL,
        UnitreeH1WithHandLinkId.R_RING_INTERMEDIATE,
        ((-0.0024229, 0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_PINKY_PROXIMAL: (
        "R_pinky_proximal_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_HAND_BASE,
        UnitreeH1WithHandLinkId.R_PINKY_PROXIMAL,
        ((0.00028533, -0.13571, 0.025488), (3.0369, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.R_PINKY_INTERMEDIATE: (
        "R_pinky_intermediate_joint",
        "revolute",
        UnitreeH1WithHandLinkId.R_PINKY_PROXIMAL,
        UnitreeH1WithHandLinkId.R_PINKY_INTERMEDIATE,
        ((-0.0024229, 0.032041, -0.001), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 1.7, 1.0, 0.5),
    ),
    UnitreeH1WithHandJointId.LOGO: (
        "logo_joint",
        "fixed",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.LOGO,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1WithHandJointId.D435_LEFT_IMAGER: (
        "d435_left_imager_joint",
        "fixed",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.D435_LEFT_IMAGER,
        ((0.10848474394, 0.0175, 0.69317107367), (-2.45735, 0.0, -1.5708)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1WithHandJointId.D435_RGB_MODULE: (
        "d435_rgb_module_joint",
        "fixed",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.D435_RGB_MODULE,
        ((0.10848474394, 0.0325, 0.69317107367), (-2.45735, 0.0, -1.5708)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1WithHandJointId.MID360: (
        "mid360_joint",
        "fixed",
        UnitreeH1WithHandLinkId.TORSO,
        UnitreeH1WithHandLinkId.MID360,
        ((0.0472999018, 0.0, 0.67492878653), (0.0, 0.243124, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
}
"""URDF-derived joint specifications for the Unitree H1 with Hand robot."""


UNITREE_H1_WITH_HAND_LINKAGE = Linkage[UnitreeH1WithHandLinkId](
    links={
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    },
)
"""The linkage for the Unitree H1 with Hand robot."""

UNITREE_H1_WITH_HAND_ARTICULATION = Articulation[
    UnitreeH1WithHandLinkId, UnitreeH1WithHandJointId
](
    joints={
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    },
)
"""The articulation for the Unitree H1 with Hand robot."""

UNITREE_H1_WITH_HAND = Skeleton[UnitreeH1WithHandLinkId, UnitreeH1WithHandJointId](
    linkage=UNITREE_H1_WITH_HAND_LINKAGE,
    articulation=UNITREE_H1_WITH_HAND_ARTICULATION,
)
"""The kinematic chain for the Unitree H1 with Hand robot."""
