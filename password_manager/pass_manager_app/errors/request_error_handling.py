from dataclasses import asdict

from django.http import HttpRequest

from ..dto import ErrorResponseDTO


def validation_error(message: str) -> dict:
    return asdict(ErrorResponseDTO(error='Request data validation error', description=message))


def request_method_error(request: HttpRequest) -> dict:
    return asdict(ErrorResponseDTO(error='Request method error',
                                   description=f'Unexpected request method: {request.method}'))


def server_error(message: str) -> dict:
    return asdict(ErrorResponseDTO(error='Internal server error', description=message))


def service_not_found(part_of_service_name: str) -> dict:
    return asdict(ErrorResponseDTO(error="Service not found",
                                   description=f'The service that includes the {part_of_service_name} was not found'))