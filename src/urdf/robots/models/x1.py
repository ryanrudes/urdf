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


class AgiBotX1LinkId(LinkId):
    """Link identifiers for the AgiBot X1 robot."""

    BASE: str = "base_link"
    """Link with ID base_link."""

    LUMBER_YAW: str = "lumber_yaw"
    """Link with ID lumber_yaw."""

    LUMBER_ROLL: str = "lumber_roll"
    """Link with ID lumber_roll."""

    LUMBER_PITCH: str = "lumber_pitch"
    """Link with ID lumber_pitch."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch"
    """The left shoulder pitch link."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll"
    """The left shoulder roll link."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw"
    """The left shoulder yaw link."""

    LEFT_ELBOW_PITCH: str = "left_elbow_pitch"
    """Link with ID left_elbow_pitch."""

    LEFT_ELBOW_YAW: str = "left_elbow_yaw"
    """The left elbow link."""

    LEFT_WRIST_PITCH: str = "left_wrist_pitch"
    """Link with ID left_wrist_pitch."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch"
    """The right shoulder pitch link."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll"
    """The right shoulder roll link."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw"
    """The right shoulder yaw link."""

    RIGHT_ELBOW_PITCH: str = "right_elbow_pitch"
    """Link with ID right_elbow_pitch."""

    RIGHT_ELBOW_YAW: str = "right_elbow_yaw"
    """The right elbow link."""

    RIGHT_WRIST_PITCH: str = "right_wrist_pitch"
    """Link with ID right_wrist_pitch."""

    WAIST_MOTOR_A: str = "waist_motor_a_link"
    """Link with ID waist_motor_a_link."""

    WAIST_MOTOR_A_BALL: str = "waist_motor_a_ball"
    """Link with ID waist_motor_a_ball."""

    WAIST_MOTOR_A_LOOP: str = "waist_motor_a_loop"
    """Link with ID waist_motor_a_loop."""

    WAIST_MOTOR_B: str = "waist_motor_b_link"
    """Link with ID waist_motor_b_link."""

    WAIST_MOTOR_B_BALL: str = "waist_motor_b_ball"
    """Link with ID waist_motor_b_ball."""

    WAIST_MOTOR_B_LOOP: str = "waist_motor_b_loop"
    """Link with ID waist_motor_b_loop."""

    LEFT_HIP_PITCH: str = "left_hip_pitch"
    """The left hip pitch link."""

    LEFT_HIP_ROLL: str = "left_hip_roll"
    """The left hip roll link."""

    LEFT_HIP_YAW: str = "left_hip_yaw"
    """The left hip yaw link."""

    LEFT_KNEE_PITCH: str = "left_knee_pitch"
    """The left ankle pitch link."""

    LEFT_ANKLE_PITCH: str = "left_ankle_pitch"
    """The left ankle pitch link."""

    LEFT_ANKLE_ROLL: str = "left_ankle_roll"
    """The left ankle roll link."""

    LEG_L_TOE_A: str = "leg_l_toe_a_link"
    """Link with ID leg_l_toe_a_link."""

    LEG_L_TOE_A_BALL: str = "leg_l_toe_a_ball"
    """Link with ID leg_l_toe_a_ball."""

    LEG_L_TOE_A_LOOP: str = "leg_l_toe_a_loop"
    """Link with ID leg_l_toe_a_loop."""

    LEG_L_TOE_B: str = "leg_l_toe_b_link"
    """Link with ID leg_l_toe_b_link."""

    LEG_L_TOE_B_BALL: str = "leg_l_toe_b_ball"
    """Link with ID leg_l_toe_b_ball."""

    LEG_L_TOE_B_LOOP: str = "leg_l_toe_b_loop"
    """Link with ID leg_l_toe_b_loop."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch"
    """The right hip pitch link."""

    RIGHT_HIP_ROLL: str = "right_hip_roll"
    """The right hip roll link."""

    RIGHT_HIP_YAW: str = "right_hip_yaw"
    """The right hip yaw link."""

    RIGHT_KNEE_PITCH: str = "right_knee_pitch"
    """The right ankle pitch link."""

    RIGHT_ANKLE_PITCH: str = "right_ankle_pitch"
    """The right ankle pitch link."""

    RIGHT_ANKLE_ROLL: str = "right_ankle_roll"
    """The right ankle roll link."""

    LEG_R_TOE_A: str = "leg_r_toe_a_link"
    """Link with ID leg_r_toe_a_link."""

    LEG_R_TOE_A_BALL: str = "leg_r_toe_a_ball"
    """Link with ID leg_r_toe_a_ball."""

    LEG_R_TOE_A_LOOP: str = "leg_r_toe_a_loop"
    """Link with ID leg_r_toe_a_loop."""

    LEG_R_TOE_B: str = "leg_r_toe_b_link"
    """Link with ID leg_r_toe_b_link."""

    LEG_R_TOE_B_BALL: str = "leg_r_toe_b_ball"
    """Link with ID leg_r_toe_b_ball."""

    LEG_R_TOE_B_LOOP: str = "leg_r_toe_b_loop"
    """Link with ID leg_r_toe_b_loop."""

    ARM_R_WRIST_A_BALL: str = "arm_r_wrist_a_ball"
    """Link with ID arm_r_wrist_a_ball."""

    ARM_R_WRIST_MOTOR_A: str = "arm_r_wrist_motor_a_link"
    """Link with ID arm_r_wrist_motor_a_link."""

    ARM_R_WRIST_A_LOOP: str = "arm_r_wrist_a_loop"
    """Link with ID arm_r_wrist_a_loop."""

    ARM_R_WRIST_B_BALL: str = "arm_r_wrist_b_ball"
    """Link with ID arm_r_wrist_b_ball."""

    ARM_R_WRIST_MOTOR_B: str = "arm_r_wrist_motor_b_link"
    """Link with ID arm_r_wrist_motor_b_link."""

    ARM_R_WRIST_B_LOOP: str = "arm_r_wrist_b_loop"
    """Link with ID arm_r_wrist_b_loop."""

    ARM_L_WRIST_A_BALL: str = "arm_l_wrist_a_ball"
    """Link with ID arm_l_wrist_a_ball."""

    ARM_L_WRIST_MOTOR_A: str = "arm_l_wrist_motor_a_link"
    """Link with ID arm_l_wrist_motor_a_link."""

    ARM_L_WRIST_A_LOOP: str = "arm_l_wrist_a_loop"
    """Link with ID arm_l_wrist_a_loop."""

    ARM_L_WRIST_B_BALL: str = "arm_l_wrist_b_ball"
    """Link with ID arm_l_wrist_b_ball."""

    ARM_L_WRIST_MOTOR_B: str = "arm_l_wrist_motor_b_link"
    """Link with ID arm_l_wrist_motor_b_link."""

    ARM_L_WRIST_B_LOOP: str = "arm_l_wrist_b_loop"
    """Link with ID arm_l_wrist_b_loop."""


class AgiBotX1JointId(JointId):
    """Joint identifiers for the AgiBot X1 robot."""

    LUMBER_YAW: str = "lumber_yaw_joint"
    """Joint with ID lumber_yaw_joint."""

    LUMBER_ROLL: str = "lumber_roll_joint"
    """Joint with ID lumber_roll_joint."""

    LUMBER_PITCH: str = "lumber_pitch_joint"
    """Joint with ID lumber_pitch_joint."""

    LEFT_SHOULDER_PITCH: str = "left_shoulder_pitch_joint"
    """The left shoulder pitch joint."""

    LEFT_SHOULDER_ROLL: str = "left_shoulder_roll_joint"
    """The left shoulder roll joint."""

    LEFT_SHOULDER_YAW: str = "left_shoulder_yaw_joint"
    """The left shoulder yaw joint."""

    LEFT_ELBOW_PITCH: str = "left_elbow_pitch_joint"
    """Joint with ID left_elbow_pitch_joint."""

    LEFT_ELBOW_YAW: str = "left_elbow_yaw_joint"
    """The left elbow joint."""

    LEFT_WRIST_PITCH: str = "left_wrist_pitch_joint"
    """Joint with ID left_wrist_pitch_joint."""

    RIGHT_SHOULDER_PITCH: str = "right_shoulder_pitch_joint"
    """The right shoulder pitch joint."""

    RIGHT_SHOULDER_ROLL: str = "right_shoulder_roll_joint"
    """The right shoulder roll joint."""

    RIGHT_SHOULDER_YAW: str = "right_shoulder_yaw_joint"
    """The right shoulder yaw joint."""

    RIGHT_ELBOW_PITCH: str = "right_elbow_pitch_joint"
    """Joint with ID right_elbow_pitch_joint."""

    RIGHT_ELBOW_YAW: str = "right_elbow_yaw_joint"
    """The right elbow joint."""

    RIGHT_WRIST_PITCH: str = "right_wrist_pitch_joint"
    """Joint with ID right_wrist_pitch_joint."""

    WAIST_MOTOR_A_LINK: str = "waist_motor_a_link_joint"
    """Joint with ID waist_motor_a_link_joint."""

    WAIST_MOTOR_A_BALL: str = "waist_motor_a_ball_joint"
    """Joint with ID waist_motor_a_ball_joint."""

    WAIST_MOTOR_A_LOOP: str = "waist_motor_a_loop_joint"
    """Joint with ID waist_motor_a_loop_joint."""

    WAIST_MOTOR_B_LINK: str = "waist_motor_b_link_joint"
    """Joint with ID waist_motor_b_link_joint."""

    WAIST_MOTOR_B_BALL: str = "waist_motor_b_ball_joint"
    """Joint with ID waist_motor_b_ball_joint."""

    WAIST_MOTOR_B_LOOP: str = "waist_motor_b_loop_joint"
    """Joint with ID waist_motor_b_loop_joint."""

    LEFT_HIP_PITCH: str = "left_hip_pitch_joint"
    """The left hip pitch joint."""

    LEFT_HIP_ROLL: str = "left_hip_roll_joint"
    """The left hip roll joint."""

    LEFT_HIP_YAW: str = "left_hip_yaw_joint"
    """The left hip yaw joint."""

    LEFT_KNEE_PITCH: str = "left_knee_pitch_joint"
    """The left ankle pitch joint."""

    LEFT_ANKLE_PITCH: str = "left_ankle_pitch_joint"
    """The left ankle pitch joint."""

    LEFT_ANKLE_ROLL: str = "left_ankle_roll_joint"
    """The left ankle roll joint."""

    LEG_L_TOE_A_LINK: str = "leg_l_toe_a_link_joint"
    """Joint with ID leg_l_toe_a_link_joint."""

    LEG_L_TOE_A_BALL: str = "leg_l_toe_a_ball_joint"
    """Joint with ID leg_l_toe_a_ball_joint."""

    LEG_L_TOE_A_LOOP: str = "leg_l_toe_a_loop_joint"
    """Joint with ID leg_l_toe_a_loop_joint."""

    LEG_L_TOE_B_LINK: str = "leg_l_toe_b_link_joint"
    """Joint with ID leg_l_toe_b_link_joint."""

    LEG_L_TOE_B_BALL: str = "leg_l_toe_b_ball_joint"
    """Joint with ID leg_l_toe_b_ball_joint."""

    LEG_L_TOE_B_LOOP: str = "leg_l_toe_b_loop_joint"
    """Joint with ID leg_l_toe_b_loop_joint."""

    RIGHT_HIP_PITCH: str = "right_hip_pitch_joint"
    """The right hip pitch joint."""

    RIGHT_HIP_ROLL: str = "right_hip_roll_joint"
    """The right hip roll joint."""

    RIGHT_HIP_YAW: str = "right_hip_yaw_joint"
    """The right hip yaw joint."""

    RIGHT_KNEE_PITCH: str = "right_knee_pitch_joint"
    """The right ankle pitch joint."""

    RIGHT_ANKLE_PITCH: str = "right_ankle_pitch_joint"
    """The right ankle pitch joint."""

    RIGHT_ANKLE_ROLL: str = "right_ankle_roll_joint"
    """The right ankle roll joint."""

    LEG_R_TOE_A_LINK: str = "leg_r_toe_a_link_joint"
    """Joint with ID leg_r_toe_a_link_joint."""

    LEG_R_TOE_A_BALL: str = "leg_r_toe_a_ball_joint"
    """Joint with ID leg_r_toe_a_ball_joint."""

    LEG_R_TOE_A_LOOP: str = "leg_r_toe_a_loop_joint"
    """Joint with ID leg_r_toe_a_loop_joint."""

    LEG_R_TOE_B_LINK: str = "leg_r_toe_b_link_joint"
    """Joint with ID leg_r_toe_b_link_joint."""

    LEG_R_TOE_B_BALL: str = "leg_r_toe_b_ball_joint"
    """Joint with ID leg_r_toe_b_ball_joint."""

    LEG_R_TOE_B_LOOP: str = "leg_r_toe_b_loop_joint"
    """Joint with ID leg_r_toe_b_loop_joint."""

    ARM_R_WRIST_A_BALL: str = "arm_r_wrist_a_ball_joint"
    """Joint with ID arm_r_wrist_a_ball_joint."""

    ARM_R_WRIST_MOTOR_A_LINK: str = "arm_r_wrist_motor_a_link_joint"
    """Joint with ID arm_r_wrist_motor_a_link_joint."""

    ARM_R_WRIST_A_LOOP: str = "arm_r_wrist_a_loop_joint"
    """Joint with ID arm_r_wrist_a_loop_joint."""

    ARM_R_WRIST_B_BALL: str = "arm_r_wrist_b_ball_joint"
    """Joint with ID arm_r_wrist_b_ball_joint."""

    ARM_R_WRIST_MOTOR_B_LINK: str = "arm_r_wrist_motor_b_link_joint"
    """Joint with ID arm_r_wrist_motor_b_link_joint."""

    ARM_R_WRIST_B_LOOP: str = "arm_r_wrist_b_loop_joint"
    """Joint with ID arm_r_wrist_b_loop_joint."""

    ARM_L_WRIST_A_BALL: str = "arm_l_wrist_a_ball_joint"
    """Joint with ID arm_l_wrist_a_ball_joint."""

    ARM_L_WRIST_MOTOR_A_LINK: str = "arm_l_wrist_motor_a_link_joint"
    """Joint with ID arm_l_wrist_motor_a_link_joint."""

    ARM_L_WRIST_A_LOOP: str = "arm_l_wrist_a_loop_joint"
    """Joint with ID arm_l_wrist_a_loop_joint."""

    ARM_L_WRIST_B_BALL: str = "arm_l_wrist_b_ball_joint"
    """Joint with ID arm_l_wrist_b_ball_joint."""

    ARM_L_WRIST_MOTOR_B_LINK: str = "arm_l_wrist_motor_b_link_joint"
    """Joint with ID arm_l_wrist_motor_b_link_joint."""

    ARM_L_WRIST_B_LOOP: str = "arm_l_wrist_b_loop_joint"
    """Joint with ID arm_l_wrist_b_loop_joint."""


type AgiBotX1Link = Link[AgiBotX1LinkId]
"""A link in the AgiBot X1 robot."""

type AgiBotX1Joint = (
    FixedJoint[AgiBotX1LinkId, AgiBotX1JointId]
    | RevoluteJoint[AgiBotX1LinkId, AgiBotX1JointId]
)
"""A joint in the AgiBot X1 robot."""

type AgiBotX1JointSpec = JointSpec[AgiBotX1LinkId]
"""URDF-derived data for a joint in the AgiBot X1 robot."""


_LINK_SPECS: dict[AgiBotX1LinkId, LinkSpec] = {
    AgiBotX1LinkId.BASE: (
        "base_link",
        4.3041648,
        ((0.00252285, -0.00063439, 0.03023409), (0.0, 0.0, 0.0)),
        (
            0.02680559,
            -5.49e-06,
            5.389e-05,
            0.01083128,
            -0.00011229,
            0.02180955,
        ),
    ),
    AgiBotX1LinkId.LUMBER_YAW: (
        "lumber_yaw",
        0.36251906,
        ((-0.01800066, 1.4e-06, 0.02432982), (0.0, 0.0, 0.0)),
        (
            0.00035849,
            0.0,
            6.896e-05,
            0.00045823,
            -1e-08,
            0.00063906,
        ),
    ),
    AgiBotX1LinkId.LUMBER_ROLL: (
        "lumber_roll",
        0.03412073,
        ((-0.00029919, 0.0003642, -0.00019197), (0.0, 0.0, 0.0)),
        (
            4.93e-06,
            1.3e-07,
            0.0,
            5.42e-06,
            -9e-08,
            4.83e-06,
        ),
    ),
    AgiBotX1LinkId.LUMBER_PITCH: (
        "lumber_pitch",
        8.8571074,
        ((0.00070244, 0.21072612, -0.00117164), (0.0, 0.0, 0.0)),
        (
            0.14777412,
            -0.00392755,
            0.00035997,
            0.06085873,
            -0.00078171,
            0.11164753,
        ),
    ),
    AgiBotX1LinkId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch",
        1.0067875,
        ((-0.00251212, -0.00149141, -0.05674475), (0.0, 0.0, 0.0)),
        (
            0.00108106,
            2.069e-05,
            1.583e-05,
            0.00096162,
            1.04e-06,
            0.0008545,
        ),
    ),
    AgiBotX1LinkId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll",
        0.69169508,
        ((0.000154, 0.07784637, -0.02711338), (0.0, 0.0, 0.0)),
        (
            0.00133669,
            1.21e-06,
            3.26e-06,
            0.00065344,
            9.451e-05,
            0.00117974,
        ),
    ),
    AgiBotX1LinkId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw",
        0.72559372,
        ((-2.68e-06, 0.00182113, -0.00392718), (0.0, 0.0, 0.0)),
        (
            0.00116043,
            -5.8e-07,
            1.27e-06,
            0.00117758,
            -6.33e-05,
            0.00048696,
        ),
    ),
    AgiBotX1LinkId.LEFT_ELBOW_PITCH: (
        "left_elbow_pitch",
        0.69780135,
        ((2.604e-05, 0.07528242, 0.0268658), (0.0, 0.0, 0.0)),
        (
            0.00116267,
            2.7e-07,
            1.6e-07,
            0.00064619,
            -0.00010622,
            0.00096882,
        ),
    ),
    AgiBotX1LinkId.LEFT_ELBOW_YAW: (
        "left_elbow_yaw",
        0.28787886,
        ((3.656e-05, 0.00424199, -0.05421422), (0.0, 0.0, 0.0)),
        (
            0.00071486,
            9e-08,
            -3.7e-07,
            0.00069793,
            2.677e-05,
            0.00054487,
        ),
    ),
    AgiBotX1LinkId.LEFT_WRIST_PITCH: (
        "left_wrist_pitch",
        0.00900738,
        ((-9.994e-05, 0.0, 0.00229425), (0.0, 0.0, 0.0)),
        (
            2.4e-07,
            0.0,
            0.0,
            5.7e-07,
            0.0,
            3.8e-07,
        ),
    ),
    AgiBotX1LinkId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch",
        1.0067875,
        ((0.00250704, -0.00149173, -0.05674328), (0.0, 0.0, 0.0)),
        (
            0.00108106,
            -2.069e-05,
            -1.583e-05,
            0.00096162,
            8.4e-07,
            0.0008545,
        ),
    ),
    AgiBotX1LinkId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll",
        0.69142604,
        ((9.998e-05, -0.07787239, -0.02705625), (0.0, 0.0, 0.0)),
        (
            0.00133757,
            -3.8e-07,
            -2.53e-06,
            0.00065281,
            -9.481e-05,
            0.00118057,
        ),
    ),
    AgiBotX1LinkId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw",
        0.604503,
        ((-0.00189082, -0.00017102, 0.03175107), (0.0, 0.0, 0.0)),
        (
            0.00050135,
            2.4e-06,
            6.05e-06,
            0.00055045,
            -1.7e-07,
            0.00049583,
        ),
    ),
    AgiBotX1LinkId.RIGHT_ELBOW_PITCH: (
        "right_elbow_pitch",
        0.69780135,
        ((-2.604e-05, -0.07529828, 0.02685625), (0.0, 0.0, 0.0)),
        (
            0.00116302,
            2.7e-07,
            -1.6e-07,
            0.00064594,
            0.00010623,
            0.00096939,
        ),
    ),
    AgiBotX1LinkId.RIGHT_ELBOW_YAW: (
        "right_elbow_yaw",
        0.28835476,
        ((-3.65e-05, -0.00422926, -0.05414537), (0.0, 0.0, 0.0)),
        (
            0.00071572,
            9e-08,
            3.7e-07,
            0.00069879,
            -2.692e-05,
            0.00054493,
        ),
    ),
    AgiBotX1LinkId.RIGHT_WRIST_PITCH: (
        "right_wrist_pitch",
        0.00900738,
        ((-9.994e-05, 0.0, 0.00229425), (0.0, 0.0, 0.0)),
        (
            2.4e-07,
            0.0,
            0.0,
            5.7e-07,
            0.0,
            3.8e-07,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_A: (
        "waist_motor_a_link",
        0.05818703,
        ((-0.04046842, 0.0, -0.00673515), (0.0, 0.0, 0.0)),
        (
            1.004e-05,
            -3e-08,
            -1.16e-05,
            5.053e-05,
            0.0,
            4.77e-05,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_A_BALL: (
        "waist_motor_a_ball",
        0.03613902,
        ((-0.00179727, 0.03749978, -3.559e-05), (0.0, 0.0, 0.0)),
        (
            3.412e-05,
            0.0,
            0.0,
            2.43e-06,
            0.0,
            3.624e-05,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_A_LOOP: (
        "waist_motor_a_loop",
        0.01765296,
        ((0.0, 0.0, 0.00052471), (0.0, 0.0, 0.0)),
        (
            8e-07,
            0.0,
            0.0,
            8e-07,
            0.0,
            3.5e-07,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_B: (
        "waist_motor_b_link",
        0.05818703,
        ((-0.04046842, 0.0, -0.00673515), (0.0, 0.0, 0.0)),
        (
            1.004e-05,
            -3e-08,
            -1.16e-05,
            5.053e-05,
            0.0,
            4.77e-05,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_B_BALL: (
        "waist_motor_b_ball",
        0.03613902,
        ((3.559e-05, -0.03749978, 0.00179727), (0.0, 0.0, 0.0)),
        (
            3.624e-05,
            0.0,
            0.0,
            2.43e-06,
            0.0,
            3.412e-05,
        ),
    ),
    AgiBotX1LinkId.WAIST_MOTOR_B_LOOP: (
        "waist_motor_b_loop",
        0.01765296,
        ((-0.00052471, 0.0, 0.0), (0.0, 0.0, 0.0)),
        (
            3.5e-07,
            0.0,
            0.0,
            8e-07,
            0.0,
            8e-07,
        ),
    ),
    AgiBotX1LinkId.LEFT_HIP_PITCH: (
        "left_hip_pitch",
        1.6733645,
        ((-4.816e-05, -0.01075844, -0.05407776), (0.0, 0.0, 0.0)),
        (
            0.00234427,
            -2.8e-06,
            -8.23e-06,
            0.00252881,
            -0.00011548,
            0.00218719,
        ),
    ),
    AgiBotX1LinkId.LEFT_HIP_ROLL: (
        "left_hip_roll",
        0.28562185,
        ((0.00014604, -0.04123483, -0.01015339), (0.0, 0.0, 0.0)),
        (
            0.00055729,
            9.8e-07,
            5.6e-07,
            0.0004105,
            -0.00016545,
            0.00047775,
        ),
    ),
    AgiBotX1LinkId.LEFT_HIP_YAW: (
        "left_hip_yaw",
        2.7369623,
        ((-0.00212295, -3.062e-05, 0.09164842), (0.0, 0.0, 0.0)),
        (
            0.01270795,
            -2.44e-06,
            0.00060592,
            0.01244948,
            4.78e-06,
            0.00342683,
        ),
    ),
    AgiBotX1LinkId.LEFT_KNEE_PITCH: (
        "left_knee_pitch",
        1.5122608,
        ((-0.0047354, -0.13101324, 0.0279688), (0.0, 0.0, 0.0)),
        (
            0.00806663,
            -5.703e-05,
            3.669e-05,
            0.00174565,
            0.00090864,
            0.00825577,
        ),
    ),
    AgiBotX1LinkId.LEFT_ANKLE_PITCH: (
        "left_ankle_pitch",
        0.06217211,
        ((-2.32e-06, 7.077e-05, -2.048e-05), (0.0, 0.0, 0.0)),
        (
            2.273e-05,
            0.0,
            0.0,
            2.373e-05,
            0.0,
            6.68e-06,
        ),
    ),
    AgiBotX1LinkId.LEFT_ANKLE_ROLL: (
        "left_ankle_roll",
        0.58971207,
        ((0.00017156, -0.02524695, -0.00019936), (0.0, 0.0, 0.0)),
        (
            0.00152113,
            4.7e-07,
            3.91e-06,
            0.00189897,
            4.837e-05,
            0.00054313,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_A: (
        "leg_l_toe_a_link",
        0.03114168,
        ((-0.00875902, 0.00339112, -0.00875449), (0.0, 0.0, 0.0)),
        (
            4.33e-06,
            1.42e-06,
            -1.59e-06,
            7.48e-06,
            6.1e-07,
            8.76e-06,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_A_BALL: (
        "leg_l_toe_a_ball",
        0.05674707,
        ((-1.914e-05, -0.0941377, 1.9e-06), (0.0, 0.0, 0.0)),
        (
            0.00022106,
            -1e-07,
            0.0,
            1.09e-06,
            -1e-08,
            0.00022113,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_A_LOOP: (
        "leg_l_toe_a_loop",
        0.0062017,
        ((0.0, 0.0, -0.0006502), (0.0, 0.0, 0.0)),
        (
            2.8e-07,
            0.0,
            0.0,
            2.8e-07,
            0.0,
            1.2e-07,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_B: (
        "leg_l_toe_b_link",
        0.03161,
        ((0.0089831, 0.00345524, -0.00906395), (0.0, 0.0, 0.0)),
        (
            4.6e-06,
            -1.46e-06,
            1.73e-06,
            7.81e-06,
            6.7e-07,
            8.88e-06,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_B_BALL: (
        "leg_l_toe_b_ball",
        0.0423305,
        ((-2.566e-05, -0.06676392, 2.566e-05), (0.0, 0.0, 0.0)),
        (
            9.172e-05,
            -7e-08,
            0.0,
            9.5e-07,
            -7e-08,
            9.179e-05,
        ),
    ),
    AgiBotX1LinkId.LEG_L_TOE_B_LOOP: (
        "leg_l_toe_b_loop",
        0.0062017,
        ((0.0, 0.0, 0.00064901), (0.0, 0.0, 0.0)),
        (
            2.8e-07,
            0.0,
            0.0,
            2.8e-07,
            0.0,
            1.2e-07,
        ),
    ),
    AgiBotX1LinkId.RIGHT_HIP_PITCH: (
        "right_hip_pitch",
        1.6665735,
        ((-0.00011915, 0.01061483, -0.05407727), (0.0, 0.0, 0.0)),
        (
            0.00232109,
            6.27e-06,
            -4.66e-06,
            0.00250972,
            0.00011538,
            0.00216871,
        ),
    ),
    AgiBotX1LinkId.RIGHT_HIP_ROLL: (
        "right_hip_roll",
        0.28768793,
        ((-0.00027058, -0.04164617, 0.01034263), (0.0, 0.0, 0.0)),
        (
            0.0005667,
            -5.75e-06,
            2.7e-06,
            0.00041717,
            0.00016914,
            0.00048988,
        ),
    ),
    AgiBotX1LinkId.RIGHT_HIP_YAW: (
        "right_hip_yaw",
        2.6963535,
        ((-0.00241642, 1.672e-05, -0.09704704), (0.0, 0.0, 0.0)),
        (
            0.01254086,
            -9.4e-07,
            -0.00059613,
            0.01225062,
            -3.99e-06,
            0.00336389,
        ),
    ),
    AgiBotX1LinkId.RIGHT_KNEE_PITCH: (
        "right_knee_pitch",
        1.50954,
        ((0.00477062, -0.13172342, 0.02793834), (0.0, 0.0, 0.0)),
        (
            0.0080222,
            3.758e-05,
            -3.424e-05,
            0.00174185,
            0.00090582,
            0.00821165,
        ),
    ),
    AgiBotX1LinkId.RIGHT_ANKLE_PITCH: (
        "right_ankle_pitch",
        0.06217211,
        ((2.47e-06, -7.076e-05, -1.763e-05), (0.0, 0.0, 0.0)),
        (
            2.273e-05,
            0.0,
            0.0,
            2.373e-05,
            -1e-08,
            6.68e-06,
        ),
    ),
    AgiBotX1LinkId.RIGHT_ANKLE_ROLL: (
        "right_ankle_roll",
        0.59182763,
        ((-2.32e-06, 0.02507893, 0.00010556), (0.0, 0.0, 0.0)),
        (
            0.00151845,
            1e-08,
            5e-08,
            0.00189242,
            -4.706e-05,
            0.00054401,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_A: (
        "leg_r_toe_a_link",
        0.03114168,
        ((0.00876658, 0.00337152, -0.00875449), (0.0, 0.0, 0.0)),
        (
            4.34e-06,
            -1.43e-06,
            1.59e-06,
            7.47e-06,
            6.2e-07,
            8.76e-06,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_A_BALL: (
        "leg_r_toe_a_ball",
        0.05674707,
        ((-1.914e-05, -0.0941377, 1.914e-05), (0.0, 0.0, 0.0)),
        (
            0.00022106,
            -1e-07,
            0.0,
            1.09e-06,
            -1e-07,
            0.00022113,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_A_LOOP: (
        "leg_r_toe_a_loop",
        0.0062017,
        ((0.0, 0.0, 0.00064901), (0.0, 0.0, 0.0)),
        (
            2.8e-07,
            0.0,
            0.0,
            2.8e-07,
            0.0,
            1.2e-07,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_B: (
        "leg_r_toe_b_link",
        0.03161,
        ((-0.00897565, 0.00347454, -0.00906395), (0.0, 0.0, 0.0)),
        (
            4.59e-06,
            1.46e-06,
            -1.73e-06,
            7.82e-06,
            6.7e-07,
            8.88e-06,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_B_BALL: (
        "leg_r_toe_b_ball",
        0.0423305,
        ((-2.566e-05, -0.06676392, 2.566e-05), (0.0, 0.0, 0.0)),
        (
            9.172e-05,
            -7e-08,
            0.0,
            9.5e-07,
            -7e-08,
            9.179e-05,
        ),
    ),
    AgiBotX1LinkId.LEG_R_TOE_B_LOOP: (
        "leg_r_toe_b_loop",
        0.0062017,
        ((0.0, 0.0, -0.00064901), (0.0, 0.0, 0.0)),
        (
            2.8e-07,
            0.0,
            0.0,
            2.8e-07,
            0.0,
            1.2e-07,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_A_BALL: (
        "arm_r_wrist_a_ball",
        0.23598732,
        ((0.00076586, -0.01156825, 4.912e-05), (0.0, 0.0, 0.0)),
        (
            7.634e-05,
            1.26e-06,
            -3e-08,
            2.519e-05,
            -1e-07,
            7.977e-05,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_MOTOR_A: (
        "arm_r_wrist_motor_a_link",
        0.00117982,
        ((0.0, 0.0, 0.00973737), (0.0, 0.0, 0.0)),
        (
            6e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            2e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_A_LOOP: (
        "arm_r_wrist_a_loop",
        0.00548041,
        ((0.0, 0.0, -1.922e-05), (0.0, 0.0, 0.0)),
        (
            8e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            7e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_B_BALL: (
        "arm_r_wrist_b_ball",
        0.03617567,
        ((0.00121967, 0.04417257, 0.0), (0.0, 0.0, 0.0)),
        (
            1.73e-05,
            -4.1e-07,
            0.0,
            4.69e-06,
            0.0,
            1.731e-05,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_MOTOR_B: (
        "arm_r_wrist_motor_b_link",
        0.00117982,
        ((0.0, 0.0, 0.00973737), (0.0, 0.0, 0.0)),
        (
            6e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            2e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_R_WRIST_B_LOOP: (
        "arm_r_wrist_b_loop",
        0.00548041,
        ((0.0, 0.0, -1.922e-05), (0.0, 0.0, 0.0)),
        (
            8e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            7e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_A_BALL: (
        "arm_l_wrist_a_ball",
        0.23598732,
        ((0.00076586, -0.01156825, 4.912e-05), (0.0, 0.0, 0.0)),
        (
            7.634e-05,
            1.26e-06,
            -3e-08,
            2.519e-05,
            -1e-07,
            7.977e-05,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_MOTOR_A: (
        "arm_l_wrist_motor_a_link",
        0.00117982,
        ((0.0, 0.0, 0.00973737), (0.0, 0.0, 0.0)),
        (
            6e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            2e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_A_LOOP: (
        "arm_l_wrist_a_loop",
        0.00548041,
        ((0.0, 0.0, -1.922e-05), (0.0, 0.0, 0.0)),
        (
            8e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            7e-08,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_B_BALL: (
        "arm_l_wrist_b_ball",
        0.03617567,
        ((0.00121967, 0.04417257, 0.0), (0.0, 0.0, 0.0)),
        (
            1.73e-05,
            -4.1e-07,
            0.0,
            4.69e-06,
            0.0,
            1.731e-05,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_MOTOR_B: (
        "arm_l_wrist_motor_b_link",
        0.23598732,
        ((0.00076586, 0.01156825, -4.912e-05), (0.0, 0.0, 0.0)),
        (
            7.634e-05,
            -1.26e-06,
            3e-08,
            2.519e-05,
            -1e-07,
            7.977e-05,
        ),
    ),
    AgiBotX1LinkId.ARM_L_WRIST_B_LOOP: (
        "arm_l_wrist_b_loop",
        0.00117982,
        ((0.0, 0.0, 0.00973737), (0.0, 0.0, 0.0)),
        (
            6e-08,
            0.0,
            0.0,
            8e-08,
            0.0,
            2e-08,
        ),
    ),
}
"""URDF-derived link specifications for the AgiBot X1 robot."""


_JOINT_SPECS: dict[AgiBotX1JointId, AgiBotX1JointSpec] = {
    AgiBotX1JointId.LUMBER_YAW: (
        "lumber_yaw_joint",
        "fixed",
        AgiBotX1LinkId.BASE,
        AgiBotX1LinkId.LUMBER_YAW,
        (
            (0.00244999999994827, 0.0, 0.115534033809005),
            (0.0, 0.0, -4.54911392613975e-05),
        ),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LUMBER_ROLL: (
        "lumber_roll_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_YAW,
        AgiBotX1LinkId.LUMBER_ROLL,
        ((0.0, 0.0, 0.0405), (1.57079632679491, 0.0, -1.5707963267949)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LUMBER_PITCH: (
        "lumber_pitch_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_ROLL,
        AgiBotX1LinkId.LUMBER_PITCH,
        ((0.0, 0.0, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_SHOULDER_PITCH: (
        "left_shoulder_pitch_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_PITCH,
        AgiBotX1LinkId.LEFT_SHOULDER_PITCH,
        ((0.0, 0.255999999999995, -0.145800000000004), (0.0, 0.0, -3.14159265358978)),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_SHOULDER_ROLL: (
        "left_shoulder_roll_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_SHOULDER_PITCH,
        AgiBotX1LinkId.LEFT_SHOULDER_ROLL,
        ((-0.0313, 0.0, -0.0592), (0.0, -1.5708, 0.0)),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_SHOULDER_YAW: (
        "left_shoulder_yaw_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_SHOULDER_ROLL,
        AgiBotX1LinkId.LEFT_SHOULDER_YAW,
        ((0.0, 0.1252, -0.0313000000000029), (1.57079632679488, 1.5707963267949, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_ELBOW_PITCH: (
        "left_elbow_pitch_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_SHOULDER_YAW,
        AgiBotX1LinkId.LEFT_ELBOW_PITCH,
        ((0.0, -0.031, -0.0365000000000021), (-1.5707963267949, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_ELBOW_YAW: (
        "left_elbow_yaw_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_ELBOW_PITCH,
        AgiBotX1LinkId.LEFT_ELBOW_YAW,
        ((0.0, 0.116999999999998, 0.0310000000000001), (1.5707963267949, -1.5708, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEFT_WRIST_PITCH: (
        "left_wrist_pitch_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_ELBOW_YAW,
        AgiBotX1LinkId.LEFT_WRIST_PITCH,
        ((0.006, 9.9998e-05, -0.1394), (1.5708, 0.0, 0.0)),
        (-1.0, 0.0, 0.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_SHOULDER_PITCH: (
        "right_shoulder_pitch_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_PITCH,
        AgiBotX1LinkId.RIGHT_SHOULDER_PITCH,
        ((0.0, 0.256, 0.1458), (3.1416, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_SHOULDER_ROLL: (
        "right_shoulder_roll_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_SHOULDER_PITCH,
        AgiBotX1LinkId.RIGHT_SHOULDER_ROLL,
        ((0.0313, 0.0, -0.0592), (3.1416, -1.5708, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_SHOULDER_YAW: (
        "right_shoulder_yaw_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_SHOULDER_ROLL,
        AgiBotX1LinkId.RIGHT_SHOULDER_YAW,
        ((0.0, -0.1252, -0.0313), (1.5708, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_ELBOW_PITCH: (
        "right_elbow_pitch_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_SHOULDER_YAW,
        AgiBotX1LinkId.RIGHT_ELBOW_PITCH,
        (
            (-0.0309999999999999, 0.0, 0.0365000000000022),
            (-1.5707963267949, 0.0, -1.5707963267949),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_ELBOW_YAW: (
        "right_elbow_yaw_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_ELBOW_PITCH,
        AgiBotX1LinkId.RIGHT_ELBOW_YAW,
        (
            (0.0, -0.116999999999998, 0.0310000000000001),
            (-1.5707963267949, -1.5708, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.RIGHT_WRIST_PITCH: (
        "right_wrist_pitch_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_ELBOW_YAW,
        AgiBotX1LinkId.RIGHT_WRIST_PITCH,
        ((0.006, 9.9998e-05, -0.1394), (1.5708, 0.0, 0.0)),
        (1.0, 0.0, 0.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.WAIST_MOTOR_A_LINK: (
        "waist_motor_a_link_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_PITCH,
        AgiBotX1LinkId.WAIST_MOTOR_A,
        ((0.0, 0.0749999999999926, 0.0708000000001417), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.WAIST_MOTOR_A_BALL: (
        "waist_motor_a_ball_joint",
        "fixed",
        AgiBotX1LinkId.WAIST_MOTOR_A,
        AgiBotX1LinkId.WAIST_MOTOR_A_BALL,
        ((-0.065, 0.0, -0.0108000000001461), (3.14159265358979, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.WAIST_MOTOR_A_LOOP: (
        "waist_motor_a_loop_joint",
        "fixed",
        AgiBotX1LinkId.WAIST_MOTOR_A_BALL,
        AgiBotX1LinkId.WAIST_MOTOR_A_LOOP,
        ((0.0, 0.0749999999999924, 0.0), (3.14159265358979, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.WAIST_MOTOR_B_LINK: (
        "waist_motor_b_link_joint",
        "fixed",
        AgiBotX1LinkId.LUMBER_PITCH,
        AgiBotX1LinkId.WAIST_MOTOR_B,
        ((0.0, 0.0750000000000303, -0.0708000000000074), (3.14159265358979, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.WAIST_MOTOR_B_BALL: (
        "waist_motor_b_ball_joint",
        "fixed",
        AgiBotX1LinkId.WAIST_MOTOR_B,
        AgiBotX1LinkId.WAIST_MOTOR_B_BALL,
        (
            (-0.0650000000000492, 0.0, -0.0108000000000005),
            (3.14159265358979, 1.5707963267949, 0.0),
        ),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.WAIST_MOTOR_B_LOOP: (
        "waist_motor_b_loop_joint",
        "fixed",
        AgiBotX1LinkId.WAIST_MOTOR_B_BALL,
        AgiBotX1LinkId.WAIST_MOTOR_B_LOOP,
        ((0.0, -0.0749999999999924, 0.0), (0.0, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEFT_HIP_PITCH: (
        "left_hip_pitch_joint",
        "revolute",
        AgiBotX1LinkId.BASE,
        AgiBotX1LinkId.LEFT_HIP_PITCH,
        ((0.00245, 0.092277, -0.012143), (0.0, -0.7854, 1.5708)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.LEFT_HIP_ROLL: (
        "left_hip_roll_joint",
        "revolute",
        AgiBotX1LinkId.LEFT_HIP_PITCH,
        AgiBotX1LinkId.LEFT_HIP_ROLL,
        (
            (0.0, -0.0405000000000076, -0.0589000000000007),
            (1.57079632679491, 0.785398163397451, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.LEFT_HIP_YAW: (
        "left_hip_yaw_joint",
        "revolute",
        AgiBotX1LinkId.LEFT_HIP_ROLL,
        AgiBotX1LinkId.LEFT_HIP_YAW,
        ((0.0, -0.0838049159474928, -0.0406000000000136), (1.5707963267949, 0.0, 0.0)),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 50.0, 24.0),
    ),
    AgiBotX1JointId.LEFT_KNEE_PITCH: (
        "left_knee_pitch_joint",
        "revolute",
        AgiBotX1LinkId.LEFT_HIP_YAW,
        AgiBotX1LinkId.LEFT_KNEE_PITCH,
        (
            (-0.0337000000000097, 0.0, 0.142200000000001),
            (-1.57079632679488, 0.0, -1.5707963267949),
        ),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.LEFT_ANKLE_PITCH: (
        "left_ankle_pitch_joint",
        "revolute",
        AgiBotX1LinkId.LEFT_KNEE_PITCH,
        AgiBotX1LinkId.LEFT_ANKLE_PITCH,
        (
            (0.0, -0.304939999999997, 0.0336000000000411),
            (-3.14159265358979, 0.0, 3.14159265358979),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 80.0, 10.0),
    ),
    AgiBotX1JointId.LEFT_ANKLE_ROLL: (
        "left_ankle_roll_joint",
        "revolute",
        AgiBotX1LinkId.LEFT_ANKLE_PITCH,
        AgiBotX1LinkId.LEFT_ANKLE_ROLL,
        ((0.0, 0.0, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 80.0, 10.0),
    ),
    AgiBotX1JointId.LEG_L_TOE_A_LINK: (
        "leg_l_toe_a_link_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_KNEE_PITCH,
        AgiBotX1LinkId.LEG_L_TOE_A,
        (
            (0.0198500000000011, -0.109961932116273, 0.0336568378288508),
            (0.0, -1.5707963267949, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEG_L_TOE_A_BALL: (
        "leg_l_toe_a_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEG_L_TOE_A,
        AgiBotX1LinkId.LEG_L_TOE_A_BALL,
        (
            (-0.0233806454082247, 0.00902193211627456, -0.0211500000000038),
            (0.0, 0.0, 0.0),
        ),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_L_TOE_A_LOOP: (
        "leg_l_toe_a_loop_joint",
        "fixed",
        AgiBotX1LinkId.LEG_L_TOE_A_BALL,
        AgiBotX1LinkId.LEG_L_TOE_A_LOOP,
        ((0.0, -0.195, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_L_TOE_B_LINK: (
        "leg_l_toe_b_link_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_KNEE_PITCH,
        AgiBotX1LinkId.LEG_L_TOE_B,
        (
            (0.0198499999999967, -0.164961932116271, 0.0335431621711256),
            (0.0, -1.5707963267949, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEG_L_TOE_B_BALL: (
        "leg_l_toe_b_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEG_L_TOE_B,
        AgiBotX1LinkId.LEG_L_TOE_B_BALL,
        (
            (0.0233806454082588, 0.00902193211627189, -0.0211500000000081),
            (0.0, 0.0, 0.0),
        ),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_L_TOE_B_LOOP: (
        "leg_l_toe_b_loop_joint",
        "fixed",
        AgiBotX1LinkId.LEG_L_TOE_B_BALL,
        AgiBotX1LinkId.LEG_L_TOE_B_LOOP,
        ((0.0, -0.14, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.RIGHT_HIP_PITCH: (
        "right_hip_pitch_joint",
        "revolute",
        AgiBotX1LinkId.BASE,
        AgiBotX1LinkId.RIGHT_HIP_PITCH,
        ((0.00245, -0.092277, -0.012143), (0.0, -0.7854, -1.5708)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.RIGHT_HIP_ROLL: (
        "right_hip_roll_joint",
        "revolute",
        AgiBotX1LinkId.RIGHT_HIP_PITCH,
        AgiBotX1LinkId.RIGHT_HIP_ROLL,
        (
            (0.0, 0.0405000000001067, -0.0588999999999981),
            (1.57079632679491, 0.78539816339745, 0.0),
        ),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.RIGHT_HIP_YAW: (
        "right_hip_yaw_joint",
        "revolute",
        AgiBotX1LinkId.RIGHT_HIP_ROLL,
        AgiBotX1LinkId.RIGHT_HIP_YAW,
        (
            (0.0, -0.0777549159474913, 0.0405999999999983),
            (-1.57079632680723, 0.0, 0.00861027512635925),
        ),
        (-0.0, 0.0, 1.0),
        (-3.14, 3.14, 50.0, 24.0),
    ),
    AgiBotX1JointId.RIGHT_KNEE_PITCH: (
        "right_knee_pitch_joint",
        "revolute",
        AgiBotX1LinkId.RIGHT_HIP_YAW,
        AgiBotX1LinkId.RIGHT_KNEE_PITCH,
        (
            (-0.0347752157308957, 0.0, -0.147956063988164),
            (1.57940660192126, 0.0, 1.57079632822694),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 150.0, 8.0),
    ),
    AgiBotX1JointId.RIGHT_ANKLE_PITCH: (
        "right_ankle_pitch_joint",
        "revolute",
        AgiBotX1LinkId.RIGHT_KNEE_PITCH,
        AgiBotX1LinkId.RIGHT_ANKLE_PITCH,
        ((0.0, -0.304939999999999, 0.0335999999999944), (3.14159265358979, 0.0, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 80.0, 10.0),
    ),
    AgiBotX1JointId.RIGHT_ANKLE_ROLL: (
        "right_ankle_roll_joint",
        "revolute",
        AgiBotX1LinkId.RIGHT_ANKLE_PITCH,
        AgiBotX1LinkId.RIGHT_ANKLE_ROLL,
        ((0.0, 0.0, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 80.0, 10.0),
    ),
    AgiBotX1JointId.LEG_R_TOE_A_LINK: (
        "leg_r_toe_a_link_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_KNEE_PITCH,
        AgiBotX1LinkId.LEG_R_TOE_A,
        (
            (-0.0198500000000012, -0.109961932116264, 0.0336568378288726),
            (0.0, 1.5707963267949, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEG_R_TOE_A_BALL: (
        "leg_r_toe_a_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEG_R_TOE_A,
        AgiBotX1LinkId.LEG_R_TOE_A_BALL,
        (
            (0.0233806454082594, 0.00902193211626567, -0.0211499999999971),
            (0.0, 0.0, 0.0),
        ),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_R_TOE_A_LOOP: (
        "leg_r_toe_a_loop_joint",
        "fixed",
        AgiBotX1LinkId.LEG_R_TOE_A_BALL,
        AgiBotX1LinkId.LEG_R_TOE_A_LOOP,
        ((0.0, -0.195000000000005, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_R_TOE_B_LINK: (
        "leg_r_toe_b_link_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_KNEE_PITCH,
        AgiBotX1LinkId.LEG_R_TOE_B,
        (
            (-0.0198500000000051, -0.164961932116276, 0.0335431621711194),
            (0.0, 1.5707963267949, 0.0),
        ),
        (0.0, 0.0, -1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.LEG_R_TOE_B_BALL: (
        "leg_r_toe_b_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEG_R_TOE_B,
        AgiBotX1LinkId.LEG_R_TOE_B_BALL,
        (
            (-0.0233806454082563, 0.00902193211627755, -0.0211499999999931),
            (0.0, 0.0, 0.0),
        ),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.LEG_R_TOE_B_LOOP: (
        "leg_r_toe_b_loop_joint",
        "fixed",
        AgiBotX1LinkId.LEG_R_TOE_B_BALL,
        AgiBotX1LinkId.LEG_R_TOE_B_LOOP,
        ((0.0, -0.14, 0.0), (0.0, 1.5707963267949, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_R_WRIST_A_BALL: (
        "arm_r_wrist_a_ball_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_ELBOW_YAW,
        AgiBotX1LinkId.ARM_R_WRIST_A_BALL,
        ((-0.009, -0.02, -0.0199), (1.5708, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_R_WRIST_MOTOR_A_LINK: (
        "arm_r_wrist_motor_a_link_joint",
        "fixed",
        AgiBotX1LinkId.ARM_R_WRIST_A_BALL,
        AgiBotX1LinkId.ARM_R_WRIST_MOTOR_A,
        ((0.0027628, -0.097124, 0.0), (1.5708, 0.0, 0.028438)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.ARM_R_WRIST_A_LOOP: (
        "arm_r_wrist_a_loop_joint",
        "fixed",
        AgiBotX1LinkId.ARM_R_WRIST_MOTOR_A,
        AgiBotX1LinkId.ARM_R_WRIST_A_LOOP,
        ((0.0, 0.0, 0.0132), (-1.5708, -0.028438, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_R_WRIST_B_BALL: (
        "arm_r_wrist_b_ball_joint",
        "fixed",
        AgiBotX1LinkId.RIGHT_ELBOW_YAW,
        AgiBotX1LinkId.ARM_R_WRIST_B_BALL,
        ((-0.009, 0.02, -0.0199), (-1.5708, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_R_WRIST_MOTOR_B_LINK: (
        "arm_r_wrist_motor_b_link_joint",
        "fixed",
        AgiBotX1LinkId.ARM_R_WRIST_B_BALL,
        AgiBotX1LinkId.ARM_R_WRIST_MOTOR_B,
        ((0.0027628, 0.097124, 0.0), (-1.5708, 0.0, -0.028438)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.ARM_R_WRIST_B_LOOP: (
        "arm_r_wrist_b_loop_joint",
        "fixed",
        AgiBotX1LinkId.ARM_R_WRIST_MOTOR_B,
        AgiBotX1LinkId.ARM_R_WRIST_B_LOOP,
        ((0.0, 0.0, 0.0132), (1.5708, -0.028438, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_L_WRIST_A_BALL: (
        "arm_l_wrist_a_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_ELBOW_YAW,
        AgiBotX1LinkId.ARM_L_WRIST_A_BALL,
        ((-0.009, -0.02, -0.0199), (1.5708, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_L_WRIST_MOTOR_A_LINK: (
        "arm_l_wrist_motor_a_link_joint",
        "fixed",
        AgiBotX1LinkId.ARM_L_WRIST_A_BALL,
        AgiBotX1LinkId.ARM_L_WRIST_MOTOR_A,
        ((0.0027628, -0.097124, 0.0), (1.5708, 0.0, 0.028438)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.ARM_L_WRIST_A_LOOP: (
        "arm_l_wrist_a_loop_joint",
        "fixed",
        AgiBotX1LinkId.ARM_L_WRIST_MOTOR_A,
        AgiBotX1LinkId.ARM_L_WRIST_A_LOOP,
        ((0.0, 0.0, 0.0132), (-1.5708, -0.028438, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_L_WRIST_B_BALL: (
        "arm_l_wrist_b_ball_joint",
        "fixed",
        AgiBotX1LinkId.LEFT_ELBOW_YAW,
        AgiBotX1LinkId.ARM_L_WRIST_B_BALL,
        ((-0.009, 0.02, -0.0199), (-1.5708, 0.0, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
    AgiBotX1JointId.ARM_L_WRIST_MOTOR_B_LINK: (
        "arm_l_wrist_motor_b_link_joint",
        "fixed",
        AgiBotX1LinkId.ARM_L_WRIST_B_BALL,
        AgiBotX1LinkId.ARM_L_WRIST_MOTOR_B,
        ((0.0027628, 0.097124, 0.0), (-1.5708, 0.0, -0.028438)),
        (0.0, 0.0, 1.0),
        (-3.14, 3.14, 0.0, 0.0),
    ),
    AgiBotX1JointId.ARM_L_WRIST_B_LOOP: (
        "arm_l_wrist_b_loop_joint",
        "fixed",
        AgiBotX1LinkId.ARM_L_WRIST_MOTOR_B,
        AgiBotX1LinkId.ARM_L_WRIST_B_LOOP,
        ((0.0, 0.0, 0.0132), (1.5708, -0.028438, 0.0)),
        (0.0, 0.0, 0.0),
        None,
    ),
}
"""URDF-derived joint specifications for the AgiBot X1 robot."""


AGIBOT_X1_LINKAGE = Linkage[AgiBotX1LinkId](
    links={
        link_id: link_from_spec(link_id, spec) for link_id, spec in _LINK_SPECS.items()
    },
)
"""The linkage for the AgiBot X1 robot."""

AGIBOT_X1_ARTICULATION = Articulation[AgiBotX1LinkId, AgiBotX1JointId](
    joints={
        joint_id: joint_from_spec(joint_id, spec)
        for joint_id, spec in _JOINT_SPECS.items()
    },
)
"""The articulation for the AgiBot X1 robot."""

AGIBOT_X1 = Skeleton[AgiBotX1LinkId, AgiBotX1JointId](
    linkage=AGIBOT_X1_LINKAGE,
    articulation=AGIBOT_X1_ARTICULATION,
)
"""The kinematic chain for the AgiBot X1 robot."""
