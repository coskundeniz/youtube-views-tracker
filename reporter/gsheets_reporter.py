import os

from utils import logger
from reporter.reporter import Reporter


class GSheetsReporter(Reporter):
    """Url reader for txt files

    :type filename: str
    :param filename: Name of the output file
    """

    def __init__(self, filename: str) -> None:

        self._filename = filename

    def update_views(self, videos: list["YoutubeVideo"]) -> None:
        """Update view counts for videos on the output file

        :type videos: list
        :param videos: List of videos
        """

        pass
