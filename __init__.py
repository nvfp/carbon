import os


LIB_VER = '1.3.0'
LIB_DIR_PTH = os.path.dirname(os.path.abspath(__file__))
LIB_NAME = os.path.basename(LIB_DIR_PTH)  # this name might include the version number
LIB_NAME_ONLY = 'carbon'


## testing purposes
_TESTING_EMPTY_DIR_PTH = os.path.join(LIB_DIR_PTH, '_testing', '_empty_dir')
def _ensure_empty_dir():
    if len(os.listdir(_TESTING_EMPTY_DIR_PTH)) != 0:
        raise AssertionError(f'The dir {repr(_TESTING_EMPTY_DIR_PTH)} is not clean.')