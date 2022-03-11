import gspread
from gspread.spreadsheet import Spreadsheet
from gspread.exceptions import SpreadsheetNotFound

from exceptions import MissingShareMailError
from utils import logger
from reporter.reporter import Reporter


class GSheetsReporter(Reporter):
    """Google Sheets report generator

    :type filename: str
    :param filename: Name or url of the output file
    :type share_mail: str
    :param share_mail: Mail address to share Google Sheets document
    """

    def __init__(self, filename: str, share_mail: str) -> None:

        self._filename = filename
        self._share_mail = share_mail
        if not self._share_mail:
            raise MissingShareMailError("share_mail(sm) parameter is missing!")

        self._sheets_client = gspread.service_account(filename="credentials.json")

    def update_views(self, videos: list["YoutubeVideo"]) -> None:
        """Update view counts for videos on the output file

        :type videos: list
        :param videos: List of videos
        """

        gsheet = self._get_sheet()

        logger.info(f"Updating view counts on {self._filename}...")

        worksheet = gsheet.sheet1

        for index, video in enumerate(videos, start=1):

            worksheet.update_cell(row=index, col=1, value=video.views)
            worksheet.update_cell(row=index, col=2, value=video.title)
            worksheet.update_cell(row=index, col=3, value=video.url)

        worksheet.columns_auto_resize(start_column_index=1, end_column_index=3)

    def _get_sheet(self) -> Spreadsheet:
        """Create or open spreadsheet

        :rtype: Spreadsheet
        :returns: Spreadsheet instance
        """

        try:
            logger.info(f"Opening sheet {self._filename}...")

            if "docs.google.com" in self._filename:
                gsheet = self._sheets_client.open_by_url(self._filename)
            else:
                gsheet = self._sheets_client.open(self._filename)

        except SpreadsheetNotFound:
            logger.error(f"Spreadsheet could not be found with name: {self._filename}")
            logger.info(f"Creating a sheet with name: {self._filename}")
            gsheet = self._sheets_client.create(self._filename)

            gsheet.share(self._share_mail, perm_type="user", role="writer")

        return gsheet
