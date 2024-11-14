import json

from kafka import KafkaConsumer, errors

from .codes import ERROR_KAFKA_CONSUMER, WARNING_DECODING_JSON_MESSAGE
from .logger import Logger
from .settings import Settings


class Consumer:
    def __init__(self, settings: Settings, logger: Logger):
        self.settings = settings
        self.logger = logger
        self._consumer = KafkaConsumer(
            bootstrap_servers=settings.KAFKA_SERVER,
            group_id=settings.KAFKA_GROUP,
            auto_offset_reset=settings.KAFKA_AUTO_OFFSET_RESET,
            auto_commit_interval_ms=30 * 1000,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

    def subscribe(self) -> None:
        self.logger.info(f"Subscribing to topic {self.settings.KAFKA_TOPIC}")
        self._consumer.subscribe(topics=self.settings.KAFKA_TOPIC)

    def start_consumption(self, handle_event: callable) -> None:
        self.logger.info("Starting consumption of messages")
        while True:
            try:
                records = self._consumer.poll(timeout_ms=1000)

                if not records:
                    continue

                for topic_data, consumer_records in records.items():
                    for consumer_record in consumer_records:
                        message = consumer_record.value
                        handle_event(message)

            except (json.decoder.JSONDecodeError, AttributeError):
                self.logger.warning(
                    "Error in decoding JSON message",
                    code=WARNING_DECODING_JSON_MESSAGE,
                )
                continue

            except errors.KafkaError as e:
                self._consumer.close()
                self.logger.warning(
                    f"Error in consuming message {e}",
                    code=ERROR_KAFKA_CONSUMER,
                )
                break

            except (KeyboardInterrupt, SystemExit):
                self._consumer.close()
                self.logger.info("Stopping consumption of messages")
                break
