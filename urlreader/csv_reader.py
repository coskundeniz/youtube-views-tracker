from urlreader.urlreader import UrlReader


class CsvReader(UrlReader):
    """Url reader for csv files

    :type filename: str
    :param filename: Name of the file containing video urls
    """

    def __init__(self, filename: str) -> None:

        self.filename = filename

    def read_urls(self):
        """Read urls from file"""
        pass