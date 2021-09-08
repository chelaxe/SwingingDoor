#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

swinging_door
=============

Implementation of the SwingingDoor algorithm in Python.

"""

from sys import version_info
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from typing import Generator, Tuple

__author__ = "Aleksandr F. Mikhaylov (ChelAxe)"  # type: str
__version__ = "0.1.1"  # type: str
__license__ = "MIT"  # type: str


class Point:
    """
    Point in rectangular coordinate system.
    """

    def __init__(self, abscissa, ordinate):
        # type: (float, float) -> None
        """

        Class constructor specifying the coordinates of the point.

        :param float abscissa: point abscissa;
        :param float ordinate: point ordinate.

        >>> Point(1.0, 2.0)
        Point(1.0, 2.0)

        """

        self.abscissa = abscissa
        self.ordinate = ordinate

    def __call__(self):
        # type: () -> Tuple[float, float]
        """

        A call that returns the coordinates of a point.

        :rtype: Tuple[float, float]
        :return: Point coordinates.

        >>> Point(1.0, 2.0)()
        (1.0, 2.0)

        """

        return self.abscissa, self.ordinate

    def __repr__(self):  # type: () -> str
        """

        Unambiguous textual representation of an object.

        :rtype: str
        :return: Unambiguous textual representation of an object.

        >>> repr(Point(1.0, 2.0))
        'Point(1.0, 2.0)'

        """

        return "Point({abscissa}, {ordinate})".format(
            abscissa=self.abscissa, ordinate=self.ordinate
        )

    def __str__(self):  # type: () -> str
        """

        Natural textual representation of the object.

        :rtype: str
        :return: Natural textual representation of the object.

        >>> str(Point(1.0, 2.0))
        '(1.0, 2.0)'

        """

        return "({abscissa}, {ordinate})".format(
            abscissa=self.abscissa, ordinate=self.ordinate
        )


def swinging_door(
    data,  # type: Generator[Tuple[float, float], None, None]
    deviation=0.1,  # type: float
):
    # type: (...) -> Generator[Tuple[float, float], None, None]
    """

    Implementation of the SwingingDoor algorithm.

    :param Generator[Tuple[float,float],None,None] data: data;
    :param float deviation: compression deflection.
    :rtype: Generator[Tuple[float, float], None, None]
    :return: Compressed data.

    >>> def data(values):
    ...     x = 0.0
    ...     for y in values:
    ...         yield x, y
    ...         x += 1.0
    >>> tuple(swinging_door(data([
    ...     2.1, 3.1, 4.1, 4.6
    ... ]), deviation=0.1))
    ((0.0, 2.1), (2.444444444444445, 4.372222222222222))

    >>> tuple(swinging_door(data([
    ...     4.1, 3.1, 2.1, 4.6
    ... ]), deviation=0.1))
    ((0.0, 4.1), (2.088235294117647, 2.270588235294118))

    """

    entrance = current = Point(
        *(
            data.__next__()
            if version_info.major > 2
            else data.next()  # type: ignore
        )
    )  # type: Point

    upper_pivot = Point(
        entrance.abscissa, entrance.ordinate + deviation
    )  # type: Point
    lower_pivot = Point(
        entrance.abscissa, entrance.ordinate - deviation
    )  # type: Point

    sloping_upper_max = sloping_lower_min = 0.0  # type: float

    yield entrance()

    while True:
        past = current  # type: Point

        try:
            current = Point(
                *(
                    data.__next__()
                    if version_info.major > 2
                    else data.next()  # type: ignore
                )
            )

        except StopIteration:
            break

        sloping_upper = (current.ordinate - upper_pivot.ordinate) / (
            current.abscissa - upper_pivot.abscissa
        )  # type: float
        sloping_lower = (current.ordinate - lower_pivot.ordinate) / (
            current.abscissa - lower_pivot.abscissa
        )  # type: float

        if not sloping_upper_max and not sloping_lower_min:
            sloping_upper_max = sloping_upper
            sloping_lower_min = sloping_lower

            continue

        if sloping_upper > sloping_upper_max:
            sloping_upper_max = sloping_upper

            if sloping_upper_max > sloping_lower_min:
                sloping_entrance = (current.ordinate - past.ordinate) / (
                    current.abscissa - past.abscissa
                )  # type: float
                entrance_upper = (
                    upper_pivot.ordinate
                    - past.ordinate
                    + sloping_entrance * past.abscissa
                    - sloping_lower_min * upper_pivot.abscissa
                ) / (
                    sloping_entrance - sloping_lower_min
                )  # type: float
                entrance = Point(
                    entrance_upper,
                    upper_pivot.ordinate
                    + sloping_lower_min
                    * (entrance_upper - upper_pivot.abscissa)
                    - deviation / 2,
                )

                yield entrance()

                upper_pivot = Point(
                    entrance.abscissa, entrance.ordinate + deviation
                )
                lower_pivot = Point(
                    entrance.abscissa, entrance.ordinate - deviation
                )

                sloping_upper_max = sloping_upper = (
                    current.ordinate - upper_pivot.ordinate
                ) / (current.abscissa - upper_pivot.abscissa)
                sloping_lower_min = sloping_lower = (
                    current.ordinate - lower_pivot.ordinate
                ) / (current.abscissa - lower_pivot.abscissa)

        elif sloping_lower < sloping_lower_min:
            sloping_lower_min = sloping_lower

            if sloping_upper_max > sloping_lower_min:
                sloping_entrance = (current.ordinate - past.ordinate) / (
                    current.abscissa - past.abscissa
                )
                entrance_lower = (
                    lower_pivot.ordinate
                    - past.ordinate
                    + sloping_entrance * past.abscissa
                    - sloping_upper_max * lower_pivot.abscissa
                ) / (sloping_entrance - sloping_upper_max)
                entrance = Point(
                    entrance_lower,
                    lower_pivot.ordinate
                    + sloping_upper_max
                    * (entrance_lower - lower_pivot.abscissa)
                    + deviation / 2,
                )

                yield entrance()

                upper_pivot = Point(
                    entrance.abscissa, entrance.ordinate + deviation
                )
                lower_pivot = Point(
                    entrance.abscissa, entrance.ordinate - deviation
                )

                sloping_upper_max = sloping_upper = (
                    current.ordinate - upper_pivot.ordinate
                ) / (current.abscissa - upper_pivot.abscissa)
                sloping_lower_min = sloping_lower = (
                    current.ordinate - lower_pivot.ordinate
                ) / (current.abscissa - lower_pivot.abscissa)
