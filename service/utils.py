import pathlib


def extract_filename_and_extension(file: str) -> tuple:
    """
    Get the filename and extension.
    :param file: str: File path.
    :return: tuple: Filename and extension.
    """
    extension = pathlib.Path(file).suffix
    filename = file.split("/")[-1]
    filename = ".".join(filename.split(".")[:-1])

    return filename, extension
