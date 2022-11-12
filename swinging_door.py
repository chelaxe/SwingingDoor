#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

swinging_door
=============

Implementation of the SwingingDoor algorithm in Python.

"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from typing import Generator, List, Tuple

    Point = Tuple[float, float]

__author__ = "Aleksandr F. Mikhaylov (ChelAxe)"  # type: str
__version__ = "1.0.0"  # type: str
__license__ = "MIT"  # type: str


def swinging_door(  # pylint: disable=too-many-locals
    data,  # type: List[Point]
    deviation=0.1,  # type: float
    mode=False,  # type: bool
    step=10,  # type: int
):
    # type: (...) -> Generator[Point, None, None]
    """

    Implementation of the SwingingDoor algorithm.

    :param List[Point] data: data;
    :param float deviation: compression deflection;
    :param bool mode: use a modified algorithm;
    :param int step: step for the modified algorithm.
    :rtype: Generator[Point, None, None]
    :return: Compressed data.

    >>> list(swinging_door([
    ...     (0., 5.0), (1., 5.5), (2., 4.2),
    ...     (3., 5.8), (4., 5.2), (5., 6.8),
    ... ], deviation=1.))
    [(0.0, 5.0), (4.5, 5.5), (5.0, 6.8)]

    >>> list(swinging_door([
    ...     (0., 5.0), (1., 5.5), (2., 4.2),
    ...     (3., 5.8), (4., 5.2), (5., 2.8),
    ... ], deviation=1.))
    [(0.0, 5.0), (4.5, 3.5), (5.0, 2.8)]

    >>> list(swinging_door([
    ...     (0., 5.0), (1., 5.5), (2., 4.2),
    ...     (3., 5.8), (4., 5.2), (5., 6.8),
    ... ], deviation=1., mode=True))
    [(0.0, 5.0), (4.0, 5.2), (5.0, 6.8)]

    >>> list(swinging_door([
    ...     (0., 5.0), (1., 5.5), (2., 4.2),
    ...     (3., 5.8), (4., 5.2), (5., 6.8),
    ... ], deviation=1., mode=True, step=2))
    [(0.0, 5.0), (2.0, 4.2), (5.0, 6.8)]

    """

    current_step = 0  # type: int
    upper_pivot = lower_pivot = current = (0.0, 0.0)  # type: Point

    sloping_upper_max = sloping_lower_min = 0.0  # type: float

    for i, item in enumerate(data):
        if not i:
            entrance = current = item

            upper_pivot = (
                entrance[0],
                entrance[1] + deviation,
            )
            lower_pivot = (
                entrance[0],
                entrance[1] - deviation,
            )

            yield entrance

            current_step = 0
            continue

        past, current = current, item

        sloping_upper = (current[1] - upper_pivot[1]) / (
            current[0] - upper_pivot[0]
        )  # type: float
        sloping_lower = (current[1] - lower_pivot[1]) / (
            current[0] - lower_pivot[0]
        )  # type: float

        if not sloping_upper_max and not sloping_lower_min:
            sloping_upper_max = sloping_upper
            sloping_lower_min = sloping_lower

            current_step += 1
            continue

        if sloping_upper > sloping_upper_max:
            sloping_upper_max = sloping_upper

            if sloping_upper_max > sloping_lower_min:
                entrance = (
                    past
                    if mode
                    else (
                        (past[0] + current[0]) / 2,
                        (past[1] + current[1]) / 2 - (deviation / 2),
                    )
                )

                yield entrance

                current_step = 0

                upper_pivot = entrance[0], entrance[1] + deviation
                lower_pivot = entrance[0], entrance[1] - deviation

                sloping_upper_max = (current[1] - upper_pivot[1]) / (
                    current[0] - upper_pivot[0]
                )
                sloping_lower_min = (current[1] - lower_pivot[1]) / (
                    current[0] - lower_pivot[0]
                )

        elif sloping_lower < sloping_lower_min:
            sloping_lower_min = sloping_lower

            if sloping_upper_max > sloping_lower_min:
                entrance = (
                    past
                    if mode
                    else (
                        (past[0] + current[0]) / 2,
                        (past[1] + current[1]) / 2 - (deviation / 2),
                    )
                )

                yield entrance

                current_step = 0

                upper_pivot = entrance[0], entrance[1] + deviation
                lower_pivot = entrance[0], entrance[1] - deviation

                sloping_upper_max = (current[1] - upper_pivot[1]) / (
                    current[0] - upper_pivot[0]
                )
                sloping_lower_min = (current[1] - lower_pivot[1]) / (
                    current[0] - lower_pivot[0]
                )

        if mode and current_step == step:
            entrance = past

            yield entrance

            current_step = 0

            upper_pivot = entrance[0], entrance[1] + deviation
            lower_pivot = entrance[0], entrance[1] - deviation

            sloping_upper_max = (current[1] - upper_pivot[1]) / (
                current[0] - upper_pivot[0]
            )
            sloping_lower_min = (current[1] - lower_pivot[1]) / (
                current[0] - lower_pivot[0]
            )

        else:
            current_step += 1

    yield current
