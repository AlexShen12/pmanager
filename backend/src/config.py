from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config: SettingsConfigDict = SettingsConfigDict(env_file= '.env', env_file_encoding='utf-8', env_ignore_empty=True)

    DATABASE_URL: str
    FERNET_KEY: bytes

settings = Settings()
