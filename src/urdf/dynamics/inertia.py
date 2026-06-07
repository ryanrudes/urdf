from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from urdf.core.types import Vec3, Vec6, Mat3


@dataclass(frozen=True)
class InertiaTensor:
    """An inertia tensor is a 3x3 matrix that describes the inertial properties of a rigid body.

    This link's moments of inertia ixx, iyy, izz and products of inertia ixy, ixz, iyz are expressed about Co
    (the link's center of mass) for the unit vectors Ĉx, Ĉy, Ĉz fixed in the center-of-mass frame C.
    """

    moments: Vec3
    """The moments of inertia (ixx, iyy, izz)."""

    products: Vec3 = field(default_factory=lambda: np.zeros(3))
    """The products of inertia (ixy, ixz, iyz)."""

    @classmethod
    def zero(cls) -> InertiaTensor:
        """Create a zero inertia tensor."""
        return cls(moments=np.zeros(3), products=np.zeros(3))

    @classmethod
    def identity(cls) -> InertiaTensor:
        """Create an identity inertia tensor."""
        return cls(moments=np.ones(3), products=np.zeros(3))

    @classmethod
    def from_entries(
        cls, *, ixx: float, ixy: float, ixz: float, iyy: float, iyz: float, izz: float
    ) -> InertiaTensor:
        """Create an inertia tensor from its entries.

        Args:
            ixx: The moment of inertia about the x-axis.
            ixy: The product of inertia about the x- and y-axes.
            ixz: The product of inertia about the x- and z-axes.
            iyy: The moment of inertia about the y-axis.
            iyz: The product of inertia about the y- and z-axes.
            izz: The moment of inertia about the z-axis.
        """
        return cls(
            moments=np.array([ixx, iyy, izz]), products=np.array([ixy, ixz, iyz])
        )

    @classmethod
    def from_moments(cls, moments: Vec3 | float) -> InertiaTensor:
        """Create an inertia tensor from its moments of inertia.

        Args:
            moments: The moments of inertia (ixx, iyy, izz) or a single float value.
        """
        if isinstance(moments, float):
            moments = np.full((3,), moments)

        return cls(moments=moments, products=np.zeros(3))

    @classmethod
    def from_products(cls, products: Vec3 | float) -> InertiaTensor:
        """Create an inertia tensor from its products of inertia.

        Args:
            products: The products of inertia (ixy, ixz, iyz) or a single float value.
        """
        if isinstance(products, float):
            products = np.full((3,), products)

        return cls(moments=np.zeros(3), products=products)

    @classmethod
    def from_components(
        cls, moments: Vec3 | float, products: Vec3 | float
    ) -> InertiaTensor:
        """Create an inertia tensor from its components.

        Args:
            moments: The moments of inertia (ixx, iyy, izz) or a single float value.
            products: The products of inertia (ixy, ixz, iyz) or a single float value.

        Returns:
            The inertia tensor.
        """
        if isinstance(moments, float):
            moments = np.full((3,), moments)
        if isinstance(products, float):
            products = np.full((3,), products)

        return cls(moments=moments, products=products)

    @classmethod
    def from_matrix(cls, matrix: Mat3) -> InertiaTensor:
        """Create an inertia tensor from an inertia matrix.

        The inertia matrix is expressed in the following form:
        ```
        [ ixx ixy ixz ]
        [ ixy iyy iyz ]
        [ ixz iyz izz ]
        ```
        where ixx, iyy, izz are the moments of inertia and ixy, ixz, iyz are the products of inertia.

        Args:
            matrix: The inertia matrix.

        Returns:
            The inertia tensor.
        """
        moments = np.diag(matrix)
        products = matrix[np.triu_indices(3, k=1)]

        return cls(moments=moments, products=products)

    @classmethod
    def from_voigt(cls, voigt: Vec6) -> InertiaTensor:
        """Create an inertia tensor from its Voigt notation.

        The Voigt notation is expressed in the following form:
        ```
        [ ixx iyy izz iyz ixz ixy ]
        ```
        where ixx, iyy, izz are the moments of inertia and ixy, ixz, iyz are the products of inertia.
        """
        moments = voigt[:3]
        products = voigt[3:][::-1]

        return cls(moments=moments, products=products)

    def as_matrix(self) -> Mat3:
        """Convert the inertia tensor to an inertia matrix.

        The inertia matrix is expressed in the following form:
        ```
        [ ixx ixy ixz ]
        [ ixy iyy iyz ]
        [ ixz iyz izz ]
        ```
        """
        matrix = np.diag(self.moments)
        upper = np.triu_indices(3, k=1)
        matrix[upper] = self.products
        matrix[(upper[1], upper[0])] = self.products
        return matrix

    def as_components(self) -> tuple[Vec3, Vec3]:
        """Convert the inertia tensor to its components vector.

        Returns:
            A tuple of the moments of inertia (ixx, iyy, izz) and the products of inertia (ixy, ixz, iyz).
        """
        return (self.moments, self.products)

    def as_voigt(self) -> Vec6:
        """Convert the inertia tensor to its Voigt notation.

        Returns:
            The Voigt notation of the inertia tensor (ixx, iyy, izz, iyz, ixz, ixy).
        """
        return np.concatenate([self.moments, self.products[::-1]])

    @property
    def ixx(self) -> float:
        """The moment of inertia about the x-axis."""
        return self.moments[0]

    @property
    def iyy(self) -> float:
        """The moment of inertia about the y-axis."""
        return self.moments[1]

    @property
    def izz(self) -> float:
        """The moment of inertia about the z-axis."""
        return self.moments[2]

    @property
    def ixy(self) -> float:
        """The product of inertia about the x- and y-axes."""
        return self.products[0]

    @property
    def ixz(self) -> float:
        """The product of inertia about the x- and z-axes."""
        return self.products[1]

    @property
    def iyz(self) -> float:
        """The product of inertia about the y- and z-axes."""
        return self.products[2]
