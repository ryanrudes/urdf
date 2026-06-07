# urdf

`urdf` parses URDF files and turns them into typed Python robot definitions.

The project is split into a small parser, reusable robot construction utilities, and generated robot packages under `src/urdf/robots/`.

## What it provides

- Parse URDF files into a structured in-memory model.
- Generate typed link, joint, linkage, articulation, and skeleton definitions.
- Register built-in and user-defined robots at runtime.
- Keep robot-specific definitions in their own packages under `urdf.robots`.

## Usage

Generate a robot package from a URDF file:

```bash
hatch run dev:generate-robot assets/g1_23dof.urdf src/urdf/robots/models/g1_23dof.py
```

Run the test suite:

```bash
hatch run dev:test
```

Build the documentation:

```bash
hatch run dev:docs-build
```

## Repository layout

- `src/urdf/parser/`: URDF parsing and code generation.
- `src/urdf/robots/`: built-in robot packages, runtime registry, and shared helpers.
- `tests/`: regression coverage for generation and registration behavior.
- `docs/`: MkDocs source files.
