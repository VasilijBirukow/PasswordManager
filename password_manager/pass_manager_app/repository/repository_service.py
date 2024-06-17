from typing import Union

from ..models import Service


class ServiceManager:
    @classmethod
    def create_service(cls, service_name) -> Service:
        """
        Creates a new service with the specified name.
        """
        service: Service = Service.objects.create(name=service_name)
        service.save()
        return service

    @classmethod
    def get_service_by_name(cls, service_name) -> Union[Service, None]:
        """Gets the service by the exact name match."""
        service: Service = Service.objects.filter(name=service_name).first()
        return service if service else None

    @classmethod
    def get_service_by_part_of_name(cls, service_name) -> Union[Service, None]:
        """Gets the service by partial name match."""
        service = Service.objects.filter(name__icontains=service_name).first()
        return service if service else None
