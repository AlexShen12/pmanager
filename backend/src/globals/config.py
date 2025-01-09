from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator

class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8')

    # Database settings
    DATABASE_URL: str 
    FERNET_KEY: bytes

settings = Settings()



