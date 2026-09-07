from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bwenge"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///./bwenge.db"

    SECRET_KEY: str = "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()