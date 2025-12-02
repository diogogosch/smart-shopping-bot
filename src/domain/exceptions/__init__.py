"""Custom exceptions for SmartShopBot domain."""


class SmartShopBotException(Exception):
    """Base exception for SmartShopBot."""
    pass


class ValidationError(SmartShopBotException):
    """Raised when validation fails."""
    pass


class NotFoundError(SmartShopBotException):
    """Raised when a resource is not found."""
    pass


class AlreadyExistsError(SmartShopBotException):
    """Raised when a resource already exists."""
    pass


class RepositoryError(SmartShopBotException):
    """Raised when database operations fail."""
    pass


class CacheError(SmartShopBotException):
    """Raised when cache operations fail."""
    pass


class AIServiceError(SmartShopBotException):
    """Raised when AI service fails."""
    pass


class OCRServiceError(SmartShopBotException):
    """Raised when OCR service fails."""
    pass


class UnauthorizedError(SmartShopBotException):
    """Raised when user is not authorized."""
    pass
