import json as _json
import os as _os
import typing as _typing


class SafeJSON:
    """Secure JSON read/write operations, ensuring data integrity during writing and rewriting."""

    @staticmethod
    def write(__pth: str, __obj: _typing.Any, /, do_log: bool = True) -> None:

        ## normalize the path and perform some validations
        pth_norm = _os.path.normpath(__pth)
        if not pth_norm.lower().endswith('.json'):
            raise AssertionError(f'Not a JSON file: {repr(__pth)}.')
        if not _os.path.isdir(_os.path.dirname(pth_norm)):
            raise NotADirectoryError(f'The directory does not exist: {repr(__pth)}.')
        if _os.path.exists(pth_norm):
            raise FileExistsError(f'File already exists: {repr(__pth)}.')

        with open(pth_norm, 'w') as fp:
            _json.dump(__obj, fp)
        
        if do_log:
            print(f'INFO: Json written: {repr(__pth)}.')

    @staticmethod
    def read(__pth: str, /) -> _typing.Any:

        ## normalize the path and perform some validations
        pth_norm = _os.path.normpath(__pth)
        if not pth_norm.lower().endswith('.json'):
            raise AssertionError(f'Not a JSON file: {repr(__pth)}.')
        if not _os.path.isfile(pth_norm):
            raise FileNotFoundError(f'Not a file: {repr(__pth)}.')

        with open(pth_norm, 'r') as fp:
            out = _json.load(fp)
        return out

    @staticmethod
    def rewrite(__pth: str, __obj: _typing.Any, /, do_log: bool = True) -> None:

        ## normalize the path and perform some validations
        pth_norm = _os.path.normpath(__pth)
        if not pth_norm.lower().endswith('.json'):
            raise AssertionError(f'Not a JSON file: {repr(__pth)}.')
        if not _os.path.isfile(pth_norm):
            raise FileNotFoundError(f'Not a file: {repr(__pth)}.')

        tmp_file = pth_norm + '.tmp'
        bak_file = pth_norm + '.bak'
        if _os.path.exists(tmp_file):
            raise FileExistsError(f'Temporary file exists: {repr(tmp_file)}.')
        if _os.path.exists(bak_file):
            raise FileExistsError(f'Backup file exists: {repr(bak_file)}.')

        ## writing the new as temp
        with open(tmp_file, 'w') as fp:
            _json.dump(__obj, fp)

        _os.rename(pth_norm, bak_file)  # backup the previous
        _os.rename(tmp_file, pth_norm)  # rename temp to new
        _os.remove(bak_file)  # delete the previous

        if do_log:
            print(f'INFO: Json rewritten: {repr(__pth)}.')
    
    @staticmethod
    def recover(__pth: str, /) -> None:

        ## normalize and ensure that it's a JSON file
        pth_norm = _os.path.normpath(__pth)
        if not pth_norm.endswith('.json'):
            raise ValueError(f'Not a JSON file: {repr(__pth)}.')

        tmp_file = pth_norm + '.tmp'
        bak_file = pth_norm + '.bak'

        ## case I
        if _os.path.exists(pth_norm) and _os.path.exists(tmp_file) and (not _os.path.exists(bak_file)):
            _os.remove(tmp_file)
            return

        ## case II
        if (not _os.path.exists(pth_norm)) and _os.path.exists(tmp_file) and _os.path.exists(bak_file):
            _os.rename(tmp_file, pth_norm)
            _os.remove(bak_file)
            return

        ## case III
        if _os.path.exists(pth_norm) and (not _os.path.exists(tmp_file)) and _os.path.exists(bak_file):
            _os.remove(bak_file)
            return