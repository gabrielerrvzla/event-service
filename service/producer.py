import datetime
import json

from kafka import KafkaProducer

from .logger import Logger
from .settings import Settings


class Producer:
    MAX_FLUSH_TIME = 45

    def __init__(self, settings: Settings, logger: Logger):
        self._last_message_sent_time = None
        self.settings = settings
        self.logger = logger

    def _to_dict(self, data: object) -> dict:
        data = json.dumps(data, default=str)
        return json.loads(data)

    def load(self) -> None:
        self._producer = KafkaProducer(
            bootstrap_servers=self.settings.KAFKA_SERVER,
            api_version=(2, 0, 2),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def _flush(self):
        if self._last_message_sent_time:
            if (
                datetime.datetime.now() - self._last_message_sent_time
            ).seconds < self.MAX_FLUSH_TIME:
                self._producer.flush()

    def send_message(self, topic: str, data=object) -> None:
        if not hasattr(self, "_producer"):
            self.load()
        self._flush()
        data = self._to_dict(data)

        result = self._producer.send(topic, data)
        result.get(timeout=60)
        self._last_message_sent_time = datetime.datetime.now()