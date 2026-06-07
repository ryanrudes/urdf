# Getting Started

Welcome to **urdf**! This library parses Unified Robot Description Format (URDF) XML files and generates strongly-typed, clean Python definitions. By compiling URDF metadata into static Python code, `urdf` enables full IDE autocompletion, type safety via mypy or pyright, and efficient runtime retrieval.

---

## Installation

`urdf` requires **Python 3.12 or newer**. You can install the package directly from your repository:

```bash
# Clone the repository
git clone https://github.com/ryanrudes/urdf.git
cd urdf

# Install with development dependencies
pip install -e .
```

If you are using the [Hatch](https://hatch.pypa.io/) environment manager (configured in `pyproject.toml`), you can invoke development tasks directly:

```bash
hatch run dev:test
```

---

## Core Workflow: URDF Code Generation

The primary feature of `urdf` is translating raw XML URDF files into strongly-typed Python modules containing enums and class definitions for the robot's links, joints, and kinematic chains.

### 1. Generating a Single Robot Model

You can generate a Python definition using the Command Line Interface (CLI):

```bash
python -m urdf.cli path/to/robot.urdf path/to/output.py --class-prefix MyRobot --constant-prefix MY_ROBOT
```

Or, using the Hatch environment shortcut:

```bash
hatch run dev:generate-robot path/to/robot.urdf path/to/output.py --class-prefix MyRobot --constant-prefix MY_ROBOT
```

#### CLI Parameters

| Option | Type | Description |
| :--- | :--- | :--- |
| `urdf` | Positional | Path to the input `.urdf` file. |
| `output` | Positional | Path to the output `.py` destination. |
| `--class-prefix` | Optional | Prefix for generated classes (e.g. `AgiBotX1`). Defaults to a PascalCase version of the URDF name. |
| `--constant-prefix` | Optional | Prefix for generated constants (e.g. `AGIBOT_X1`). Defaults to an UPPER_SNAKE_CASE version of the class prefix. |
| `--sync` | Flag | Synchronize all assets from the configured directory (see below). |

---

### 2. Synchronizing Predefined Workspace Models

The repository contains a folder named `assets/` containing URDF models along with an `assets/robots.json` metadata index. 

You can synchronize all these models simultaneously, which automatically exports the python code into the `src/urdf/robots/models/` directory and updates the central registry:

```bash
python -m urdf.cli --sync
# OR
hatch run dev:sync-robots
```

#### What happens during synchronization?
1. The parser processes all `.urdf` files in `assets/`.
2. The code generator resolves class and constant prefixes from `assets/robots.json`.
3. It exports code for each model under `src/urdf/robots/models/`.
4. It regenerates `src/urdf/robots/models/__init__.py` to import and export these models.
5. It regenerates the central `src/urdf/robots/registry.py` and `src/urdf/robots/__init__.py` modules, making the new robots instantly discoverable through the runtime lookup APIs.

---

## Next Steps

Now that you know how to compile your URDF assets, proceed to the next tutorials to start using the compiled definitions in your code:

- Learn how to inspect links, joints, and kinematic chains in the [Working with Skeletons](./working_with_skeletons.md) tutorial.
- Learn how to dynamically register user-defined robots in the [Custom Robots](./custom_robots.md) tutorial.
