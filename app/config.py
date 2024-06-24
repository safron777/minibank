from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str


    SECRET_KEY: str
    ALGORITHM: str
    # Со 2 версии Pydantic, class Config был заменен на атрибут model_config
    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(env_file=".env-non-dev")


    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
    

   # REDIS_HOST: str
    #REDIS_PORT: int

    #SENTRY_DSN: str

    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
