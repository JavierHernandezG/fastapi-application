from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from injector import Injector

class Settings(BaseSettings):
    environment: str = "local"
    app_name: str
    app_host: str 
    app_port: int

    model_config = SettingsConfigDict(env_file=".env")

    #TODO what is property
    @property
    def injector(self) -> Injector:
        from fastapi_application.dependencies import injectors
        return injectors[self.environment]

