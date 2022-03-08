import openpyxl

from utils import logger
from reporter.reporter import Reporter


class ExcelReporter(Reporter):
    """Excel report generator

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

        titles = [video.title for video in videos]
        urls = [video.url for video in videos]
        self._adjust_column_width(sheet, "B", titles)
        self._adjust_column_width(sheet, "C", urls)

        workbook.save(self._filename)

    def _adjust_column_width(self, sheet: "Worksheet", column: str, contents: list[str]) -> None:
        """Adjust the width of given column according to maximum length of content

        :type sheet: Worksheet
        :param sheet: Active worksheet object
        :type column: str
        :param column: Column name
        :type contents: list
        :param contents: Column contents
        """

        max_content_length = max([len(content) for content in contents])
        sheet.column_dimensions[column].width = max_content_length + 2
