from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8')

    # Database settings
    DATABASE_URL: str 



