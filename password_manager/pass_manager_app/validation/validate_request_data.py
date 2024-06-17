from ..errors.errors import ValidationError
from .validate_password import validate_password
from .validate_service_name import validate_service_name


def validate_request_data(password: str, service_name: str):
    """Validates the request data by checking the password and the name of the service."""
    errors = list()
    errors.extend(validate_password(password))
    errors.extend(validate_service_name(service_name))

    check_errors(errors)


def check_errors(error_list: list):
    """Checks the error list and throws an exception if it is not empty."""
    if len(error_list) > 0:
        raise ValidationError(error_list)
