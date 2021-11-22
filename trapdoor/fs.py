import os
from stat import ST_MODE

def ensure_directory_exists(directory: str, mode=0o700):
    if not os.path.exists(directory):
        os.makedirs(directory, mode)

    if not os.path.isdir(directory):
        raise RuntimeError("`directory` exists but is not a directory!")

    if not get_file_permissions(directory) == mode:
        os.chmod(directory, mode)

def get_file_permissions(file: str):
    return int(oct(os.stat(file).st_mode)[-3:])