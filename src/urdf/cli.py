from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from urdf.parser import sync_assets, write_robot_definition_code


def main(argv: Sequence[str] | None = None) -> None:
    """Run the URDF-to-robot-definition exporter from the command line."""
    parser = argparse.ArgumentParser(
        description="Export a Python robot definition from a URDF file."
    )
    parser.add_argument("urdf", type=Path, nargs="?", help="The input URDF file.")
    parser.add_argument("output", type=Path, nargs="?", help="The output Python file.")
    parser.add_argument(
        "--class-prefix",
        help="The generated Python class prefix, such as UnitreeG1_23DOF.",
    )
    parser.add_argument(
        "--constant-prefix",
        help="The generated Python constant prefix, such as UNITREE_G1_23DOF.",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Synchronize all URDF assets with the generated Python definitions and registry.",
    )
    args = parser.parse_args(argv)

    if args.sync:
        sync_assets()
        return

    if args.urdf is None or args.output is None:
        parser.error(
            "the following arguments are required: urdf, output (unless --sync is specified)"
        )

    write_robot_definition_code(
        args.urdf,
        args.output,
        class_prefix=args.class_prefix,
        constant_prefix=args.constant_prefix,
    )


if __name__ == "__main__":
    main()
