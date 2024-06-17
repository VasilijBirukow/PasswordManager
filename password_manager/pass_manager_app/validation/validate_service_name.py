def validate_service_name(service_name: str) -> list:
    """
    This function checks if the given service name is valid. A valid service name
    must not be empty and should contain only alphanumeric characters (letters and digits).
    """
    errors = list()
    if not service_name:
        errors.append("Service name cannot be empty")
        return errors
    if not service_name.isalnum():
        errors.append("Service name should contains digits and letters only")

    return errors
