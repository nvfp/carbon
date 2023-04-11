import random as _random


def randfloat(__low: float, __high: float, __prec: int = 2, /) -> float:
    """
    This function follows `random.uniform` behaviors.
    `__prec`: float precision (>= 0); if `__low` at 2 decimal point (`0.25`), `__prec` should at least `2`.
    `__prec` normally max at 15-18 (depends on system).
    """

    ## each end only half probability-dense
    # return round(_random.uniform(__low, __high), __prec)

    k = pow(10, __prec)
    return _random.randint(round(__low*k), round(__high*k)) / k


def randrange(low: float, high: float, len: float, /, pad: float = 0.1, prec: int = 3) -> tuple[float, float]:
    """
    if `low = 0, high = 1` -> include both `0` and `1`.
    if `low = 0, high = 1, pad = 0.1` -> include both `0.1` and `0.9`.

    `pad`: should `0 <= pad < 0.5`
    """

    range_len = high - low
    the_pad = range_len * pad

    start = randfloat(low + the_pad, high - the_pad - len, prec)
    end = start + len

    return (start, end)


def minmax_normalization(x: float, min: float, max: float, /) -> float:
    """min-max feature scaling"""
    return (x - min) / (max - min)


def slice_list(__in: list, __n: int, /) -> list:
    """if `__n = 2` -> `[1, 2, 3, 4, 5]` -> `[[1, 2], [3, 4], [5]]`"""
    out = [
        __in[i : i + __n]
        for i in range(0, len(__in), __n)
    ]
    return out