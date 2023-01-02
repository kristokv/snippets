from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_ID: str
    SECRET_KEY: str
    GEOSERVER_USER: str
    GEOSERVER_PASSWORD: str

    class Config:
        case_sensitive = False
        env_file = ".env"


SETTINGS = Settings()
