# Working with Skeletons

Once you have generated a robot definition, it is compiled into a `Skeleton` object. A `Skeleton` contains the entire structure of the robot—its linkage (rigid bodies) and its articulation (moveable joints).

This tutorial demonstrates how to import built-in robot models, query their physical and structural properties, and traverse their kinematic chains in a type-safe manner.

---

## Importing Built-in Models

All synchronized robot models are available for import from `urdf.robots`. The package exports both the runtime constants (such as `AGIBOT_X1`) and their associated identifier types:

```python
from urdf.robots import (
    AGIBOT_X1,         # Skeleton instance
    AgiBotX1LinkId,    # LinkId enum
    AgiBotX1JointId,   # JointId enum
)
```

---

## Skeletons, Linkages, and Articulations

A `Skeleton` is defined as:

```python
class Skeleton[LinkIdT: LinkId, JointIdT: JointId]:
    linkage: Linkage[LinkIdT]
    articulation: Articulation[LinkIdT, JointIdT]
```

- **`linkage`**: Holds the rigid bodies (`Link` objects) of the robot.
- **`articulation`**: Holds the moveable connections (`Joint` objects) connecting those links.

---

## 1. Inspecting Links and Calculating Robot Mass

A `Link` contains the physical properties of a rigid body: its name, mass, inertial origin, and inertia tensor.

Let's write a script to calculate the total mass of the `AgiBot X1` robot and list all its links:

```python
import numpy as np
from urdf.robots import AGIBOT_X1, AgiBotX1LinkId

# 1. Accessing a specific link using typed enums (fully autocompleted in IDEs!)
pelvis_link = AGIBOT_X1.linkage[AgiBotX1LinkId.PELVIS]
print(f"Pelvis Mass: {pelvis_link.mass} kg")
print(f"Pelvis Center of Mass Translation: {pelvis_link.origin.translation} meters")

# 2. Calculating the total mass of the robot
total_mass = sum(link.mass for link in AGIBOT_X1.linkage.links.values())
print(f"\nTotal Robot Mass: {total_mass:.3f} kg")

# 3. Iterating through all links and listing their names
print("\nLinks in AgiBot X1:")
for link_id, link in AGIBOT_X1.linkage.links.items():
    print(f" - {link_id.name}: {link.name} (Mass: {link.mass:.3f} kg)")
```

---

## 2. Traversing Joints and Inspecting Kinematics

A `Joint` connects a `parent` link to a `child` link. The `Skeleton` provides convenient methods to query these connected link objects directly:

- `skeleton.parent_link(joint)`
- `skeleton.child_link(joint)`

Let's write a script that traverses all joints, prints their names, types, and the names of the links they connect:

```python
from urdf.robots import AGIBOT_X1

print("AgiBot X1 Kinematic Connections:")
for joint_id, joint in AGIBOT_X1.articulation.joints.items():
    # Retrieve the parent and child Link objects
    parent_link = AGIBOT_X1.parent_link(joint)
    child_link = AGIBOT_X1.child_link(joint)
    
    print(f"Joint: {joint.name} (Type: {joint.type.value})")
    print(f"  Connects: {parent_link.name} -> {child_link.name}")
```

---

## 3. Querying Joint Types and Position Limits

Joints can be subclassed into specific types (e.g. `FixedJoint`, `RevoluteJoint`, `ContinuousJoint`, `PrismaticJoint`). Bounded joints (like `RevoluteJoint` and `PrismaticJoint`) have a `.limits` attribute containing effort, velocity, and lower/upper bounds.

Let's find all revolute joints in the robot and print their angular limits (expressed in radians):

```python
from urdf.kinematics import RevoluteJoint
from urdf.robots import AGIBOT_X1

print("Actuated Revolute Joints and Limits:")
for joint_id, joint in AGIBOT_X1.articulation.joints.items():
    # Check if the joint is a RevoluteJoint
    if isinstance(joint, RevoluteJoint):
        limits = joint.limits
        # Convert bounds to degrees for readability
        lower_deg = np.degrees(limits.lower)
        upper_deg = np.degrees(limits.upper)
        
        print(f" - {joint.name}:")
        print(f"   Limits: [{lower_deg:.1f}°, {upper_deg:.1f}°]")
        print(f"   Max Velocity: {limits.velocity:.1f} rad/s")
        print(f"   Max Effort: {limits.effort:.1f} N·m")
```

---

## 4. Exploiting Static Type Safety

Because `urdf` is built with generic types, your type checker can catch errors at write-time.

```python
from urdf.robots import AGIBOT_X1, AgiBotX1LinkId, UnitreeG1_23DOFLinkId

# This compiles perfectly:
agibot_pelvis = AGIBOT_X1.linkage[AgiBotX1LinkId.PELVIS]

# This will trigger an error in your IDE/Mypy, preventing runtime KeyErrors:
# "Argument 1 to __getitem__ has incompatible type 'UnitreeG1_23DOFLinkId'; expected 'AgiBotX1LinkId'"
invalid_lookup = AGIBOT_X1.linkage[UnitreeG1_23DOFLinkId.PELVIS]
```

This safety extends to functions you write:

```python
from urdf.robots import AgiBotX1Robot

def analyze_agibot_pelvis(robot: AgiBotX1Robot) -> None:
    # Mypy knows pelvis_link is a Link[AgiBotX1LinkId]
    pelvis_link = robot.linkage[AgiBotX1LinkId.PELVIS]
    print(pelvis_link.mass)
```
