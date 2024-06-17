class ValidationError(Exception):
    def __init__(self, error_list: list):
        self.message = ', '.join(error_list)
        super().__init__(self.message)


class ConfigError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class ReadFileError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
