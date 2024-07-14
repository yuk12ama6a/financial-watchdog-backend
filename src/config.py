from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    アプリ設定

    Attributes
        - MAJOR_VERSION (int): メジャーバージョン
        - MINOR_VERSION (int): マイナーバージョン
        - PATCH_VERSION (int): パッチバージョン
    """

    VERSION: str = "0.0.0"

    model_config = SettingsConfigDict(env_file="./env/.env", env_file_encoding="utf-8")
