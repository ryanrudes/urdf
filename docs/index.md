# urdf

`urdf` parses URDF files and generates typed Python robot definitions.

---

<p align="center">
  <code style="font-size: 1.2em;">URDF parsing &rarr; Strongly-typed Python model code</code>
</p>

---

## Why use `urdf`?

* 🛡️ **Compile-time Safety**: Shift coordinate name lookups and joint traversals from runtime string dictionary lookups to static `StrEnum` subclass checks.
* ⚡ **Zero-Overhead Specs**: Keep layout models extremely lightweight in memory using static tuple specifications (`LinkSpec`, `JointSpec`).
* 🧩 **Runtime Registry**: Register, query, and modify user-defined and built-in robot skeletons at runtime.
* 🤖 **Humanoid-Ready**: Comes with built-in configurations for Unitree G1, H1, AgiBot X1, and Booster T1 models.

---

## Documentation Structure

Our documentation is organized into three main sections:

### 🏁 Tutorials
Step-by-step guides to get you up and running:

* **[Getting Started](tutorials/getting_started.md)**: Install the library and run URDF code generation.
* **[Working with Skeletons](tutorials/working_with_skeletons.md)**: Traverse links/joints and query inertial properties.
* **[Custom Robots](tutorials/custom_robots.md)**: Manage custom robots at runtime using the registry.

### 💡 Explanations
Deeper mathematical and architectural design details:

* **[Architecture & Design](explanations/architecture.md)**: Understand the AST compiler pipeline and runtime model layouts.
* **[Kinematics & Dynamics](explanations/kinematics_and_dynamics.md)**: Review physical coordinate frames, SI units, and inertia tensor representations.

### 📚 API Reference
Complete index of the code symbols:

* **[Full Reference](api/reference.md)**: Detailed signatures and docstrings of all package modules.

---

## Quick Command Reference

Here are the common commands to run development environments using Hatch:

```bash
# Generate a Python robot definition from a URDF file
hatch run dev:generate-robot assets/g1_23dof.urdf src/urdf/robots/models/g1_23dof.py

# Synchronize all workspace models in assets/ with the generator
hatch run dev:sync-robots

# Run formatting, checks, and unit tests
hatch run dev:format
hatch run dev:lint
hatch run dev:test
```
