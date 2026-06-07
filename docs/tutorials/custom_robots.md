# Custom Robots and the Runtime Registry

While `urdf` simplifies parsing and compiling static robot models from URDF files, you may also need to work with robot models dynamically. The library includes a **runtime robot registry** that lets you register, retrieve, and unregister robot definitions in memory.

This is particularly useful when loading user-uploaded robots, generating modular robot variations, or storing virtual robot instances in simulation environments.

---

## The Registry API

The `urdf.robots` module exports a set of functions to manage the runtime registry:

- **`register_robot(robot, replace=False)`**: Adds a new robot to the registry.
- **`get_robot(robot_id)`**: Retrieves a registered `Robot` by its string ID.
- **`get_skeleton(robot_id)`**: Conveniently retrieves just the `Skeleton` of a registered robot.
- **`registered_robot_ids()`**: Returns a `frozenset[str]` of all currently registered robot IDs.
- **`unregister_robot(robot_id, allow_builtin=False)`**: Removes a robot from the registry.

---

## 1. Querying Registered Robots

All built-in robots (like `Unitree G1`, `H1`, `AgiBot X1`, etc.) are automatically registered at runtime under their lowercase IDs.

You can inspect all registered robots using the following script:

```python
from urdf.robots import registered_robot_ids, get_robot

# Get all registered IDs
all_ids = registered_robot_ids()
print(f"Registered Robots: {sorted(list(all_ids))}")

# Retrieve a specific robot by string ID
robot = get_robot("unitree_h1")
print(f"Robot Name: {robot.name}")
print(f"Robot ID: {robot.id}")
print(f"Skeleton Links count: {len(robot.skeleton.linkage.links)}")
```

---

## 2. Registering a Custom Robot

To register a custom robot, you construct a `Robot` object. A `Robot` needs:
1. A unique string identifier (`id`).
2. A human-readable `name`.
3. A `Skeleton` instance (which contains the robot's links and joints).

You can reuse an existing skeleton (as a base) or build one manually. Here is how to register a custom robot variant:

```python
from urdf.robots import (
    Robot,
    register_robot,
    get_robot,
    registered_robot_ids,
    UNITREE_G1_23DOF,  # Built-in skeleton
)

# 1. Create a custom robot definition using the G1 skeleton as its kinematic chain
my_custom_robot = Robot(
    id="my_custom_g1",
    name="My Modular G1 Variant",
    skeleton=UNITREE_G1_23DOF,
)

# 2. Register it
register_robot(my_custom_robot)

# 3. Check that it is registered
if "my_custom_g1" in registered_robot_ids():
    print("Successfully registered my_custom_g1!")

# 4. Retrieve and verify the robot
retrieved_robot = get_robot("my_custom_g1")
print(f"Retrieved Name: {retrieved_robot.name}")
```

---

## 3. Handling Duplicates and Replacing Definitions

By default, trying to register a robot with an ID that is already in use will raise a `ValueError` to prevent accidental overwrites. To replace an existing definition, set `replace=True`:

```python
from urdf.robots import Robot, register_robot, UNITREE_G1_23DOF

original = Robot(id="temp_robot", name="Original Version", skeleton=UNITREE_G1_23DOF)
duplicate = Robot(id="temp_robot", name="Updated Version", skeleton=UNITREE_G1_23DOF)

# Register the original
register_robot(original)

# This raises: ValueError: A robot is already registered for 'temp_robot'.
try:
    register_robot(duplicate)
except ValueError as exc:
    print(f"Prevented duplicate: {exc}")

# Overwrite it explicitly
register_robot(duplicate, replace=True)
print("Successfully replaced the robot definition!")
```

---

## 4. Unregistering Robots

To clean up resources or remove temporary robots, use `unregister_robot`:

```python
from urdf.robots import unregister_robot, registered_robot_ids

# Unregister our temporary robot
removed_robot = unregister_robot("temp_robot")
print(f"Removed: {removed_robot.name}")

# Verify it's gone
assert "temp_robot" not in registered_robot_ids()
```

### Safety: Protecting Built-in Models

To prevent code from accidentally disabling built-in robots, trying to unregister a built-in robot (like `unitree_g1_23dof`) will fail by default:

```python
from urdf.robots import unregister_robot, RobotId

# This raises: ValueError: Cannot unregister built-in robot 'unitree_g1_23dof'.
try:
    unregister_robot(RobotId.UNITREE_G1_23DOF)
except ValueError as exc:
    print(f"Built-in protection: {exc}")

# If you absolutely must remove a built-in robot, set allow_builtin=True:
# unregister_robot(RobotId.UNITREE_G1_23DOF, allow_builtin=True)
```
