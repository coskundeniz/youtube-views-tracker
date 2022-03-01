import os

from utils import logger
from urlreader.urlreader import UrlReader


class TxtReader(UrlReader):
    """Url reader for txt files

    :type filename: str
    :param filename: Name of the file containing video urls
    """

    def __init__(self, filename: str) -> None:

        self.filename = filename

    def read_urls(self) -> list:
        """Read urls from file

        :rtype: list
        :returns: List of video urls
        """

        if not os.path.exists(self.filename):
            logger.error(f"Url file {self.filename} does not exist!")
            raise SystemExit()

        urls = []
        with open(self.filename, encoding="utf-8") as urlsfile:
            logger.info(f"Reading video urls from {self.filename}...")
            urls.extend(urlsfile.read().splitlines())

        return urls
