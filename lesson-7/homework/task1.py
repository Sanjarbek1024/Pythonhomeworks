class Vector:
    def __init__(self, *components):
        """Initialize a vector with given components. Accepts any number of dimensions."""
        self.components = components  # Store components as a tuple

    def __repr__(self):
        """String representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        """Add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to be added.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """Subtract two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to be subtracted.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """Define multiplication: dot product or scalar multiplication."""
        if isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Vector' and '{type(other).__name__}'")

    def __rmul__(self, other):
        """Allow scalar multiplication from the left."""
        return self.__mul__(other)

    def magnitude(self):
        """Calculate the magnitude (Euclidean norm) of the vector."""
        return sum(x ** 2 for x in self.components) ** 0.5  # Square root of the sum of squares
    def normalize(self):
        """Normalize the vector (return a unit vector)."""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(x / magnitude for x in self.components))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)  # Output: Vector(1, 2, 3)

v3 = v1 + v2
print(v3)  # Output: Vector(5, 7, 9)

v4 = v2 - v1
print(v4)  # Output: Vector(3, 3, 3)

dot_product = v1 * v2
print(dot_product)  # Output: 32

v5 = 3 * v1
print(v5)  # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)