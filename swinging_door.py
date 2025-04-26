#!/usr/bin/env python3

"""
swinging_door
=============

Implementation of the Swinging Door algorithm in Python.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from typing import Generator, Iterator, Tuple, Union

    Source = Union[Generator, Iterator]
    Number = Union[int, float]
    Point = Tuple[Number, Number]
    Stretch = Tuple[Point, Point]
    Slopings = Tuple[float, float]

__author__: str = "Aleksandr F. Mikhaylov (ChelAxe)"
__version__: str = "2.0.0"
__license__: str = "MIT"


def _sloping_calc(stretch: "Stretch", deviation: "Number") -> "Slopings":
    """
    Calculate slopings upper and lower.

    :param Stretch stretch: stretch;
    :param Number deviation: compression deflection.
    :rtype: Slopings
    :return: Slopings upper and lower.
    :raises ValueError: if division by 0 occurs during slope calculation.

    >>> _sloping_calc(((1, 6), (2, 6.5)), 1)
    (1.5, -0.5)

    >>> _sloping_calc(((1, 6), (1, 6.5)), 1)
    Traceback (most recent call last):
        ...
    ValueError: The division by 0 occurs during the calculation of the slope.
    """

    current: "Point"
    entrance: "Point"
    current, entrance = stretch

    _divide: float = current[0] - entrance[0]

    try:
        upper: float = (current[1] - (entrance[1] + deviation)) / _divide
        lower: float = (current[1] - (entrance[1] - deviation)) / _divide

    except ZeroDivisionError as err:
        raise ValueError(
            "The division by 0 occurs during the calculation of the slope."
        ) from err

    return upper, lower


def _new_corridor(
    stretch: "Stretch", deviation: "Number", upper: bool = True
) -> "Tuple[Point, Slopings]":
    """
    Calculate new corridor.

    :param Stretch stretch: stretch;
    :param Number deviation: compression deflection;
    :param bool upper: upper point.
    :rtype: Tuple[Point, Slopings]
    :return: Entrance point and slopings upper and lower.

    >>> _new_corridor(((7, 8), (8, 9.5)), 1)
    ((7.5, 8.25), (0.5, 4.5))

    >>> _new_corridor(((7, 8), (8, 6)), 1, False)
    ((7.5, 7.5), (-5.0, -1.0))
    """

    past: "Point"
    current: "Point"
    past, current = stretch

    entrance: "Point" = (
        (past[0] + current[0]) / 2,
        (
            (past[1] + current[1]) / 2 - (deviation / 2)
            if upper
            else (past[1] + current[1]) / 2 + (deviation / 2)
        ),
    )

    return entrance, _sloping_calc((current, entrance), deviation)


def swinging_door(
    source: "Source", deviation: "Number" = 0.1
) -> "Generator[Point, None, None]":
    """
    Implementation of the SwingingDoor algorithm.

    :param Source source: source data;
    :param Number deviation: compression deflection.
    :rtype: Generator[Point, None, None]
    :return: Compressed data.

    >>> list(swinging_door(iter([
    ...     (1, 6), (2, 6.5), (3, 5.5),
    ...     (4, 6.5), (5, 8), (6, 7.5),
    ...     (7, 8), (8, 9.5),
    ... ]), 1))
    [(1, 6), (7.5, 8.25), (8, 9.5)]

    >>> list(swinging_door(iter([
    ...     (1, 6), (2, 6.5), (3, 5.5),
    ...     (4, 6.5), (5, 8), (6, 7.5),
    ...     (7, 8), (8, 6),
    ... ]), 1))
    [(1, 6), (7.5, 7.5), (8, 6)]

    >>> list(swinging_door(iter([
    ...     (1, 6), (2, 6.5), (3, 5.5),
    ...     (4, 6.5), (5, 8), (6, 7.5),
    ...     (7, 8),
    ... ]), 0))
    [(1, 6), (2, 6.5), (3, 5.5), (4, 6.5), (5, 8), (6, 7.5), (7, 8)]

    >>> list(swinging_door(iter([]), 1))
    []

    >>> list(swinging_door(iter([(1, 6),]), 1))
    [(1, 6)]

    >>> list(swinging_door(iter([(1, 6),(1, 6.5),]), 1))
    Traceback (most recent call last):
        ...
    ValueError: The division by 0 occurs during the calculation of the slope.
    """

    if not deviation:
        yield from source
        return

    try:
        entrance: "Point" = next(source)

    except StopIteration:
        return

    yield entrance

    try:
        current: "Point" = next(source)

    except StopIteration:
        return

    sloping_upper: float
    sloping_lower: float

    sloping_upper, sloping_lower = _sloping_calc(
        (current, entrance), deviation
    )

    sloping_upper_max: float = sloping_upper
    sloping_lower_min: float = sloping_lower

    try:
        while True:
            past: "Point" = current
            current = next(source)

            sloping_upper, sloping_lower = _sloping_calc(
                (current, entrance), deviation
            )

            if sloping_upper > sloping_upper_max:
                sloping_upper_max = sloping_upper

                if sloping_upper_max > sloping_lower_min:
                    entrance, (
                        sloping_upper_max,
                        sloping_lower_min,
                    ) = _new_corridor((past, current), deviation)

                    yield entrance

            elif sloping_lower < sloping_lower_min:
                sloping_lower_min = sloping_lower

                if sloping_upper_max > sloping_lower_min:
                    entrance, (
                        sloping_upper_max,
                        sloping_lower_min,
                    ) = _new_corridor((past, current), deviation, upper=False)

                    yield entrance

    except StopIteration:
        yield past


if __name__ == "__main__":  # pragma: no cover
    import sys
    from doctest import testmod

    sys.exit(testmod().failed)
