import json
from dataclasses import asdict
from typing import Dict

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_GET, require_POST

from .dto import ServiceResponseDTO
from .errors.request_error_handling import service_not_found, server_error, validation_error
from .errors.errors import ValidationError
from .models import Service
from .repository.repository_password import PasswordManager
from .repository.repository_service import ServiceManager
from .validation.validate_request_data import validate_request_data, check_errors
from .validation.validate_service_name import validate_service_name


@require_POST
def create_or_update(request: HttpRequest, service_name: str) -> JsonResponse:
    try:
        data: Dict[str, str] = json.loads(request.body)
        password: str = data.get('password')

        validate_request_data(password, service_name)

        create_or_update_service(password, service_name)
        return JsonResponse(asdict(ServiceResponseDTO(password, service_name)), status=200)
    except ValidationError as error:
        return JsonResponse(validation_error(error.message), status=400)
    except Exception as error:
        return JsonResponse(server_error(str(error)), status=500)


def create_or_update_service(password: str, service_name: str) -> None:
    """The method handles the logic of creating or updating the service and password. Does not return a value."""
    service: Service = ServiceManager.get_service_by_name(service_name)
    if service is None:
        service: Service = ServiceManager.create_service(service_name)
        PasswordManager.create_password(password, service)
    else:
        PasswordManager.update_password(password, service.id)


@require_GET
def get_password_by_service_name(request: HttpRequest, service_name: str) -> JsonResponse:
    try:
        error_list = validate_service_name(service_name)
        check_errors(error_list)

        service: Service = ServiceManager.get_service_by_name(service_name)

        if service is None:
            raise ObjectDoesNotExist(f'Service with name {service_name} not found')

        password: str = PasswordManager.get_password_by_service_id(service.id)
        return JsonResponse(asdict(ServiceResponseDTO(password, service_name)), status=200)
    except ValidationError as error:
        return JsonResponse(validation_error(error.message), status=400)
    except ObjectDoesNotExist:
        return JsonResponse(service_not_found(service_name), status=404)


@require_GET
def get_password_by_part_of_service_name(request: HttpRequest) -> JsonResponse:
    """The function processes a request to search for a service based on its name. Returns a `JsonResponse`
    with password and service data, or with an error if the service is not found."""
    part_of_service_name: str = request.GET.get('service_name')

    try:
        error_list = validate_service_name(part_of_service_name)
        check_errors(error_list)

        service: Service = ServiceManager.get_service_by_part_of_name(part_of_service_name)
        if not service:
            raise ObjectDoesNotExist('Service not found')

        password: str = PasswordManager.get_password_by_service_id(service.id)
        return JsonResponse(asdict(ServiceResponseDTO(password, service.name)), status=200)
    except ValidationError as error:
        return JsonResponse(validation_error(error.message), status=400)
    except ObjectDoesNotExist:
        return JsonResponse(service_not_found(part_of_service_name), status=404)
    except Exception as error:
        return JsonResponse(server_error(str(error)), status=500)
