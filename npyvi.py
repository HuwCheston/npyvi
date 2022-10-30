#!/usr/bin/env python
from collections.abc import Iterable


def _npvi(
        dat: Iterable[int | float]
) -> float:
    return sum([abs((k - k1) / ((k + k1) / 2)) for (k, k1) in zip(dat, dat[1:])]) * 100 / (sum(1 for _ in dat) - 1)


def npvi(
        *args: int | float | Iterable[float | int]
) -> float | list[float]:
    """
    Extracts the normalised pairwise variability index (nPVI).

    This function can take as an input an arbitrary number of ints
    or floats, or an arbitrary number of iterables containing ints
    and floats. If the former, returns a single nPVI value for all
    arguments; if the latter, returns array of nPVI values for every
    individual iterable provided.


    Parameters
    ----------
    args : int | float | Iterable[float | int]
        Data to extra nPVI values from.

    Returns
    -------
    float | Iterable[float]
        The extracted nPVI value or values.

    Examples
    --------
    >>> npvi(1, 2, 3)
    53.333333333333336
    >>> npvi([1, 2, 3], [3, 3, 6], [4, 6, 8])
    [53.333333333333336, 33.33333333333333, 34.285714285714285]
    """

    if all(isinstance(x, (int, float)) for x in args):
        return _npvi(args)
    elif all(isinstance(x, Iterable) for x in args):
        return [_npvi([i for i in x if isinstance(i, (int, float))]) for x in args]
    else:
        raise TypeError('Could not parse input for nPVI calculation')
