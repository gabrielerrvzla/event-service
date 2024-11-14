import os
from typing import ClassVar

from pydantic import field_validator
from pydantic_settings import BaseSettings

from .logger import Logger


class Settings(BaseSettings):
    # Base
    STATIC: ClassVar[str] = os.path.join(os.path.dirname(__file__), "static")
    SERVICE_NAME: str = "service"

    # Kafka
    KAFKA_SERVER: str
    KAFKA_GROUP: str
    KAFKA_TOPIC: str
    KAFKA_AUTO_OFFSET_RESET: str = "smallest"

    # Minio
    MINIO_HOST: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_SECURE: bool
    MINIO_CERT_CHECK: bool

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # Sentry
    SENTRY_DSN: str = None
    SENTRY_TRACE_SAMPLE_RATE: float = 1.0

    @field_validator("KAFKA_TOPIC", mode="after")
    def split_string_to_list(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


settings = Settings()
logger = Logger(settings.SERVICE_NAME, level=Logger.INFO)
