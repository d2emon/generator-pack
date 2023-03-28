"""Base point model."""
import math
import random
from .model import Model


class Point(Model):
    """Model with x and y

    Attributes:
        field_names (Collection): Field names.
        x: (float): Point x value.
        y: (float): Point y value.
    """

    field_names = [
        'x',
        'y',
    ]

    x = Model.field_property('x')
    y = Model.field_property('y')

    def __init__(self, x, y):
        """Initialize model.

        Args:
            x (float): Point x value.
            y (float): Point y value.
        """
        super().__init__(x=x, y=y)

    @property
    def length(self) -> float:
        """Get distance from start.

        Returns:
            float: Distance from start.
        """
        return math.sqrt(self.x ^ 2 + self.y ^ 2)

    @property
    def angle(self) -> float:
        """Get angle from start.

        Returns:
            float: Angle from start.
        """
        return math.atan(self.y / self.x)

    def rotate(self, angle: float) -> Model:
        """Rotate point by angle.

        Args:
            angle (float): Angle to rotate.

        Returns:
            Point: Rotated point.
        """
        return self.polar(
            self.length,
            self.angle + angle,
        )

    @classmethod
    def polar(cls, radius: float, angle: float) -> Model:
        """Get point by polar coordinates.

        Args:
            radius (float): Point radius
            angle (float): Point angle.

        Returns:
            Point: New point.
        """
        return cls(
            radius * math.cos(angle),
            radius * math.sin(angle),
        )

    @classmethod
    def between(cls, point1: Model, point2: Model) -> Model:
        """Get middle point between two points.

        Args:
            point1 (Point): First point.
            point2 (Point): Second point.

        Returns:
            Point: Point in the middle
        """
        return cls(
            int((point1.x + point2.x) / 2),
            int((point1.y + point2.y) / 2),
        )

    @classmethod
    def diffuse(cls, point1: Model, point2: Model) -> Model:
        """Get random point between two points.

        Args:
            point1 (Point): First point.
            point2 (Point): Second point.

        Returns:
            Point: Point in the middle
        """
        percent = random.uniform(100)
        dx = point2.x - point1.x
        dy = point2.y - point1.y
        return cls(
            int(point1.x + percent * dx),
            int(point1.y + percent * dy),
        )
