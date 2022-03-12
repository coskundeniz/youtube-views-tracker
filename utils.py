import json
import logging
from logging.handlers import RotatingFileHandler


LOG_FILENAME = "yt_views.log"

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    LOG_FILENAME, maxBytes=20971520, encoding="utf-8", backupCount=50
)
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
log_format = "%(asctime)s [%(levelname)5s] %(lineno)3d: %(message)s"
formatter = logging.Formatter(log_format, datefmt="%d-%m-%Y %H:%M:%S")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_configuration(filename="config.json") -> dict:
    """Read configuration file

    :type filename: str
    :param filename: Name of the configuration file
    :rtype: dict
    :returns: Configuration as dict
    """

    with open(filename, encoding="utf-8") as configfile:
        config = json.load(configfile)

    return config
