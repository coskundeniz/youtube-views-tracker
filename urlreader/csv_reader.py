import csv

from utils import logger
from urlreader.urlreader import UrlReader


class CsvReader(UrlReader):
    """Url reader for csv files

    :type filename: str
    :param filename: Name of the file containing video urls
    :type url_column: int
    :param url_column: Url column index
    """

    def __init__(self, filename: str, url_column: int) -> None:

        self._filename = filename
        self._url_column = url_column

    def read_urls(self):
        """Read urls from file

        :rtype: list
        :returns: List of video urls
        """

        self.check_file_exists(self._filename)

        urls = []

        with open(self._filename, newline="", encoding="utf-8") as csvfile:
            logger.info(f"Reading video urls from {self._filename}...")
            reader = csv.reader(csvfile)
            for row in reader:
                urls.append(row[self._url_column].strip())

        return urls
