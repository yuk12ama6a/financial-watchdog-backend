from src.config import Settings


def test_get_database_url_success() -> None:
    target = Settings(
        POSTGRES_USERNAME="user",
        POSTGRES_PASSWORD="pass",
        POSTGRES_HOST="host",
        POSTGRES_PORT=5432,
        POSTGRES_DB_NAME="db",
    )

    url = target.get_database_url()

    assert url == "postgresql://user:pass@host:5432/db"
