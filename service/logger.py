import json
import logging


class Formatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "level": record.levelname,
            "message": record.getMessage(),
            "datetime": self.formatTime(record, self.datefmt),
            **getattr(record, "extra", {}),
        }
        return json.dumps(log_entry)


class Logger:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(Formatter())
        self.logger.addHandler(handler)

    def _log(self, level: int, message: str, **context) -> None:
        self.logger.log(level, message, extra={"extra": context})

    def debug(self, message: str, **context) -> None:
        self._log(self.DEBUG, message, **context)

    def info(self, message: str, **context) -> None:
        self._log(self.INFO, message, **context)

    def warning(self, message: str, **context) -> None:
        self._log(self.WARNING, message, **context)

    def error(self, message: str, code: int, **context) -> None:
        self._log(self.ERROR, message, code=code, **context)

    def critical(self, message: str, code: int, **context) -> None:
        self._log(self.CRITICAL, message, code=code, **context)
