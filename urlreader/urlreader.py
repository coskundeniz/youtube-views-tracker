import os
from abc import ABC, abstractmethod

from exceptions import UrlFileDoesNotExistError
from utils import logger


class UrlReader(ABC):
    """Base class for url readers"""

    MAX_URL_COUNT = 1000
    MAX_CHANNEL_COUNT = 3

    @abstractmethod
    def read_urls(self) -> list:
        """Read urls from file"""

    @classmethod
    def check_url_count(cls: "UrlReader", urls: list[str]) -> list[str]:
        """Check and adjust number of urls

        If the number is higher than 1000, return the first 1000 urls.

        :type cls: UrlReader
        :param cls: Class instance
        :type urls: list
        :param urls: List of video urls
        :rtype: list
        :returns: List of video urls
        """

        if len(urls) > cls.MAX_URL_COUNT:
            logger.warning(f"Max number of urls reached! Using first {cls.MAX_URL_COUNT} urls...")
            urls = urls[: cls.MAX_URL_COUNT]

        return urls

    @staticmethod
    def check_file_exists(filepath: str) -> None:
        """Check if given filepath exists

        Raises UrlFileDoesNotExistError if file does not exist.

        :type filepath: str
        :param filepath: Path of the input file
        """

        if not os.path.exists(filepath):
            message = f"Url file {filepath} does not exist!"
            raise UrlFileDoesNotExistError(message)
