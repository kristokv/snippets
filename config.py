from pydantic import BaseSettings


class Settings(BaseSettings):
    MINIO_ACCESS_ID: str
    MINIO_SECRET_KEY: str
    GEOSERVER_USER: str = "admin"
    GEOSERVER_PASSWORD: str = "geoserver"

    class Config:
        case_sensitive = False
        env_file = ".env"


SETTINGS = Settings()
