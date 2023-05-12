import numpy as _np


def tanh(__x: _np.ndarray, /, derivative: bool = False) -> _np.ndarray:
    """`__x`: Float value or a numpy array."""

    z = _np.tanh(__x)

    if derivative:
        return 1 - z*z
    else:
        return z

def sigmoid(__x: _np.ndarray, /, derivative: bool = False) -> _np.ndarray:
    """`__x`: Float value or a numpy array."""

    z = 1 / (1 + _np.exp(-__x))

    if derivative:
        return z*(1 - z)
    else:
        return z

def relu(__x: _np.ndarray, /, derivative: bool = False) -> _np.ndarray:
    """`__x`: Float value or a numpy array."""

    if derivative:
        return _np.where(__x > 0, 1, 0)
    else:
        return _np.maximum(0, __x)

def softmax():
    raise NotImplementedError
