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


class UnitreeG1_23DOFLinkId(LinkId):
    """Link identifiers for the Unitree G1 23-DOF robot."""

    PELVIS: str = "pelvis"
    """The pelvis link."""

    PELVIS_CONTOUR: str = "pelvis_contour_link"
    """The pelvis contour link."""

    LEFT_HIP_PITCH: str = "left_hip_pitch_link"
    """The left hip pitch link."""

    LEFT_HIP_ROLL: str = "left_hip_roll_link"
    """The left hip roll link."""

    LEFT_HIP_YAW: str = "left_hip_yaw_link"
    """The left hip yaw link."""

    LEFT_KNEE: str = "left_knee_link"
    """The left knee link."""

    LEFT_ANKLE_PITCH: str = "left_ankle_pitch_link"
    """The left ankle pitch link."""

    LEFT_ANKLE_ROLL: str = "left_ankle_roll_link"
    """The left ankle roll link."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch_link"
    """The right hip pitch link."""

    RIGHT_HIP_ROLL: str = "right_hip_roll_link"
    """The right hip roll link."""

    RIGHT_HIP_YAW: str = "right_hip_yaw_link"
    """The right hip yaw link."""

    RIGHT_KNEE: str = "right_knee_link"
    """The right knee link."""

    RIGHT_ANKLE_PITCH: str = "right_ankle_pitch_link"
    """The right ankle pitch link."""

    RIGHT_ANKLE_ROLL: str = "right_ankle_roll_link"
    """The right ankle roll link."""

    WAIST_YAW_FIXED: str = "waist_yaw_fixed_link"
    """The waist yaw fixed link."""

    TORSO: str = "torso_link"
    """The torso link."""

    LOGO: str = "logo_link"
    """The logo link."""

    HEAD: str = "head_link"
    """The head link."""

    WAIST_SUPPORT: str = "waist_support_link"
    """The waist support link."""

    IMU_IN_TORSO: str = "imu_in_torso"
    """The imu in torso link."""

    IMU_IN_PELVIS: str = "imu_in_pelvis"
    """The imu in pelvis link."""

    D435: str = "d435_link"
    """The d435 link."""

    MID360: str = "mid360_link"
    """The mid360 link."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch_link"
    """The left shoulder pitch link."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll_link"
    """The left shoulder roll link."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw_link"
    """The left shoulder yaw link."""

    LEFT_ELBOW: str = "left_elbow_link"
    """The left elbow link."""

    LEFT_WRIST_ROLL_RUBBER_HAND: str = "left_wrist_roll_rubber_hand"
    """The left wrist roll rubber hand link."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_link"
    """The right shoulder pitch link."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_link"
    """The right shoulder roll link."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_link"
    """The right shoulder yaw link."""

    RIGHT_ELBOW: str = "right_elbow_link"
    """The right elbow link."""

    RIGHT_WRIST_ROLL_RUBBER_HAND: str = "right_wrist_roll_rubber_hand"
    """The right wrist roll rubber hand link."""


class UnitreeG1_23DOFJointId(JointId):
    """Joint identifiers for the Unitree G1 23-DOF robot."""

    PELVIS_CONTOUR: str = "pelvis_contour_joint"
    """The pelvis contour joint."""

    LEFT_HIP_PITCH: str = "left_hip_pitch_joint"
    """The left hip pitch joint."""

    LEFT_HIP_ROLL: str = "left_hip_roll_joint"
    """The left hip roll joint."""

    LEFT_HIP_YAW: str = "left_hip_yaw_joint"
    """The left hip yaw joint."""

    LEFT_KNEE: str = "left_knee_joint"
    """The left knee joint."""

    LEFT_ANKLE_PITCH: str = "left_ankle_pitch_joint"
    """The left ankle pitch joint."""

    LEFT_ANKLE_ROLL: str = "left_ankle_roll_joint"
    """The left ankle roll joint."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch_joint"
    """The right hip pitch joint."""

    RIGHT_HIP_ROLL: str = "right_hip_roll_joint"
    """The right hip roll joint."""

    RIGHT_HIP_YAW: str = "right_hip_yaw_joint"
    """The right hip yaw joint."""

    RIGHT_KNEE: str = "right_knee_joint"
    """The right knee joint."""

    RIGHT_ANKLE_PITCH: str = "right_ankle_pitch_joint"
    """The right ankle pitch joint."""

    RIGHT_ANKLE_ROLL: str = "right_ankle_roll_joint"
    """The right ankle roll joint."""

    WAIST_YAW_FIXED: str = "waist_yaw_fixed_joint"
    """The waist yaw fixed joint."""

    WAIST_YAW: str = "waist_yaw_joint"
    """The waist yaw joint."""

    LOGO: str = "logo_joint"
    """The logo joint."""

    HEAD: str = "head_joint"
    """The head joint."""

    WAIST_SUPPORT: str = "waist_support_joint"
    """The waist support joint."""

    IMU_IN_TORSO: str = "imu_in_torso_joint"
    """The imu in torso joint."""

    IMU_IN_PELVIS: str = "imu_in_pelvis_joint"
    """The imu in pelvis joint."""

    D435: str = "d435_joint"
    """The d435 joint."""

    MID360: str = "mid360_joint"
    """The mid360 joint."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch_joint"
    """The left shoulder pitch joint."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll_joint"
    """The left shoulder roll joint."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw_joint"
    """The left shoulder yaw joint."""

    LEFT_ELBOW: str = "left_elbow_joint"
    """The left elbow joint."""

    LEFT_WRIST_ROLL: str = "left_wrist_roll_joint"
    """The left wrist roll joint."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_joint"
    """The right shoulder pitch joint."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_joint"
    """The right shoulder roll joint."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_joint"
    """The right shoulder yaw joint."""

    RIGHT_ELBOW: str = "right_elbow_joint"
    """The right elbow joint."""

    RIGHT_WRIST_ROLL: str = "right_wrist_roll_joint"
    """The right wrist roll joint."""


type UnitreeG1_23DOFLink = Link[UnitreeG1_23DOFLinkId]
"""A link in the Unitree G1 23-DOF robot."""

type UnitreeG1_23DOFJoint = (
    FixedJoint[UnitreeG1_23DOFLinkId, UnitreeG1_23DOFJointId]
    | RevoluteJoint[UnitreeG1_23DOFLinkId, UnitreeG1_23DOFJointId]
)
"""A joint in the Unitree G1 23-DOF robot."""

type UnitreeG1_23DOFJointSpec = JointSpec[UnitreeG1_23DOFLinkId]
"""URDF-derived data for a joint in the Unitree G1 23-DOF robot."""


_LINK_SPECS: dict[UnitreeG1_23DOFLinkId, LinkSpec] = {
    UnitreeG1_23DOFLinkId.PELVIS: (
        "pelvis",
        3.813,
        ((0.0, 0.0, -0.07605), (0.0, 0.0, 0.0)),
        (
            0.010549,
            0.0,
            2.1e-06,
            0.0093089,
            0.0,
            0.0079184,
        ),
    ),
    UnitreeG1_23DOFLinkId.PELVIS_CONTOUR: (
        "pelvis_contour_link",
        0.001,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (
            1e-07,
            0.0,
            0.0,
            1e-07,
            0.0,
            1e-07,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_HIP_PITCH: (
        "left_hip_pitch_link",
        1.35,
        ((0.002741, 0.047791, -0.02606), (0.0, 0.0, 0.0)),
        (
            0.001811,
            3.68e-05,
            -3.44e-05,
            0.0014193,
            0.000171,
            0.0012812,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_HIP_ROLL: (
        "left_hip_roll_link",
        1.52,
        ((0.029812, -0.001045, -0.087934), (0.0, 0.0, 0.0)),
        (
            0.0023773,
            -3.8e-06,
            -0.0003908,
            0.0024123,
            1.84e-05,
            0.0016595,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_HIP_YAW: (
        "left_hip_yaw_link",
        1.702,
        ((-0.057709, -0.010981, -0.15078), (0.0, 0.0, 0.0)),
        (
            0.0057774,
            -0.0005411,
            -0.0023948,
            0.0076124,
            -0.0007072,
            0.003149,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_KNEE: (
        "left_knee_link",
        1.932,
        ((0.005457, 0.003964, -0.12074), (0.0, 0.0, 0.0)),
        (
            0.011329,
            4.82e-05,
            -4.49e-05,
            0.011277,
            -0.0007146,
            0.0015168,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_ANKLE_PITCH: (
        "left_ankle_pitch_link",
        0.074,
        ((-0.007269, 0.0, 0.011137), (0.0, 0.0, 0.0)),
        (
            8.4e-06,
            0.0,
            -2.9e-06,
            1.89e-05,
            0.0,
            1.26e-05,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_ANKLE_ROLL: (
        "left_ankle_roll_link",
        0.608,
        ((0.026505, 0.0, -0.016425), (0.0, 0.0, 0.0)),
        (
            0.0002231,
            2e-07,
            8.91e-05,
            0.0016161,
            -1e-07,
            0.0016667,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_link",
        1.35,
        ((0.002741, -0.047791, -0.02606), (0.0, 0.0, 0.0)),
        (
            0.001811,
            -3.68e-05,
            -3.44e-05,
            0.0014193,
            -0.000171,
            0.0012812,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_HIP_ROLL: (
        "right_hip_roll_link",
        1.52,
        ((0.029812, 0.001045, -0.087934), (0.0, 0.0, 0.0)),
        (
            0.0023773,
            3.8e-06,
            -0.0003908,
            0.0024123,
            -1.84e-05,
            0.0016595,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_HIP_YAW: (
        "right_hip_yaw_link",
        1.702,
        ((-0.057709, 0.010981, -0.15078), (0.0, 0.0, 0.0)),
        (
            0.0057774,
            0.0005411,
            -0.0023948,
            0.0076124,
            0.0007072,
            0.003149,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_KNEE: (
        "right_knee_link",
        1.932,
        ((0.005457, -0.003964, -0.12074), (0.0, 0.0, 0.0)),
        (
            0.011329,
            -4.82e-05,
            4.49e-05,
            0.011277,
            0.0007146,
            0.0015168,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_ANKLE_PITCH: (
        "right_ankle_pitch_link",
        0.074,
        ((-0.007269, 0.0, 0.011137), (0.0, 0.0, 0.0)),
        (
            8.4e-06,
            0.0,
            -2.9e-06,
            1.89e-05,
            0.0,
            1.26e-05,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_ANKLE_ROLL: (
        "right_ankle_roll_link",
        0.608,
        ((0.026505, 0.0, -0.016425), (0.0, 0.0, 0.0)),
        (
            0.0002231,
            -2e-07,
            8.91e-05,
            0.0016161,
            1e-07,
            0.0016667,
        ),
    ),
    UnitreeG1_23DOFLinkId.WAIST_YAW_FIXED: (
        "waist_yaw_fixed_link",
        0.244,
        ((0.003964, 0.0, 0.018769), (0.0, 0.0, 0.0)),
        (
            9.9587e-05,
            -1.833e-06,
            -1.2617e-05,
            0.00012411,
            -1.18e-07,
            0.00015586,
        ),
    ),
    UnitreeG1_23DOFLinkId.TORSO: (
        "torso_link",
        8.562,
        ((0.002601, 0.000257, 0.153719), (0.0, 0.0, 0.0)),
        (
            0.065674966,
            -8.597e-05,
            -0.001737252,
            0.053535188,
            8.6899e-05,
            0.030808125,
        ),
    ),
    UnitreeG1_23DOFLinkId.LOGO: (
        "logo_link",
        0.001,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (
            1e-07,
            0.0,
            0.0,
            1e-07,
            0.0,
            1e-07,
        ),
    ),
    UnitreeG1_23DOFLinkId.HEAD: (
        "head_link",
        1.036,
        ((0.005267, 0.000299, 0.449869), (0.0, 0.0, 0.0)),
        (
            0.004085051,
            -2.543e-06,
            -6.9455e-05,
            0.004185212,
            -3.726e-06,
            0.001807911,
        ),
    ),
    UnitreeG1_23DOFLinkId.WAIST_SUPPORT: (
        "waist_support_link",
        0.001,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (
            1e-07,
            0.0,
            0.0,
            1e-07,
            0.0,
            1e-07,
        ),
    ),
    UnitreeG1_23DOFLinkId.IMU_IN_TORSO: (
        "imu_in_torso",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeG1_23DOFLinkId.IMU_IN_PELVIS: (
        "imu_in_pelvis",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeG1_23DOFLinkId.D435: (
        "d435_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeG1_23DOFLinkId.MID360: (
        "mid360_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeG1_23DOFLinkId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_link",
        0.718,
        ((0.0, 0.035892, -0.011628), (0.0, 0.0, 0.0)),
        (
            0.0004291,
            -9.2e-06,
            6.4e-06,
            0.000453,
            2.26e-05,
            0.000423,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_link",
        0.643,
        ((-0.000227, 0.00727, -0.063243), (0.0, 0.0, 0.0)),
        (
            0.0006177,
            -1e-06,
            8.7e-06,
            0.0006912,
            -5.3e-06,
            0.0003894,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_link",
        0.734,
        ((0.010773, -0.002949, -0.072009), (0.0, 0.0, 0.0)),
        (
            0.0009988,
            7.9e-06,
            0.0001412,
            0.0010605,
            -2.86e-05,
            0.0004354,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_ELBOW: (
        "left_elbow_link",
        0.6,
        ((0.064956, 0.004454, -0.010062), (0.0, 0.0, 0.0)),
        (
            0.0002891,
            6.53e-05,
            1.72e-05,
            0.0004152,
            -5.6e-06,
            0.0004197,
        ),
    ),
    UnitreeG1_23DOFLinkId.LEFT_WRIST_ROLL_RUBBER_HAND: (
        "left_wrist_roll_rubber_hand",
        0.35692864,
        ((0.1079465665, 0.00163511945, 0.00202244863), (0.0, 0.0, 0.0)),
        (
            0.00019613494735,
            -4.19816908e-06,
            -3.95086058e-05,
            0.00200280358206,
            2.49774203e-06,
            0.00194181412808,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_link",
        0.718,
        ((0.0, -0.035892, -0.011628), (0.0, 0.0, 0.0)),
        (
            0.0004291,
            9.2e-06,
            6.4e-06,
            0.000453,
            -2.26e-05,
            0.000423,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_link",
        0.643,
        ((-0.000227, -0.00727, -0.063243), (0.0, 0.0, 0.0)),
        (
            0.0006177,
            1e-06,
            8.7e-06,
            0.0006912,
            5.3e-06,
            0.0003894,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_link",
        0.734,
        ((0.010773, 0.002949, -0.072009), (0.0, 0.0, 0.0)),
        (
            0.0009988,
            -7.9e-06,
            0.0001412,
            0.0010605,
            2.86e-05,
            0.0004354,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_ELBOW: (
        "right_elbow_link",
        0.6,
        ((0.064956, -0.004454, -0.010062), (0.0, 0.0, 0.0)),
        (
            0.0002891,
            -6.53e-05,
            1.72e-05,
            0.0004152,
            5.6e-06,
            0.0004197,
        ),
    ),
    UnitreeG1_23DOFLinkId.RIGHT_WRIST_ROLL_RUBBER_HAND: (
        "right_wrist_roll_rubber_hand",
        0.35692864,
        ((0.1079465665, -0.00163511945, 0.00202244863), (0.0, 0.0, 0.0)),
        (
            0.00019613494735,
            4.19816908e-06,
            -3.95086058e-05,
            0.00200280358206,
            -2.49774203e-06,
            0.00194181412808,
        ),
    ),
}
"""URDF-derived link specifications for the Unitree G1 23-DOF robot."""


_JOINT_SPECS: dict[UnitreeG1_23DOFJointId, UnitreeG1_23DOFJointSpec] = {
    UnitreeG1_23DOFJointId.PELVIS_CONTOUR: (
        "pelvis_contour_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.PELVIS,
        UnitreeG1_23DOFLinkId.PELVIS_CONTOUR,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.LEFT_HIP_PITCH: (
        "left_hip_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.PELVIS,
        UnitreeG1_23DOFLinkId.LEFT_HIP_PITCH,
        ((0.0, 0.064452, -0.1027), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.5307, 2.8798, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_HIP_ROLL: (
        "left_hip_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_HIP_PITCH,
        UnitreeG1_23DOFLinkId.LEFT_HIP_ROLL,
        ((0.0, 0.052, -0.030465), (0.0, -0.1749, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.5236, 2.9671, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_HIP_YAW: (
        "left_hip_yaw_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_HIP_ROLL,
        UnitreeG1_23DOFLinkId.LEFT_HIP_YAW,
        ((0.025001, 0.0, -0.12412), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.7576, 2.7576, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_KNEE: (
        "left_knee_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_HIP_YAW,
        UnitreeG1_23DOFLinkId.LEFT_KNEE,
        ((-0.078273, 0.0021489, -0.17734), (0.0, 0.1749, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.087267, 2.8798, 139.0, 20.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_ANKLE_PITCH: (
        "left_ankle_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_KNEE,
        UnitreeG1_23DOFLinkId.LEFT_ANKLE_PITCH,
        ((0.0, -9.4445e-05, -0.30001), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87267, 0.5236, 35.0, 30.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_ANKLE_ROLL: (
        "left_ankle_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_ANKLE_PITCH,
        UnitreeG1_23DOFLinkId.LEFT_ANKLE_ROLL,
        ((0.0, 0.0, -0.017558), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.2618, 0.2618, 35.0, 30.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.PELVIS,
        UnitreeG1_23DOFLinkId.RIGHT_HIP_PITCH,
        ((0.0, -0.064452, -0.1027), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.5307, 2.8798, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_HIP_ROLL: (
        "right_hip_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_HIP_PITCH,
        UnitreeG1_23DOFLinkId.RIGHT_HIP_ROLL,
        ((0.0, -0.052, -0.030465), (0.0, -0.1749, 0.0)),
        (1.0, 0.0, 0.0),
        (-2.9671, 0.5236, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_HIP_YAW: (
        "right_hip_yaw_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_HIP_ROLL,
        UnitreeG1_23DOFLinkId.RIGHT_HIP_YAW,
        ((0.025001, 0.0, -0.12412), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.7576, 2.7576, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_KNEE: (
        "right_knee_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_HIP_YAW,
        UnitreeG1_23DOFLinkId.RIGHT_KNEE,
        ((-0.078273, -0.0021489, -0.17734), (0.0, 0.1749, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.087267, 2.8798, 139.0, 20.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_ANKLE_PITCH: (
        "right_ankle_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_KNEE,
        UnitreeG1_23DOFLinkId.RIGHT_ANKLE_PITCH,
        ((0.0, 9.4445e-05, -0.30001), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87267, 0.5236, 35.0, 30.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_ANKLE_ROLL: (
        "right_ankle_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_ANKLE_PITCH,
        UnitreeG1_23DOFLinkId.RIGHT_ANKLE_ROLL,
        ((0.0, 0.0, -0.017558), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.2618, 0.2618, 35.0, 30.0),
    ),
    UnitreeG1_23DOFJointId.WAIST_YAW_FIXED: (
        "waist_yaw_fixed_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.WAIST_YAW_FIXED,
        ((0.0039635, 0.0, -0.054), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.WAIST_YAW: (
        "waist_yaw_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.PELVIS,
        UnitreeG1_23DOFLinkId.TORSO,
        ((-0.0039635, 0.0, 0.054), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.618, 2.618, 88.0, 32.0),
    ),
    UnitreeG1_23DOFJointId.LOGO: (
        "logo_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.LOGO,
        ((0.0039635, 0.0, -0.054), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.HEAD: (
        "head_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.HEAD,
        ((0.0039635, 0.0, -0.054), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.WAIST_SUPPORT: (
        "waist_support_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.WAIST_SUPPORT,
        ((0.0039635, 0.0, -0.054), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.IMU_IN_TORSO: (
        "imu_in_torso_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.IMU_IN_TORSO,
        ((-0.03959, -0.00224, 0.13792), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.IMU_IN_PELVIS: (
        "imu_in_pelvis_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.PELVIS,
        UnitreeG1_23DOFLinkId.IMU_IN_PELVIS,
        ((0.04525, 0.0, -0.08339), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.D435: (
        "d435_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.D435,
        ((0.0576235, 0.01753, 0.41987), (0.0, 0.8307767239493009, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.MID360: (
        "mid360_joint",
        "fixed",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.MID360,
        ((0.0002835, 3e-05, 0.40618), (0.0, 0.04014257279586953, 0.0)),
        None,
        None,
    ),
    UnitreeG1_23DOFJointId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_PITCH,
        ((0.0039563, 0.10022, 0.23778), (0.27931, 5.4949e-05, -0.00019159)),
        (0.0, 1.0, 0.0),
        (-3.0892, 2.6704, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_PITCH,
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_ROLL,
        ((0.0, 0.038, -0.013831), (-0.27925, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.5882, 2.2515, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_ROLL,
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_YAW,
        ((0.0, 0.00624, -0.1032), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.618, 2.618, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_ELBOW: (
        "left_elbow_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_SHOULDER_YAW,
        UnitreeG1_23DOFLinkId.LEFT_ELBOW,
        ((0.015783, 0.0, -0.080518), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.0472, 2.0944, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.LEFT_WRIST_ROLL: (
        "left_wrist_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.LEFT_ELBOW,
        UnitreeG1_23DOFLinkId.LEFT_WRIST_ROLL_RUBBER_HAND,
        ((0.1, 0.00188791, -0.01), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.972222054, 1.972222054, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.TORSO,
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_PITCH,
        ((0.0039563, -0.10021, 0.23778), (-0.27931, 5.4949e-05, 0.00019159)),
        (0.0, 1.0, 0.0),
        (-3.0892, 2.6704, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_PITCH,
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_ROLL,
        ((0.0, -0.038, -0.013831), (0.27925, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-2.2515, 1.5882, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_ROLL,
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_YAW,
        ((0.0, -0.00624, -0.1032), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.618, 2.618, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_ELBOW: (
        "right_elbow_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_SHOULDER_YAW,
        UnitreeG1_23DOFLinkId.RIGHT_ELBOW,
        ((0.015783, 0.0, -0.080518), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.0472, 2.0944, 25.0, 37.0),
    ),
    UnitreeG1_23DOFJointId.RIGHT_WRIST_ROLL: (
        "right_wrist_roll_joint",
        "revolute",
        UnitreeG1_23DOFLinkId.RIGHT_ELBOW,
        UnitreeG1_23DOFLinkId.RIGHT_WRIST_ROLL_RUBBER_HAND,
        ((0.1, -0.00188791, -0.01), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-1.972222054, 1.972222054, 25.0, 37.0),
    ),
}
"""URDF-derived joint specifications for the Unitree G1 23-DOF robot."""


UNITREE_G1_23DOF_LINKAGE = Linkage[UnitreeG1_23DOFLinkId](
    links={
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    },
)
"""The linkage for the Unitree G1 23-DOF robot."""

UNITREE_G1_23DOF_ARTICULATION = Articulation[
    UnitreeG1_23DOFLinkId, UnitreeG1_23DOFJointId
](
    joints={
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    },
)
"""The articulation for the Unitree G1 23-DOF robot."""

UNITREE_G1_23DOF = Skeleton[UnitreeG1_23DOFLinkId, UnitreeG1_23DOFJointId](
    linkage=UNITREE_G1_23DOF_LINKAGE,
    articulation=UNITREE_G1_23DOF_ARTICULATION,
)
"""The kinematic chain for the Unitree G1 23-DOF robot."""
