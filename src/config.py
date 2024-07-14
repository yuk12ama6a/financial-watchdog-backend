from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    アプリ設定

    Attributes
        - VERSION (str): バージョン
    """

    VERSION: str = "0.0.0"

    model_config = SettingsConfigDict(env_file="./env/.env", env_file_encoding="utf-8")
