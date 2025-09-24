from typing import Any


from fastapi import status, FastAPI

class BlogAPIException(Exception):
    """
    Base exception class for blog API.
    
    All custom exceptions should inherit from this class
    to ensure consistent error handling.
    """
    
    def __init__(
        self,
        message: str,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        self.message = message
        self.error_code = error_code or self.__class__.__name__.upper()
        self.details = details or {}
        self.status_code = status_code
        super().__init__(self.message)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all exception handlers with the FastAPI app.
    
    Args:
        app: FastAPI application instance
    """
    # Add exceptions here
    pass
