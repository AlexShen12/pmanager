from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"

    # Security settings
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"  # For JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Other settings
    DEBUG: bool = True
    APP_NAME: str = "My FastAPI App"
    API_VERSION: str = "v1"

    class Config:
        env_file = ".env"  # Load variables from .env file


# Create a settings instance to use throughout the app
settings = Settings()
