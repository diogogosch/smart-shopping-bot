"""Application settings and configuration."""
from typing import Literal, Optional
from pydantic_settings import BaseSettings
from pydantic import Field, validator


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str = Field(..., description="Telegram bot token")
    BOT_USERNAME: str = Field(default="SmartShopBot", description="Bot username")
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql://shopbot:shopbot@localhost:5432/smart_shop_bot",
        description="PostgreSQL connection URL"
    )
    DATABASE_POOL_SIZE: int = Field(default=10, description="Connection pool size")
    DATABASE_MAX_OVERFLOW: int = Field(default=20, description="Max pool overflow")
    
    # Redis
    REDIS_URL: str = Field(
        default="redis://localhost:6379",
        description="Redis connection URL"
    )
    REDIS_TTL: int = Field(default=3600, description="Redis cache TTL in seconds")
    
    # AI Provider
    AI_PROVIDER: Literal["openai", "gemini", "none"] = Field(
        default="openai",
        description="AI provider to use"
    )
    OPENAI_API_KEY: Optional[str] = Field(default=None, description="OpenAI API key")
    OPENAI_MODEL: str = Field(default="gpt-3.5-turbo", description="OpenAI model name")
    GEMINI_API_KEY: Optional[str] = Field(default=None, description="Gemini API key")
    GEMINI_MODEL: str = Field(default="gemini-2.0-flash", description="Gemini model name")
    
    # OCR
    TESSERACT_PATH: Optional[str] = Field(
        default=None,
        description="Path to tesseract binary"
    )
    GOOGLE_VISION_API_KEY: Optional[str] = Field(
        default=None,
        description="Google Vision API key"
    )
    
    # Features
    ENABLE_AI_SUGGESTIONS: bool = Field(default=True, description="Enable AI suggestions")
    ENABLE_PRICE_TRACKING: bool = Field(default=True, description="Enable price tracking")
    ENABLE_NOTIFICATIONS: bool = Field(default=True, description="Enable notifications")
    
    # Internationalization
    DEFAULT_LANGUAGE: str = Field(default="en", description="Default language")
    SUPPORTED_LANGUAGES: list = Field(
        default=["en", "pt_BR"],
        description="Supported languages"
    )
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    
    # Environment
    ENVIRONMENT: Literal["development", "production"] = Field(
        default="production",
        description="Environment type"
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @validator("AI_PROVIDER", pre=True)
    def validate_ai_provider(cls, v: str) -> str:
        """Validate AI provider configuration."""
        if v == "none":
            return "none"
        if v == "openai" and not cls.OPENAI_API_KEY:
            raise ValueError("OpenAI API key required for openai provider")
        if v == "gemini" and not cls.GEMINI_API_KEY:
            raise ValueError("Gemini API key required for gemini provider")
        return v


# Global settings instance
settings = Settings()
