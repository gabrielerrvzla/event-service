import sentry_sdk

from .consumer import Consumer
from .controller import Controller
from .settings import logger, settings


def main() -> None:
    consumer = Consumer(settings, logger)
    controller = Controller(settings, logger)

    if settings.SENTRY_DSN:
        logger.info("Sentry enabled")
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            traces_sample_rate=settings.SENTRY_TRACE_SAMPLE_RATE,
        )

    consumer.subscribe()
    consumer.start_consumption(controller.handle_event)


if __name__ == "__main__":
    main()
