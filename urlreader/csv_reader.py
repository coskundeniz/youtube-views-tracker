import os
import csv

from exceptions import UrlFileDoesNotExistError
from utils import logger
from urlreader.urlreader import UrlReader


class CsvReader(UrlReader):
    """Url reader for csv files

    :type filename: str
    :param filename: Name of the file containing video urls
    """

    def __init__(self, filename: str, url_column: int) -> None:

        self._filename = filename
        self._url_column = url_column

    def read_urls(self):
        """Read urls from file

        :rtype: list
        :returns: List of video urls
        """

        if not os.path.exists(self._filename):
            message = f"Url file {self._filename} does not exist!"
            raise UrlFileDoesNotExistError(message)

        urls = []

        with open(self._filename, newline="") as csvfile:
            logger.info(f"Reading video urls from {self._filename}...")
            reader = csv.reader(csvfile)
            for row in reader:
                urls.append(row[self._url_column].strip())

        return urls
