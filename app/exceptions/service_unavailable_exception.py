class ServiceUnavailableException(Exception):
    def __init__(self, message: str = 'Service temporarily unavailable. Please contact support.'):
        super().__init__(message)
