from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    アプリ設定

    Attributes
        - MAJOR_VERSION (int): メジャーバージョン
        - MINOR_VERSION (int): マイナーバージョン
        - PATCH_VERSION (int): パッチバージョン
    """

    MAJOR_VERSION: int = 0
    MINOR_VERSION: int = 0
    PATCH_VERSION: int = 0

    model_config = SettingsConfigDict(env_file="./env/.env", env_file_encoding="utf-8")
