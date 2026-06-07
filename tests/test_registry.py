from __future__ import annotations

import unittest

from urdf.robots import (
    Robot,
    RobotId,
    UNITREE_G1_23DOF,
    get_robot,
    get_skeleton,
    register_robot,
    registered_robot_ids,
    unregister_robot,
)


class RegistryTests(unittest.TestCase):
    def tearDown(self) -> None:
        if "custom_g1" in registered_robot_ids():
            unregister_robot("custom_g1")

    def test_registers_and_removes_user_defined_robot(self) -> None:
        robot = Robot(
            id="custom_g1",
            name="Custom G1",
            skeleton=UNITREE_G1_23DOF,
        )

        register_robot(robot)

        self.assertIs(get_robot("custom_g1"), robot)
        self.assertIs(get_skeleton("custom_g1"), UNITREE_G1_23DOF)
        self.assertIn("custom_g1", registered_robot_ids())
        self.assertIs(unregister_robot("custom_g1"), robot)

    def test_duplicate_registration_requires_explicit_replacement(self) -> None:
        original = Robot(
            id="custom_g1",
            name="Original",
            skeleton=UNITREE_G1_23DOF,
        )
        replacement = Robot(
            id="custom_g1",
            name="Replacement",
            skeleton=UNITREE_G1_23DOF,
        )
        register_robot(original)

        with self.assertRaisesRegex(ValueError, "already registered"):
            register_robot(replacement)

        register_robot(replacement, replace=True)
        self.assertIs(get_robot("custom_g1"), replacement)

    def test_builtin_robot_cannot_be_unregistered_by_default(self) -> None:
        with self.assertRaisesRegex(ValueError, "built-in robot"):
            unregister_robot(RobotId.UNITREE_G1_23DOF)

        self.assertIs(get_robot(RobotId.UNITREE_G1_23DOF).skeleton, UNITREE_G1_23DOF)

    def test_all_built_in_robots_are_registered(self) -> None:
        import json
        from pathlib import Path

        config_path = Path(__file__).parents[1] / "assets" / "robots.json"
        with config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        expected_robot_ids = {cfg["constant_prefix"].lower() for cfg in data.values()}
        for robot_id in expected_robot_ids:
            with self.subTest(robot_id=robot_id):
                robot = get_robot(robot_id)
                self.assertEqual(robot.id, robot_id)
                self.assertIsNotNone(robot.skeleton)


if __name__ == "__main__":
    unittest.main()
