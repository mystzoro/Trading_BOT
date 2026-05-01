import logging
from pathlib import Path


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("trading_bot")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    log_path = Path("bot.log")

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(
        logging.Formatter("%(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
