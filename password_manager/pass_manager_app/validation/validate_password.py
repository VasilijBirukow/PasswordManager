def validate_password(password: str) -> list:
    """
    This function checks the password for compliance with certain security criteria.
    If the password does not meet the criteria, the function returns a list
    of lines describing the errors.
    """
    errors = list()

    if not password:
        errors.append("Password cannot be empty")
        return errors

    if len(password) < 8:
        errors.append("The length must be at least 8 characters")

    if password.upper() == password and password.lower() == password:
        errors.append("The letters must be in different case")

    if password.isalnum():
        errors.append("there should be at least one special character")

    if password.isalpha():
        errors.append("there must be at least one digit")

    if password.isdigit():
        errors.append("there must be at least one letter")

    return errors
