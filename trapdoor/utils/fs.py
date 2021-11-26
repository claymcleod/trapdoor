import os

def ensure_directory_exists(directory: str, mode: int = 0o700):
    """Ensures that a directory exists and has the mode that
    is specified in the arguments (by default, ensures the 
    directory is only readable by the current user).

    :param directory: Directory to ensure exists.
    :type directory: str
    :param mode: Permissions for the directory, defaults to 0o700
    :type mode: int, optional
    :raises RuntimeError: The path exists, but it's not a directory.
    
    >>> import os
    >>> import tempfile
    >>> tempdir = tempfile.mkdtemp()
    >>> test_dir_path = os.path.join(tempdir, "test")
    >>> ensure_directory_exists(test_dir_path)
    >>> get_file_permissions(test_dir_path)
    700
    >>> test_dir_path2 = os.path.join(tempdir, "test_two")
    >>> ensure_directory_exists(test_dir_path2, 0o777)
    >>> get_file_permissions(test_dir_path2)
    777
    """
    directory = os.path.expanduser(directory)

    if not os.path.exists(directory):
        os.makedirs(directory, mode)

    if not os.path.isdir(directory):
        raise RuntimeError("`directory` exists but is not a directory!")

    if not get_file_permissions(directory) == mode:
        os.chmod(directory, mode)

def get_file_permissions(path: str) -> int:
    """Simple utility function to get the current Unix
    file permissions for the specified path.

    :param path: Filepath to get permissions on.
    :type file: str
    :return: The permissions for the file at the path.
    :rtype: int
    """
    return int(oct(os.stat(path).st_mode)[-3:])