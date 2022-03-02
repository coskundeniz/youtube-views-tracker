import os

import openpyxl

from utils import logger
from reporter.reporter import Reporter

# https://www.geeksforgeeks.org/working-with-excel-spreadsheets-in-python/


class ExcelReporter(Reporter):
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

        logger.info(f"Updating view counts on {self._filename}...")

        workbook = openpyxl.Workbook()

        sheet = workbook.active

        for index, video in enumerate(videos, start=1):

            views_cell = sheet.cell(row=index, column=1)
            title_cell = sheet.cell(row=index, column=2)
            url_cell = sheet.cell(row=index, column=3)

            views_cell.value = video.views
            title_cell.value = video.title
            url_cell.value = video.url

        workbook.save(self._filename)
