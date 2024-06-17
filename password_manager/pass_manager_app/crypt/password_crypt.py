from cryptography.fernet import Fernet


class SingletonMeta(type):
    """
    The Singleton Meta metaclass is used to create the Singleton class.
    This metaclass ensures that only one instance will be created.
    each class using this metaclass.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        When trying to create an instance of a class, this method checks,
        whether an instance of this class already exists. If not, it creates a new one
        and saves it in the _instances dictionary. If an instance already exists,
        it returns an existing instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CipherManager(metaclass=SingletonMeta):
    """
    The Cipher Manager class manages password encryption and decryption.
    It uses the Fernet cipher to securely encrypt data.
    """
    cipher_holder = None

    @classmethod
    def initialize(cls, key):
        """
        Initializes the Fernet cipher using the provided key.
        This method must be called before encrypting or decrypting passwords.
        """
        if not cls.cipher_holder:
            cls.cipher_holder = Fernet(key)

    @classmethod
    def encrypt_password(cls, password: str) -> str:
        """
        Encrypts the password using the Fernet cipher.
        Returns the encrypted password as a string.
        """
        return cls.cipher_holder.encrypt(password.encode('utf-8'))

    @classmethod
    def decrypt_password(cls, encrypted_password: str) -> str:
        """
        Decrypts the encrypted password.
        Returns the original password as a string.
        """
        return cls.cipher_holder.decrypt(encrypted_password[2:-1]).decode('utf-8')
