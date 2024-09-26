from injector import Module, provider, singleton, injector
import logging
from fastapi_application.settings import Settings

class LocalModule(Module):
    #TODO singleton and injector what are they?
    @singleton
    @provider
    def settings(self) -> Settings:
        return Settings()

    @provider
    @singleton
    def make_logger(self, settings: Settings) -> logging.Logger:
        logging.basicConfig(
                level=logging.DEBUG,
                format="[%(asctime)s] %(levelname)s - %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",
                )
        return logging.getLogger(settings.app_name)

    #TODO create clients with singleton and providers

local_injection = (LocalModule)

injectors = {"local": local_injection}
