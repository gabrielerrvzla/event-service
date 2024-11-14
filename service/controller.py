from .codes import WARNING_INVALID_MESSAGE
from .logger import Logger
from .schemas import MessageSchema
from .settings import Settings
from .worker import process_message


class Controller:
    def __init__(self, settings: Settings, logger: Logger):
        self.settings = settings
        self.logger = logger

    def handle_event(self, event):
        try:
            message = MessageSchema(**event)
        except (ValueError, TypeError, AttributeError) as e:
            self.logger.warning(f"Invalid message: {e}", code=WARNING_INVALID_MESSAGE)
            return

        self.logger.info(f"Processing message for ID: {message.id}")
        process_message.delay(message.model_dump())
        self.logger.info(f"Message processing scheduled for ID: {message.id}")
