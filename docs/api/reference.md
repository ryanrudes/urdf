# API Reference

This page provides the complete API reference for all public classes, functions, and types in the `urdf` library.

---

## Core Types

The `urdf.core.types` module provides coordinate transformation classes and NumPy array aliases for vector and matrix typing.

::: urdf.core.types
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Dynamics

The `urdf.dynamics.inertia` module contains representation models for rigid body physical properties, notably inertia tensors.

::: urdf.dynamics.inertia
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Kinematics

The `urdf.kinematics.kinematic_chain` module defines the core skeleton structure, linkage, articulation, and various joint subclasses.

::: urdf.kinematics.kinematic_chain
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Parser & Code Generation

The `urdf.parser` module parses URDF XML descriptions and exports them as generated code.

::: urdf.parser
    options:
      show_root_heading: true
      show_root_toc_entry: true

::: urdf.parser.codegen
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Built-in Robots

The `urdf.robots` module exposes all built-in robot model definitions and their corresponding identifier classes.

::: urdf.robots
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Robot Registry

The `urdf.robots.registry` module manages runtime lookup and custom robot registration.

::: urdf.robots.registry
    options:
      show_root_heading: true
      show_root_toc_entry: true

---

## Robot Construction Utilities

The `urdf.robots.utils` module provides shared conversion helpers that inflate specifications into runtime kinematic objects.

::: urdf.robots.utils
    options:
      show_root_heading: true
      show_root_toc_entry: true
