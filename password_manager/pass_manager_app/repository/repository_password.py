from typing import Union

from ..crypt.password_crypt import CipherManager

from ..models import Password, Service


class PasswordManager:
    """
    This class is responsible for validating the incoming request data for a service.
    It ensures that the provided password meets the required validation criteria and
    that the service name contains only valid characters.
    """
    @classmethod
    def create_password(cls, password: str, service: Service) -> None:
        """Creates a new password for the specified service and saves it in the database."""
        encrypt_password = CipherManager.encrypt_password(password)
        password_entity: Password = Password(service_id=service.id, password=encrypt_password)
        password_entity.save()

    @classmethod
    def update_password(cls, password: str, service_id: int) -> None:
        """Updates the existing password for the service with the specified ID."""
        encrypt_password = CipherManager.encrypt_password(password)
        Password.objects.filter(service_id=service_id).update(password=encrypt_password)

    @classmethod
    def get_password_by_service_id(cls, service_id: int) -> Union[str, None]:
        """Receives the encrypted password for the service with the specified ID and decrypts it."""
        password_entity: Password = Password.objects.filter(service=service_id).first()
        if password_entity:
            return CipherManager.decrypt_password(password_entity.password)
        else:
            return None
