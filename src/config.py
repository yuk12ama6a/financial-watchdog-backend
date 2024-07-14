from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    アプリ設定

    Attributes
        - VERSION (str): バージョン
        - POSTGRES_USERNAME (str): PostgreSQLのユーザ名
        - POSTGRES_PASSWORD (str): PostgreSQLのパスワード
        - POSTGRES_HOST (str): PostgreSQLのホスト名
        - POSTGRES_PORT (int): PostgreSQLのポート番号
        - POSTGRES_DB_NAME (str): PostgreSQLのデータベース名
    """

    # Core
    VERSION: str = "0.0.0"

    # DB
    POSTGRES_USERNAME: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB_NAME: str = "postgres"

    model_config = SettingsConfigDict(env_file="./env/.env", env_file_encoding="utf-8")

    def get_database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USERNAME}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}"
