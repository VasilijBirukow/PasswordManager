from dataclasses import dataclass


@dataclass
class ServiceResponseDTO:
    password: str
    service_name: str


@dataclass
class ErrorResponseDTO:
    error: str
    description: str
