from typing import Literal

import numpy as np

from scipy.spatial.transform import RigidTransform as ScipyRigidTransform


RigidTransform = ScipyRigidTransform
"""A rigid transformation in 3D space, representing rotation and translation.

See `scipy.spatial.transform.RigidTransform` in the
[SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.RigidTransform.html).
"""

type Vec2 = np.ndarray[tuple[Literal[2]], np.dtype[np.floating]]
"""A 2-dimensional floating-point vector."""

type Vec3 = np.ndarray[tuple[Literal[3]], np.dtype[np.floating]]
"""A 3-dimensional floating-point vector."""

type Vec4 = np.ndarray[tuple[Literal[4]], np.dtype[np.floating]]
"""A 4-dimensional floating-point vector."""

type Vec6 = np.ndarray[tuple[Literal[6]], np.dtype[np.floating]]
"""A 6-dimensional floating-point vector."""

type Mat3 = np.ndarray[tuple[Literal[3], Literal[3]], np.dtype[np.floating]]
"""A 3x3 floating-point matrix."""

type Mat4 = np.ndarray[tuple[Literal[4], Literal[4]], np.dtype[np.floating]]
"""A 4x4 floating-point matrix."""
