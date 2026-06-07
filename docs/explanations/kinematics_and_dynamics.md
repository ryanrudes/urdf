# Kinematics & Dynamics

This page explains the physical models, coordinate transforms, and mathematical representations used by the **urdf** library.

---

## Units of Measure

The library strictly adheres to the standard **SI Units** for all kinematic and dynamic quantities. Below is a summary of the units used:

| Quantity | Rotational Joint (Revolute / Continuous) | Translational Joint (Prismatic) |
| :--- | :--- | :--- |
| **Position / Limit** | Radians [rad] | Meters [m] |
| **Velocity Limit** | Radians per second [rad/s] | Meters per second [m/s] |
| **Effort Limit** | Newton-meters [N·m] | Newtons [N] |
| **Damping** | Newton-meter-seconds per radian [N·m·s/rad] | Newton-seconds per meter [N·s/m] |
| **Friction** | Newton-meters [N·m] | Newtons [N] |
| **Mass** | *N/A* | Kilograms [kg] |
| **Inertia** | *N/A* | Kilogram-square meters [kg·m²] |

---

## Coordinate Frames & Rigid Transforms

Every link and joint in a robot skeleton defines its own coordinate frame. In URDF:

* A **Joint Origin** defines the transform from the **parent link frame** to the **joint frame**.
* The **child link frame** is coincident with the joint frame (unless a child offset is explicitly modeled).
* A **Link Inertial Origin** defines the transform from the **link frame** to the **link's Center of Mass (CoM) frame**.

```
  [Parent Link Frame]
          │
          ▼  (Joint Origin Transform)
    [Joint Frame]  ===  [Child Link Frame]
                              │
                              ▼  (Link Inertial Origin)
                        [Link CoM Frame]
```

### RigidTransform Class

To represent these spatial relationships, `urdf` re-exports `scipy.spatial.transform.RigidTransform`.

A `RigidTransform` represents a combined rotation and translation. You can inspect or build them as follows:

```python
from urdf.core.types import RigidTransform
import numpy as np
from scipy.spatial.transform import Rotation

# 1. Inspecting translation and rotation components
translation = transform.translation  # 3-element numpy array
rotation = transform.rotation        # scipy Rotation object

# 2. Creating a transform from translation and rotation components
transform = RigidTransform.from_components(
    translation=np.array([0.1, 0.0, 0.5]),
    rotation=Rotation.from_euler("xyz", [0.0, np.pi/4, 0.0])
)
```

---

## Inertia Tensors

An inertia tensor describes a rigid body's resistance to rotational acceleration about its center of mass. Mathematically, it is represented as a symmetric 3x3 matrix:

$$
\mathbf{I} = \begin{bmatrix} 
I_{xx} & I_{xy} & I_{xz} \\ 
I_{xy} & I_{yy} & I_{yz} \\ 
I_{xz} & I_{yz} & I_{zz} 
\end{bmatrix}
$$

* **Moments of Inertia** ($I_{xx}, I_{yy}, I_{zz}$): Quantify resistance to rotation about the principal x, y, and z axes.
* **Products of Inertia** ($I_{xy}, I_{xz}, I_{yz}$): Represent the mass distribution skewness relative to coordinate planes.

### InertiaTensor Class

The `InertiaTensor` class (`urdf.dynamics.InertiaTensor`) wraps this tensor. It represents the moments and products internally as two 3-element NumPy arrays to optimize storage.

```python
from urdf.dynamics import InertiaTensor
import numpy as np

# Create a tensor from raw moment and product arrays
moments = np.array([0.05, 0.06, 0.03])
products = np.array([0.001, -0.002, 0.0])
tensor = InertiaTensor(moments=moments, products=products)
```

### Creating Tensors

`InertiaTensor` provides several classmethods for flexible instantiation:

```python
# 1. From individual scalar entries (standard URDF format)
tensor = InertiaTensor.from_entries(
    ixx=0.01, ixy=0.0, ixz=0.0,
    iyy=0.01, iyz=0.0,
    izz=0.02
)

# 2. From a 3x3 inertia matrix
matrix = np.array([
    [0.05, 0.01, 0.0],
    [0.01, 0.05, 0.0],
    [0.0,  0.0,  0.08]
])
tensor = InertiaTensor.from_matrix(matrix)

# 3. From Voigt notation (6-element vector)
# Order: [ixx, iyy, izz, iyz, ixz, ixy]
voigt_vector = np.array([0.05, 0.05, 0.08, 0.0, 0.0, 0.01])
tensor = InertiaTensor.from_voigt(voigt_vector)
```

### Exporting Formats

You can export the tensor back into standard matrix or Voigt vector forms:

```python
# Export as a 3x3 symmetric matrix
matrix_representation = tensor.as_matrix()

# Export as a Voigt vector (numpy array of shape (6,))
voigt_vector = tensor.as_voigt()
```

---

## Joint Dynamics & Limits

Different joint types impose different constraints on the child link's degrees of freedom. Bounded joints inherit from `JointPositionLimits`, which adds scalar ranges:

### Joint Types Summary

| Joint Type Class | Actuation Degrees of Freedom | Bounded Limits? | Description |
| :--- | :--- | :--- | :--- |
| **`FixedJoint`** | 0 | No | Rigidly connects parent and child frames. |
| **`RevoluteJoint`** | 1 (Rotation) | **Yes** | Hinge joint rotating around a specified axis with lower/upper limit bounds. |
| **`ContinuousJoint`** | 1 (Rotation) | No | Continuous hinge joint rotating infinitely around an axis. |
| **`PrismaticJoint`** | 1 (Translation) | **Yes** | Sliding joint moving along an axis with lower/upper limit bounds. |
| **`PlanarJoint`** | 2 (Translation) | No | Allows motion in a plane perpendicular to the joint axis. |
| **`FloatingJoint`** | 6 (Rotation + Translation) | No | Unconstrained 6-DoF relative motion. |

### Limit Classes

* **`JointEffortLimits`**: Stores the absolute maximum force/torque (`effort`) and speed (`velocity`) constraints of a joint. Used for continuous joints.
* **`JointPositionLimits`**: Subclasses `JointEffortLimits` and adds `lower` and `upper` position bounds. Used for revolute and prismatic joints.
