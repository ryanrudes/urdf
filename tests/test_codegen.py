from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType

from urdf.parser import export_robot_definition_code, write_robot_definition_code

ROOT = Path(__file__).parents[1]


class CodegenTests(unittest.TestCase):
    def test_g1_module_is_current_generator_output(self) -> None:
        generated_path = ROOT / "src/urdf/robots/models/g1_23dof.py"
        generated_source = export_robot_definition_code(ROOT / "assets/g1_23dof.urdf")

        self.assertEqual(generated_source, generated_path.read_text())
        self.assertIn(
            "class UnitreeG1_23DOFLinkId(LinkId):\n"
            '    """Link identifiers for the Unitree G1 23-DOF robot."""',
            generated_source,
        )
        self.assertIn('"""The right shoulder roll link."""', generated_source)
        self.assertIn("from urdf.robots.utils import (", generated_source)
        self.assertNotIn("def _transform(", generated_source)
        self.assertNotIn("def _joint(", generated_source)

    def test_unknown_identifiers_get_literal_fallback_docstrings(self) -> None:
        source = _generate_temporary_module(
            """\
<robot name="example">
  <link name="right_shoulder_roll"/>
  <link name="unidentified_payload"/>
  <joint name="mystery_mount" type="fixed">
    <parent link="right_shoulder_roll"/>
    <child link="unidentified_payload"/>
  </joint>
</robot>
""",
            class_prefix="Example",
            constant_prefix="EXAMPLE",
        )

        self.assertIn('"""The right shoulder roll link."""', source)
        self.assertIn('"""Link with ID unidentified_payload."""', source)
        self.assertIn('"""Joint with ID mystery_mount."""', source)

    def test_generation_fails_without_robots_json_entry(self) -> None:
        with self.assertRaisesRegex(ValueError, "Robot metadata not found for 'robot'"):
            _generate_temporary_module(
                """\
<robot name="example">
  <link name="root"/>
</robot>
"""
            )

    def test_generated_module_supports_each_urdf_joint_type(self) -> None:
        source = _generate_temporary_module(
            """\
<robot name="joint_types">
  <link name="root"/>
  <link name="fixed_child"/>
  <link name="floating_child"/>
  <link name="revolute_child"/>
  <link name="continuous_child"/>
  <link name="prismatic_child"/>
  <link name="planar_child"/>
  <joint name="fixed_mount" type="fixed">
    <parent link="root"/><child link="fixed_child"/>
  </joint>
  <joint name="floating_mount" type="floating">
    <parent link="root"/><child link="floating_child"/>
  </joint>
  <joint name="revolute_mount" type="revolute">
    <parent link="root"/><child link="revolute_child"/>
    <axis xyz="0 0 1"/>
    <limit lower="-1" upper="1" effort="2" velocity="3"/>
  </joint>
  <joint name="continuous_mount" type="continuous">
    <parent link="root"/><child link="continuous_child"/>
    <axis xyz="0 1 0"/>
    <limit effort="2" velocity="3"/>
  </joint>
  <joint name="prismatic_mount" type="prismatic">
    <parent link="root"/><child link="prismatic_child"/>
    <axis xyz="1 0 0"/>
    <limit lower="-1" upper="1" effort="2" velocity="3"/>
  </joint>
  <joint name="planar_mount" type="planar">
    <parent link="root"/><child link="planar_child"/>
    <axis xyz="0 0 1"/>
  </joint>
</robot>
""",
            class_prefix="JointTypes",
            constant_prefix="JOINT_TYPES",
        )

        with TemporaryDirectory() as directory:
            module_path = Path(directory) / "joint_types.py"
            module_path.write_text(source)
            module = _load_module(module_path)

        joint_types = {
            type(joint).__name__
            for joint in module.JOINT_TYPES_ARTICULATION.joints.values()
        }
        self.assertEqual(
            joint_types,
            {
                "ContinuousJoint",
                "FixedJoint",
                "FloatingJoint",
                "PlanarJoint",
                "PrismaticJoint",
                "RevoluteJoint",
            },
        )


def _generate_temporary_module(
    urdf: str,
    class_prefix: str | None = None,
    constant_prefix: str | None = None,
) -> str:
    with TemporaryDirectory() as directory:
        urdf_path = Path(directory) / "robot.urdf"
        output_path = Path(directory) / "robot.py"
        urdf_path.write_text(urdf)
        write_robot_definition_code(
            urdf_path,
            output_path,
            class_prefix=class_prefix,
            constant_prefix=constant_prefix,
        )
        return output_path.read_text()


def _load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("generated_joint_types", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load generated module {path}.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
