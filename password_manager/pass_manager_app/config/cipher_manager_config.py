from ..crypt.password_crypt import CipherManager
from ..errors.errors import ConfigError, ReadFileError
from ..utils.file_utils import read_file_by_path


def configurate_cipher_manager():
    """
    This function tries to read the encryption key from the file and initialize
    A Cyphermanager with this key. If an error occurs while reading the file,
    a Config Error exception is thrown with the corresponding error message.
    """
    try:
        key = read_file_by_path('./very_very_secret_key')
        CipherManager.initialize(key)
    except ReadFileError as error:
        raise ConfigError(error.message)