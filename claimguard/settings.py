from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config= SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    ACCOUNT_SID: str
    AUTH_TOKEN: str