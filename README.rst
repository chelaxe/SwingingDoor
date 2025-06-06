|License| |Release| |Supported versions| |Docs|
|Code Coverage| |Build status Appveyor| |Build Status Travis CI|
|Contact| |Blog|

Swinging Door
=============

Implementation of the Swinging Door algorithm in Python.

Example of usage
----------------

.. code:: python

    >>> from datetime import datetime
    >>> from pandas import read_csv, DataFrame

    >>> df = DataFrame(
    ...     [
    ...         {
    ...             "Date": datetime.strptime(date, "%Y-%m-%d"),
    ...             "Price": value
    ...         }
    ...         for date, value in read_csv(
    ...             "https://datahub.io/core/oil-prices/r/wti-daily.csv"
    ...         ).values.tolist()
    ...     ]
    ... )

    >>> print(len(df))
    9895

    >>> df.plot(x="Date", y="Price")

.. code:: python

    >>> from swinging_door import swinging_door

    >>> compress = DataFrame(
    ...      list(
    ...         {
    ...             "Date": datetime.fromtimestamp(date),
    ...             "Price": value
    ...         }
    ...         for date, value in swinging_door(
    ...             iter(
    ...                 (date.timestamp(), value)
    ...                 for date, value in df.values.tolist()
    ...             ), deviation=.5
    ...         )
    ...     )
    ... )

    >>> print(len(compress))
    3392

    >>> compress.plot(x="Date", y="Price")

.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target:  https://opensource.org/licenses/MIT
.. |Release| image:: https://img.shields.io/github/release/chelaxe/SwingingDoor.svg
   :target: https://github.com/chelaxe/SwingingDoor/releases
.. |Supported versions| image:: https://img.shields.io/pypi/pyversions/swinging_door.svg
   :target: https://pypi.org/project/swinging_door/
.. |Docs| image:: https://readthedocs.org/projects/swingingdoor/badge/?version=latest&style=flat
   :target:  https://swingingdoor.readthedocs.io/en/latest/
.. |Code Coverage| image:: https://codecov.io/gh/chelaxe/SwingingDoor/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/chelaxe/SwingingDoor
.. |Build status Appveyor| image:: https://ci.appveyor.com/api/projects/status/github/chelaxe/swingingdoor?branch=main&svg=true
   :target: https://ci.appveyor.com/project/chelaxe/swingingdoor
.. |Build Status Travis CI| image:: https://api.travis-ci.com/chelaxe/SwingingDoor.svg?branch=main
   :target: https://app.travis-ci.com/github/chelaxe/SwingingDoor
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
   :target:  https://t.me/chelaxe
.. |Blog| image:: https://img.shields.io/badge/site-my%20blog-yellow.svg
   :target:  https://chelaxe.ru/
