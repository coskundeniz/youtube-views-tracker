import os

from exceptions import UrlFileDoesNotExistError
from utils import logger
from urlreader.urlreader import UrlReader


class TxtReader(UrlReader):
    """Url reader for txt files

    :type filename: str
    :param filename: Name of the file containing video urls
    """

    def __init__(self, filename: str) -> None:

        self._filename = filename

    def read_urls(self) -> list:
        """Read urls from file

        :rtype: list
        :returns: List of video urls
        """

        if not os.path.exists(self._filename):
            message = f"Url file {self._filename} does not exist!"
            raise UrlFileDoesNotExistError(message)

        urls = []
        with open(self._filename, encoding="utf-8") as urlsfile:
            logger.info(f"Reading video urls from {self._filename}...")
            urls.extend(urlsfile.read().splitlines())

        return urls
