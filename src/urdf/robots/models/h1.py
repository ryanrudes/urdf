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


class UnitreeH1LinkId(LinkId):
    """Link identifiers for the Unitree H1 robot."""

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

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_link"
    """The right shoulder pitch link."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_link"
    """The right shoulder roll link."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_link"
    """The right shoulder yaw link."""

    RIGHT_ELBOW: str = "right_elbow_link"
    """The right elbow link."""

    IMU: str = "imu_link"
    """Link with ID imu_link."""

    LOGO: str = "logo_link"
    """The logo link."""

    D435_LEFT_IMAGER: str = "d435_left_imager_link"
    """Link with ID d435_left_imager_link."""

    D435_RGB_MODULE: str = "d435_rgb_module_link"
    """Link with ID d435_rgb_module_link."""

    MID360: str = "mid360_link"
    """The mid360 link."""


class UnitreeH1JointId(JointId):
    """Joint identifiers for the Unitree H1 robot."""

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

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_joint"
    """The right shoulder pitch joint."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_joint"
    """The right shoulder roll joint."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_joint"
    """The right shoulder yaw joint."""

    RIGHT_ELBOW: str = "right_elbow_joint"
    """The right elbow joint."""

    IMU: str = "imu_joint"
    """Joint with ID imu_joint."""

    LOGO: str = "logo_joint"
    """The logo joint."""

    D435_LEFT_IMAGER: str = "d435_left_imager_joint"
    """Joint with ID d435_left_imager_joint."""

    D435_RGB_MODULE: str = "d435_rgb_module_joint"
    """Joint with ID d435_rgb_module_joint."""

    MID360: str = "mid360_joint"
    """The mid360 joint."""


type UnitreeH1Link = Link[UnitreeH1LinkId]
"""A link in the Unitree H1 robot."""

type UnitreeH1Joint = (
    FixedJoint[UnitreeH1LinkId, UnitreeH1JointId]
    | RevoluteJoint[UnitreeH1LinkId, UnitreeH1JointId]
)
"""A joint in the Unitree H1 robot."""

type UnitreeH1JointSpec = JointSpec[UnitreeH1LinkId]
"""URDF-derived data for a joint in the Unitree H1 robot."""


_LINK_SPECS: dict[UnitreeH1LinkId, LinkSpec] = {
    UnitreeH1LinkId.PELVIS: (
        "pelvis",
        5.983,
        ((-0.0004, 3.7e-05, -0.046864), (0.0, 0.0, 0.0)),
        (
            0.049168411,
            -1.9869e-05,
            -4.846e-05,
            0.009025844,
            3.431e-06,
            0.053155891,
        ),
    ),
    UnitreeH1LinkId.LEFT_HIP_YAW: (
        "left_hip_yaw_link",
        2.965,
        ((-0.061433, 1.7e-05, 0.007627), (0.0, 0.0, 0.0)),
        (
            0.005321009,
            2.253e-06,
            -0.000876895,
            0.005017692,
            1.134e-06,
            0.004100851,
        ),
    ),
    UnitreeH1LinkId.LEFT_HIP_ROLL: (
        "left_hip_roll_link",
        2.715,
        ((-0.005276, -0.013573, 4e-06), (0.0, 0.0, 0.0)),
        (
            0.003080049,
            0.00016894,
            -2.442e-06,
            0.004367226,
            4.32e-07,
            0.003475582,
        ),
    ),
    UnitreeH1LinkId.LEFT_HIP_PITCH: (
        "left_hip_pitch_link",
        4.953,
        ((0.007636, -0.029298, -0.08267), (0.0, 0.0, 0.0)),
        (
            0.096268791,
            -0.000853307,
            0.00452083,
            0.095311563,
            0.010678487,
            0.008309394,
        ),
    ),
    UnitreeH1LinkId.LEFT_KNEE: (
        "left_knee_link",
        2.824,
        ((0.003406, -0.005279, -0.143702), (0.0, 0.0, 0.0)),
        (
            0.023792186,
            -0.000201965,
            0.001348223,
            0.024505066,
            0.00034273,
            0.003235744,
        ),
    ),
    UnitreeH1LinkId.LEFT_ANKLE: (
        "left_ankle_link",
        0.725,
        ((0.042537, 0.0, -0.041674), (0.0, 0.0, 0.0)),
        (
            0.000236702,
            0.0,
            0.000197223,
            0.003296133,
            0.0,
            0.003145554,
        ),
    ),
    UnitreeH1LinkId.RIGHT_HIP_YAW: (
        "right_hip_yaw_link",
        2.965,
        ((-0.061433, -1.7e-05, 0.007627), (0.0, 0.0, 0.0)),
        (
            0.005321009,
            -2.253e-06,
            -0.000876895,
            0.005017692,
            -1.134e-06,
            0.004100851,
        ),
    ),
    UnitreeH1LinkId.RIGHT_HIP_ROLL: (
        "right_hip_roll_link",
        2.715,
        ((-0.005276, 0.013573, 4e-06), (0.0, 0.0, 0.0)),
        (
            0.003080049,
            -0.00016894,
            -2.442e-06,
            0.004367226,
            -4.32e-07,
            0.003475582,
        ),
    ),
    UnitreeH1LinkId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_link",
        4.953,
        ((0.007636, 0.029298, -0.08267), (0.0, 0.0, 0.0)),
        (
            0.096268791,
            0.000853307,
            0.00452083,
            0.095311563,
            -0.010678487,
            0.008309394,
        ),
    ),
    UnitreeH1LinkId.RIGHT_KNEE: (
        "right_knee_link",
        2.824,
        ((0.003406, 0.005279, -0.143702), (0.0, 0.0, 0.0)),
        (
            0.023792186,
            0.000201965,
            0.001348223,
            0.024505066,
            -0.00034273,
            0.003235744,
        ),
    ),
    UnitreeH1LinkId.RIGHT_ANKLE: (
        "right_ankle_link",
        0.725,
        ((0.042537, 0.0, -0.041674), (0.0, 0.0, 0.0)),
        (
            0.000236702,
            0.0,
            0.000197223,
            0.003296133,
            0.0,
            0.003145554,
        ),
    ),
    UnitreeH1LinkId.TORSO: (
        "torso_link",
        17.789,
        ((0.000489, 0.002797, 0.20484), (0.0, 0.0, 0.0)),
        (
            0.4873,
            -0.00053763,
            0.0020276,
            0.40963,
            -0.00074582,
            0.12785,
        ),
    ),
    UnitreeH1LinkId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_link",
        1.142,
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
    UnitreeH1LinkId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_link",
        0.852,
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
    UnitreeH1LinkId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_link",
        0.862,
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
    UnitreeH1LinkId.LEFT_ELBOW: (
        "left_elbow_link",
        0.745,
        ((0.164862, 0.000118, -0.015734), (0.0, 0.0, 0.0)),
        (
            0.00042388,
            -3.6086e-05,
            0.00029293,
            0.0060062,
            4.664e-06,
            0.0060023,
        ),
    ),
    UnitreeH1LinkId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_link",
        1.142,
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
    UnitreeH1LinkId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_link",
        0.852,
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
    UnitreeH1LinkId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_link",
        0.862,
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
    UnitreeH1LinkId.RIGHT_ELBOW: (
        "right_elbow_link",
        0.745,
        ((0.164862, -0.000118, -0.015734), (0.0, 0.0, 0.0)),
        (
            0.00042388,
            3.6086e-05,
            0.00029293,
            0.0060062,
            -4.664e-06,
            0.0060023,
        ),
    ),
    UnitreeH1LinkId.IMU: (
        "imu_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1LinkId.LOGO: (
        "logo_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1LinkId.D435_LEFT_IMAGER: (
        "d435_left_imager_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1LinkId.D435_RGB_MODULE: (
        "d435_rgb_module_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
    UnitreeH1LinkId.MID360: (
        "mid360_link",
        0.0,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        None,
    ),
}
"""URDF-derived link specifications for the Unitree H1 robot."""


_JOINT_SPECS: dict[UnitreeH1JointId, UnitreeH1JointSpec] = {
    UnitreeH1JointId.LEFT_HIP_YAW: (
        "left_hip_yaw_joint",
        "revolute",
        UnitreeH1LinkId.PELVIS,
        UnitreeH1LinkId.LEFT_HIP_YAW,
        ((0.0, 0.0875, -0.1742), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1JointId.LEFT_HIP_ROLL: (
        "left_hip_roll_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_HIP_YAW,
        UnitreeH1LinkId.LEFT_HIP_ROLL,
        ((0.039468, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1JointId.LEFT_HIP_PITCH: (
        "left_hip_pitch_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_HIP_ROLL,
        UnitreeH1LinkId.LEFT_HIP_PITCH,
        ((0.0, 0.11536, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.14, 2.53, 200.0, 23.0),
    ),
    UnitreeH1JointId.LEFT_KNEE: (
        "left_knee_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_HIP_PITCH,
        UnitreeH1LinkId.LEFT_KNEE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.26, 2.05, 300.0, 14.0),
    ),
    UnitreeH1JointId.LEFT_ANKLE: (
        "left_ankle_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_KNEE,
        UnitreeH1LinkId.LEFT_ANKLE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.52, 40.0, 9.0),
    ),
    UnitreeH1JointId.RIGHT_HIP_YAW: (
        "right_hip_yaw_joint",
        "revolute",
        UnitreeH1LinkId.PELVIS,
        UnitreeH1LinkId.RIGHT_HIP_YAW,
        ((0.0, -0.0875, -0.1742), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1JointId.RIGHT_HIP_ROLL: (
        "right_hip_roll_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_HIP_YAW,
        UnitreeH1LinkId.RIGHT_HIP_ROLL,
        ((0.039468, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.43, 0.43, 200.0, 23.0),
    ),
    UnitreeH1JointId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_HIP_ROLL,
        UnitreeH1LinkId.RIGHT_HIP_PITCH,
        ((0.0, -0.11536, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-3.14, 2.53, 200.0, 23.0),
    ),
    UnitreeH1JointId.RIGHT_KNEE: (
        "right_knee_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_HIP_PITCH,
        UnitreeH1LinkId.RIGHT_KNEE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.26, 2.05, 300.0, 14.0),
    ),
    UnitreeH1JointId.RIGHT_ANKLE: (
        "right_ankle_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_KNEE,
        UnitreeH1LinkId.RIGHT_ANKLE,
        ((0.0, 0.0, -0.4), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-0.87, 0.52, 40.0, 9.0),
    ),
    UnitreeH1JointId.TORSO: (
        "torso_joint",
        "revolute",
        UnitreeH1LinkId.PELVIS,
        UnitreeH1LinkId.TORSO,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-2.35, 2.35, 200.0, 23.0),
    ),
    UnitreeH1JointId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_joint",
        "revolute",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.LEFT_SHOULDER_PITCH,
        ((0.0055, 0.15535, 0.42999), (0.43633, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.87, 2.87, 40.0, 9.0),
    ),
    UnitreeH1JointId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_SHOULDER_PITCH,
        UnitreeH1LinkId.LEFT_SHOULDER_ROLL,
        ((-0.0055, 0.0565, -0.0165), (-0.43633, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-0.34, 3.11, 40.0, 9.0),
    ),
    UnitreeH1JointId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_SHOULDER_ROLL,
        UnitreeH1LinkId.LEFT_SHOULDER_YAW,
        ((0.0, 0.0, -0.1343), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-1.3, 4.45, 18.0, 20.0),
    ),
    UnitreeH1JointId.LEFT_ELBOW: (
        "left_elbow_joint",
        "revolute",
        UnitreeH1LinkId.LEFT_SHOULDER_YAW,
        UnitreeH1LinkId.LEFT_ELBOW,
        ((0.0185, 0.0, -0.198), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.25, 2.61, 18.0, 20.0),
    ),
    UnitreeH1JointId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_joint",
        "revolute",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.RIGHT_SHOULDER_PITCH,
        ((0.0055, -0.15535, 0.42999), (-0.43633, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-2.87, 2.87, 40.0, 9.0),
    ),
    UnitreeH1JointId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_SHOULDER_PITCH,
        UnitreeH1LinkId.RIGHT_SHOULDER_ROLL,
        ((-0.0055, -0.0565, -0.0165), (0.43633, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-3.11, 0.34, 40.0, 9.0),
    ),
    UnitreeH1JointId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_SHOULDER_ROLL,
        UnitreeH1LinkId.RIGHT_SHOULDER_YAW,
        ((0.0, 0.0, -0.1343), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-4.45, 1.3, 18.0, 20.0),
    ),
    UnitreeH1JointId.RIGHT_ELBOW: (
        "right_elbow_joint",
        "revolute",
        UnitreeH1LinkId.RIGHT_SHOULDER_YAW,
        UnitreeH1LinkId.RIGHT_ELBOW,
        ((0.0185, 0.0, -0.198), (0.0, 0.0, 0.0)),
        (0.0, 1.0, 0.0),
        (-1.25, 2.61, 18.0, 20.0),
    ),
    UnitreeH1JointId.IMU: (
        "imu_joint",
        "fixed",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.IMU,
        ((-0.04452, -0.01891, 0.27756), (0.0, 0.0, 0.0)),
        None,
        None,
    ),
    UnitreeH1JointId.LOGO: (
        "logo_joint",
        "fixed",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.LOGO,
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1JointId.D435_LEFT_IMAGER: (
        "d435_left_imager_joint",
        "fixed",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.D435_LEFT_IMAGER,
        ((0.10848474394, 0.0175, 0.69317107367), (-2.45735, 0.0, -1.5708)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1JointId.D435_RGB_MODULE: (
        "d435_rgb_module_joint",
        "fixed",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.D435_RGB_MODULE,
        ((0.10848474394, 0.0325, 0.69317107367), (-2.45735, 0.0, -1.5708)),
        (0.0, 0.0, 0.0),
        None,
    ),
    UnitreeH1JointId.MID360: (
        "mid360_joint",
        "fixed",
        UnitreeH1LinkId.TORSO,
        UnitreeH1LinkId.MID360,
        ((0.0472999018, 0.0, 0.67492878653), (0.0, 0.243124, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
}
"""URDF-derived joint specifications for the Unitree H1 robot."""


UNITREE_H1_LINKAGE = Linkage[UnitreeH1LinkId](
    links={
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    },
)
"""The linkage for the Unitree H1 robot."""

UNITREE_H1_ARTICULATION = Articulation[UnitreeH1LinkId, UnitreeH1JointId](
    joints={
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    },
)
"""The articulation for the Unitree H1 robot."""

UNITREE_H1 = Skeleton[UnitreeH1LinkId, UnitreeH1JointId](
    linkage=UNITREE_H1_LINKAGE,
    articulation=UNITREE_H1_ARTICULATION,
)
"""The kinematic chain for the Unitree H1 robot."""
