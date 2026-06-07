from __future__ import annotations

from urdf.kinematics import (
    Articulation,
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


class BoosterT1SerialLinkId(LinkId):
    """Link identifiers for the Booster T1 Serial robot."""

    TRUNK: str = "Trunk"
    """Link with ID Trunk."""

    H1: str = "H1"
    """Link with ID H1."""

    H2: str = "H2"
    """Link with ID H2."""

    AL1: str = "AL1"
    """Link with ID AL1."""

    AL2: str = "AL2"
    """Link with ID AL2."""

    AL3: str = "AL3"
    """Link with ID AL3."""

    LEFT_HAND: str = "left_hand_link"
    """Link with ID left_hand_link."""

    AR1: str = "AR1"
    """Link with ID AR1."""

    AR2: str = "AR2"
    """Link with ID AR2."""

    AR3: str = "AR3"
    """Link with ID AR3."""

    RIGHT_HAND: str = "right_hand_link"
    """Link with ID right_hand_link."""

    WAIST: str = "Waist"
    """Link with ID Waist."""

    HIP_PITCH_LEFT: str = "Hip_Pitch_Left"
    """Link with ID Hip_Pitch_Left."""

    HIP_ROLL_LEFT: str = "Hip_Roll_Left"
    """Link with ID Hip_Roll_Left."""

    HIP_YAW_LEFT: str = "Hip_Yaw_Left"
    """Link with ID Hip_Yaw_Left."""

    SHANK_LEFT: str = "Shank_Left"
    """Link with ID Shank_Left."""

    ANKLE_CROSS_LEFT: str = "Ankle_Cross_Left"
    """Link with ID Ankle_Cross_Left."""

    LEFT_FOOT: str = "left_foot_link"
    """Link with ID left_foot_link."""

    HIP_PITCH_RIGHT: str = "Hip_Pitch_Right"
    """Link with ID Hip_Pitch_Right."""

    HIP_ROLL_RIGHT: str = "Hip_Roll_Right"
    """Link with ID Hip_Roll_Right."""

    HIP_YAW_RIGHT: str = "Hip_Yaw_Right"
    """Link with ID Hip_Yaw_Right."""

    SHANK_RIGHT: str = "Shank_Right"
    """Link with ID Shank_Right."""

    ANKLE_CROSS_RIGHT: str = "Ankle_Cross_Right"
    """Link with ID Ankle_Cross_Right."""

    RIGHT_FOOT: str = "right_foot_link"
    """Link with ID right_foot_link."""


class BoosterT1SerialJointId(JointId):
    """Joint identifiers for the Booster T1 Serial robot."""

    AAHEAD_YAW: str = "AAHead_yaw"
    """Joint with ID AAHead_yaw."""

    HEAD_PITCH: str = "Head_pitch"
    """Joint with ID Head_pitch."""

    LEFT_SHOULDER_PITCH: str = "Left_Shoulder_Pitch"
    """The left shoulder pitch joint."""

    LEFT_SHOULDER_ROLL: str = "Left_Shoulder_Roll"
    """The left shoulder roll joint."""

    LEFT_ELBOW_PITCH: str = "Left_Elbow_Pitch"
    """Joint with ID Left_Elbow_Pitch."""

    LEFT_ELBOW_YAW: str = "Left_Elbow_Yaw"
    """The left elbow joint."""

    RIGHT_SHOULDER_PITCH: str = "Right_Shoulder_Pitch"
    """The right shoulder pitch joint."""

    RIGHT_SHOULDER_ROLL: str = "Right_Shoulder_Roll"
    """The right shoulder roll joint."""

    RIGHT_ELBOW_PITCH: str = "Right_Elbow_Pitch"
    """Joint with ID Right_Elbow_Pitch."""

    RIGHT_ELBOW_YAW: str = "Right_Elbow_Yaw"
    """The right elbow joint."""

    WAIST: str = "Waist"
    """Joint with ID Waist."""

    LEFT_HIP_PITCH: str = "Left_Hip_Pitch"
    """The left hip pitch joint."""

    LEFT_HIP_ROLL: str = "Left_Hip_Roll"
    """The left hip roll joint."""

    LEFT_HIP_YAW: str = "Left_Hip_Yaw"
    """The left hip yaw joint."""

    LEFT_KNEE_PITCH: str = "Left_Knee_Pitch"
    """The left ankle pitch joint."""

    LEFT_ANKLE_PITCH: str = "Left_Ankle_Pitch"
    """The left ankle pitch joint."""

    LEFT_ANKLE_ROLL: str = "Left_Ankle_Roll"
    """The left ankle roll joint."""

    RIGHT_HIP_PITCH: str = "Right_Hip_Pitch"
    """The right hip pitch joint."""

    RIGHT_HIP_ROLL: str = "Right_Hip_Roll"
    """The right hip roll joint."""

    RIGHT_HIP_YAW: str = "Right_Hip_Yaw"
    """The right hip yaw joint."""

    RIGHT_KNEE_PITCH: str = "Right_Knee_Pitch"
    """The right ankle pitch joint."""

    RIGHT_ANKLE_PITCH: str = "Right_Ankle_Pitch"
    """The right ankle pitch joint."""

    RIGHT_ANKLE_ROLL: str = "Right_Ankle_Roll"
    """The right ankle roll joint."""


type BoosterT1SerialLink = Link[BoosterT1SerialLinkId]
"""A link in the Booster T1 Serial robot."""

type BoosterT1SerialJoint = RevoluteJoint[BoosterT1SerialLinkId, BoosterT1SerialJointId]
"""A joint in the Booster T1 Serial robot."""

type BoosterT1SerialJointSpec = JointSpec[BoosterT1SerialLinkId]
"""URDF-derived data for a joint in the Booster T1 Serial robot."""


_LINK_SPECS: dict[BoosterT1SerialLinkId, LinkSpec] = {
    BoosterT1SerialLinkId.TRUNK: (
        "Trunk",
        11.7,
        (
            (0.0551365401093076, -1.42058017623659e-06, 0.105062332707657),
            (0.0, 0.0, 0.0),
        ),
        (
            0.0915287235057927,
            -4.25369739206781e-07,
            0.000646360369011163,
            0.076778716903413,
            5.82340020271393e-07,
            0.0556171053368987,
        ),
    ),
    BoosterT1SerialLinkId.H1: (
        "H1",
        0.44391,
        ((-0.000508, -0.001403, 0.057432), (0.0, 0.0, 0.0)),
        (
            0.000224,
            3e-06,
            1e-06,
            0.000241,
            -2e-06,
            0.00015,
        ),
    ),
    BoosterT1SerialLinkId.H2: (
        "H2",
        0.631019,
        ((0.007802, 0.001262, 0.098631), (0.0, 0.0, 0.0)),
        (
            0.002025,
            -2.5e-05,
            4.6e-05,
            0.00192,
            3.6e-05,
            0.001739,
        ),
    ),
    BoosterT1SerialLinkId.AL1: (
        "AL1",
        0.53,
        ((-0.000677, 0.044974, 0.0), (0.0, 0.0, 0.0)),
        (
            0.001293,
            -1.7e-05,
            0.0,
            0.000293,
            0.0,
            0.001367,
        ),
    ),
    BoosterT1SerialLinkId.AL2: (
        "AL2",
        0.16,
        ((0.003862, 0.037976, 0.0), (0.0, 0.0, 0.0)),
        (
            0.000345,
            8e-06,
            0.0,
            0.000177,
            0.0,
            0.000401,
        ),
    ),
    BoosterT1SerialLinkId.AL3: (
        "AL3",
        1.02,
        ((0.0, 0.085353, -9.9e-05), (0.0, 0.0, 0.0)),
        (
            0.012869,
            0.0,
            0.0,
            0.000621,
            -2.4e-05,
            0.012798,
        ),
    ),
    BoosterT1SerialLinkId.LEFT_HAND: (
        "left_hand_link",
        0.327214390850251,
        ((-0.000108, 0.109573, 0.000591), (0.0, 0.0, 0.0)),
        (
            0.008159,
            -3e-06,
            0.0,
            0.000215,
            1.7e-05,
            0.008131,
        ),
    ),
    BoosterT1SerialLinkId.AR1: (
        "AR1",
        0.53,
        ((-0.000677, -0.044974, 0.0), (0.0, 0.0, 0.0)),
        (
            0.001293,
            -1.7e-05,
            0.0,
            0.000293,
            0.0,
            0.001367,
        ),
    ),
    BoosterT1SerialLinkId.AR2: (
        "AR2",
        0.16,
        ((0.003862, -0.037976, 0.0), (0.0, 0.0, 0.0)),
        (
            0.000345,
            -8e-06,
            0.0,
            0.000177,
            0.0,
            0.000401,
        ),
    ),
    BoosterT1SerialLinkId.AR3: (
        "AR3",
        1.02,
        ((0.0, -0.085353, -9.9e-05), (0.0, 0.0, 0.0)),
        (
            0.012869,
            0.0,
            0.0,
            0.000621,
            2.4e-05,
            0.012798,
        ),
    ),
    BoosterT1SerialLinkId.RIGHT_HAND: (
        "right_hand_link",
        0.327214390850251,
        ((-0.000108, -0.109573, 0.000591), (0.0, 0.0, 0.0)),
        (
            0.008159,
            3e-06,
            0.0,
            0.000215,
            -1.7e-05,
            0.008131,
        ),
    ),
    BoosterT1SerialLinkId.WAIST: (
        "Waist",
        2.581,
        ((0.002284, 3e-06, 0.007301), (0.0, 0.0, 0.0)),
        (
            0.005289,
            0.0,
            0.000207,
            0.005299,
            1e-06,
            0.004821,
        ),
    ),
    BoosterT1SerialLinkId.HIP_PITCH_LEFT: (
        "Hip_Pitch_Left",
        1.021,
        ((0.000534, -0.007296, -0.018083), (0.0, 0.0, 0.0)),
        (
            0.001805,
            6e-06,
            -1.5e-05,
            0.001421,
            8e-05,
            0.001292,
        ),
    ),
    BoosterT1SerialLinkId.HIP_ROLL_LEFT: (
        "Hip_Roll_Left",
        0.385,
        ((0.001101, 2.4e-05, -0.05375), (0.0, 0.0, 0.0)),
        (
            0.001517,
            0.0,
            1.7e-05,
            0.001743,
            0.0,
            0.000515,
        ),
    ),
    BoosterT1SerialLinkId.HIP_YAW_LEFT: (
        "Hip_Yaw_Left",
        2.166,
        ((-0.007233, 0.000206, -0.089184), (0.0, 0.0, 0.0)),
        (
            0.025108,
            -7e-06,
            0.002094,
            0.025733,
            -5e-05,
            0.002787,
        ),
    ),
    BoosterT1SerialLinkId.SHANK_LEFT: (
        "Shank_Left",
        1.73,
        ((-0.006012, 0.000259, -0.124318), (0.0, 0.0, 0.0)),
        (
            0.034618,
            1.1e-05,
            0.001561,
            0.034539,
            0.000197,
            0.001934,
        ),
    ),
    BoosterT1SerialLinkId.ANKLE_CROSS_LEFT: (
        "Ankle_Cross_Left",
        0.073,
        ((-0.003722, 0.0, -0.007981), (0.0, 0.0, 0.0)),
        (
            1.2e-05,
            0.0,
            3e-06,
            2.9e-05,
            0.0,
            2.5e-05,
        ),
    ),
    BoosterT1SerialLinkId.LEFT_FOOT: (
        "left_foot_link",
        0.685,
        ((-0.000249, 0.0, -0.00914), (0.0, 0.0, 0.0)),
        (
            0.002214,
            0.0,
            -0.000114,
            0.002385,
            0.0,
            0.002671,
        ),
    ),
    BoosterT1SerialLinkId.HIP_PITCH_RIGHT: (
        "Hip_Pitch_Right",
        1.021,
        ((0.000534, 0.007514, -0.018082), (0.0, 0.0, 0.0)),
        (
            0.001805,
            -8e-06,
            -1.5e-05,
            0.001421,
            -8.5e-05,
            0.001292,
        ),
    ),
    BoosterT1SerialLinkId.HIP_ROLL_RIGHT: (
        "Hip_Roll_Right",
        0.385,
        ((0.001099, 2.4e-05, -0.053748), (0.0, 0.0, 0.0)),
        (
            0.001517,
            0.0,
            1.7e-05,
            0.001743,
            0.0,
            0.000515,
        ),
    ),
    BoosterT1SerialLinkId.HIP_YAW_RIGHT: (
        "Hip_Yaw_Right",
        2.17,
        ((-0.007191, -0.000149, -0.08922), (0.0, 0.0, 0.0)),
        (
            0.025137,
            6e-06,
            0.002086,
            0.025762,
            4.4e-05,
            0.002787,
        ),
    ),
    BoosterT1SerialLinkId.SHANK_RIGHT: (
        "Shank_Right",
        1.79,
        ((-0.005741, -0.000541, -0.122602), (0.0, 0.0, 0.0)),
        (
            0.035098,
            -9e-06,
            0.001554,
            0.034958,
            -8.6e-05,
            0.002039,
        ),
    ),
    BoosterT1SerialLinkId.ANKLE_CROSS_RIGHT: (
        "Ankle_Cross_Right",
        0.073,
        ((-0.003722, 0.0, -0.007981), (0.0, 0.0, 0.0)),
        (
            1.2e-05,
            0.0,
            3e-06,
            2.9e-05,
            0.0,
            2.5e-05,
        ),
    ),
    BoosterT1SerialLinkId.RIGHT_FOOT: (
        "right_foot_link",
        0.685,
        ((-0.000248, 0.0, -0.00914), (0.0, 0.0, 0.0)),
        (
            0.002214,
            0.0,
            -0.000114,
            0.002385,
            0.0,
            0.002671,
        ),
    ),
}
"""URDF-derived link specifications for the Booster T1 Serial robot."""


_JOINT_SPECS: dict[BoosterT1SerialJointId, BoosterT1SerialJointSpec] = {
    BoosterT1SerialJointId.AAHEAD_YAW: (
        "AAHead_yaw",
        "revolute",
        BoosterT1SerialLinkId.TRUNK,
        BoosterT1SerialLinkId.H1,
        ((0.0625, 0.0, 0.243), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.57, 1.57, 7.0, 12.56),
    ),
    BoosterT1SerialJointId.HEAD_PITCH: (
        "Head_pitch",
        "revolute",
        BoosterT1SerialLinkId.H1,
        BoosterT1SerialLinkId.H2,
        ((0.0, 0.0, 0.06185), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.35, 1.22, 7.0, 12.56),
    ),
    BoosterT1SerialJointId.LEFT_SHOULDER_PITCH: (
        "Left_Shoulder_Pitch",
        "revolute",
        BoosterT1SerialLinkId.TRUNK,
        BoosterT1SerialLinkId.AL1,
        ((0.0575, 0.1063, 0.219), (0.0, 0.00088113, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.31, 1.22, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.LEFT_SHOULDER_ROLL: (
        "Left_Shoulder_Roll",
        "revolute",
        BoosterT1SerialLinkId.AL1,
        BoosterT1SerialLinkId.AL2,
        ((0.0, 0.047, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.74, 1.57, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.LEFT_ELBOW_PITCH: (
        "Left_Elbow_Pitch",
        "revolute",
        BoosterT1SerialLinkId.AL2,
        BoosterT1SerialLinkId.AL3,
        ((0.00025, 0.0605, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.27, 2.27, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.LEFT_ELBOW_YAW: (
        "Left_Elbow_Yaw",
        "revolute",
        BoosterT1SerialLinkId.AL3,
        BoosterT1SerialLinkId.LEFT_HAND,
        ((0.0, 0.1471, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.44, 0.0, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.RIGHT_SHOULDER_PITCH: (
        "Right_Shoulder_Pitch",
        "revolute",
        BoosterT1SerialLinkId.TRUNK,
        BoosterT1SerialLinkId.AR1,
        ((0.0575, -0.1063, 0.219), (0.0, 0.00088113, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.31, 1.22, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.RIGHT_SHOULDER_ROLL: (
        "Right_Shoulder_Roll",
        "revolute",
        BoosterT1SerialLinkId.AR1,
        BoosterT1SerialLinkId.AR2,
        ((0.0, -0.047, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.57, 1.74, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.RIGHT_ELBOW_PITCH: (
        "Right_Elbow_Pitch",
        "revolute",
        BoosterT1SerialLinkId.AR2,
        BoosterT1SerialLinkId.AR3,
        ((0.00025, -0.0605, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.27, 2.27, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.RIGHT_ELBOW_YAW: (
        "Right_Elbow_Yaw",
        "revolute",
        BoosterT1SerialLinkId.AR3,
        BoosterT1SerialLinkId.RIGHT_HAND,
        ((0.0, -0.1471, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (0.0, 2.44, 18.0, 18.84),
    ),
    BoosterT1SerialJointId.WAIST: (
        "Waist",
        "revolute",
        BoosterT1SerialLinkId.TRUNK,
        BoosterT1SerialLinkId.WAIST,
        ((0.0625, 0.0, -0.1155), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.57, 1.57, 30.0, 10.88),
    ),
    BoosterT1SerialJointId.LEFT_HIP_PITCH: (
        "Left_Hip_Pitch",
        "revolute",
        BoosterT1SerialLinkId.WAIST,
        BoosterT1SerialLinkId.HIP_PITCH_LEFT,
        ((0.0, 0.106, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.8, 1.57, 45.0, 12.5),
    ),
    BoosterT1SerialJointId.LEFT_HIP_ROLL: (
        "Left_Hip_Roll",
        "revolute",
        BoosterT1SerialLinkId.HIP_PITCH_LEFT,
        BoosterT1SerialLinkId.HIP_ROLL_LEFT,
        ((0.0, 0.0, -0.02), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.2, 1.57, 30.0, 10.9),
    ),
    BoosterT1SerialJointId.LEFT_HIP_YAW: (
        "Left_Hip_Yaw",
        "revolute",
        BoosterT1SerialLinkId.HIP_ROLL_LEFT,
        BoosterT1SerialLinkId.HIP_YAW_LEFT,
        ((0.0, 0.0, -0.081854), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.0, 1.0, 30.0, 10.9),
    ),
    BoosterT1SerialJointId.LEFT_KNEE_PITCH: (
        "Left_Knee_Pitch",
        "revolute",
        BoosterT1SerialLinkId.HIP_YAW_LEFT,
        BoosterT1SerialLinkId.SHANK_LEFT,
        ((-0.014, 0.0, -0.134), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (0.0, 2.34, 60.0, 11.7),
    ),
    BoosterT1SerialJointId.LEFT_ANKLE_PITCH: (
        "Left_Ankle_Pitch",
        "revolute",
        BoosterT1SerialLinkId.SHANK_LEFT,
        BoosterT1SerialLinkId.ANKLE_CROSS_LEFT,
        ((0.0, 0.0, -0.28), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.35, 20.0, 18.8),
    ),
    BoosterT1SerialJointId.LEFT_ANKLE_ROLL: (
        "Left_Ankle_Roll",
        "revolute",
        BoosterT1SerialLinkId.ANKLE_CROSS_LEFT,
        BoosterT1SerialLinkId.LEFT_FOOT,
        ((0.0, 0.00025, -0.012), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.44, 0.44, 15.0, 12.4),
    ),
    BoosterT1SerialJointId.RIGHT_HIP_PITCH: (
        "Right_Hip_Pitch",
        "revolute",
        BoosterT1SerialLinkId.WAIST,
        BoosterT1SerialLinkId.HIP_PITCH_RIGHT,
        ((0.0, -0.106, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.8, 1.57, 45.0, 12.5),
    ),
    BoosterT1SerialJointId.RIGHT_HIP_ROLL: (
        "Right_Hip_Roll",
        "revolute",
        BoosterT1SerialLinkId.HIP_PITCH_RIGHT,
        BoosterT1SerialLinkId.HIP_ROLL_RIGHT,
        ((0.0, 0.0, -0.02), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.57, 0.2, 30.0, 10.9),
    ),
    BoosterT1SerialJointId.RIGHT_HIP_YAW: (
        "Right_Hip_Yaw",
        "revolute",
        BoosterT1SerialLinkId.HIP_ROLL_RIGHT,
        BoosterT1SerialLinkId.HIP_YAW_RIGHT,
        ((0.0, 0.0, -0.081854), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.0, 1.0, 30.0, 10.9),
    ),
    BoosterT1SerialJointId.RIGHT_KNEE_PITCH: (
        "Right_Knee_Pitch",
        "revolute",
        BoosterT1SerialLinkId.HIP_YAW_RIGHT,
        BoosterT1SerialLinkId.SHANK_RIGHT,
        ((-0.014, 0.0, -0.134), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (0.0, 2.34, 60.0, 11.7),
    ),
    BoosterT1SerialJointId.RIGHT_ANKLE_PITCH: (
        "Right_Ankle_Pitch",
        "revolute",
        BoosterT1SerialLinkId.SHANK_RIGHT,
        BoosterT1SerialLinkId.ANKLE_CROSS_RIGHT,
        ((0.0, 0.0, -0.28), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.35, 20.0, 18.8),
    ),
    BoosterT1SerialJointId.RIGHT_ANKLE_ROLL: (
        "Right_Ankle_Roll",
        "revolute",
        BoosterT1SerialLinkId.ANKLE_CROSS_RIGHT,
        BoosterT1SerialLinkId.RIGHT_FOOT,
        ((0.0, -0.00025, -0.012), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.44, 0.44, 15.0, 12.4),
    ),
}
"""URDF-derived joint specifications for the Booster T1 Serial robot."""


BOOSTER_T1_SERIAL_LINKAGE = Linkage[BoosterT1SerialLinkId](
    links={
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    },
)
"""The linkage for the Booster T1 Serial robot."""

BOOSTER_T1_SERIAL_ARTICULATION = Articulation[
    BoosterT1SerialLinkId, BoosterT1SerialJointId
](
    joints={
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    },
)
"""The articulation for the Booster T1 Serial robot."""

BOOSTER_T1_SERIAL = Skeleton[BoosterT1SerialLinkId, BoosterT1SerialJointId](
    linkage=BOOSTER_T1_SERIAL_LINKAGE,
    articulation=BOOSTER_T1_SERIAL_ARTICULATION,
)
"""The kinematic chain for the Booster T1 Serial robot."""
