from ..errors.errors import ReadFileError


def read_file_by_path(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as error:
        raise ReadFileError(error)
    except PermissionError as error:
        raise ReadFileError(error.message)
    except Exception as error:
        raise ReadFileError(error.message)

