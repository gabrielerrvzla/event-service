from celery import Celery

from .schemas import MessageSchema
from .settings import logger, settings

app = Celery(
    "worker",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0",
    broker_connection_retry_on_startup=True,
)


@app.task(name="process_message")
def process_message(message: dict):
    data = MessageSchema(**message)
    logger.info(f"Processing message for ID: {data.id}")
