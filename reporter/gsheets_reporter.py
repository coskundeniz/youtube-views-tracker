from typing import TYPE_CHECKING

import gspread
from gspread.spreadsheet import Spreadsheet
from gspread.exceptions import SpreadsheetNotFound

from exceptions import MissingShareMailError
from utils import logger
from reporter.reporter import Reporter


if TYPE_CHECKING:  # pragma: no cover
    from video import YoutubeVideo


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
        self._gsheet = None

    def update_views(self, videos: list["YoutubeVideo"]) -> None:
        """Update view counts for videos on the output file

        :type videos: list
        :param videos: List of videos
        """

        gsheet = self._get_sheet()

        logger.info(f"Updating view counts on {self._filename}...")

        worksheet = gsheet.sheet1

        update_range = f"A1:C{len(videos)}"
        values = []

        for video in videos:
            values.append([video.views, video.title, video.url])

        worksheet.batch_update(
            [
                {
                    "range": update_range,
                    "values": values,
                }
            ]
        )

        worksheet.columns_auto_resize(start_column_index=1, end_column_index=3)

    def _get_sheet(self) -> Spreadsheet:
        """Create or open spreadsheet

        :rtype: Spreadsheet
        :returns: Spreadsheet instance
        """

        if self._gsheet is None:
            try:
                logger.info(f"Opening sheet {self._filename}...")

                if "docs.google.com" in self._filename:
                    self._gsheet = self._sheets_client.open_by_url(self._filename)
                else:
                    self._gsheet = self._sheets_client.open(self._filename)

            except SpreadsheetNotFound:
                logger.error(f"Spreadsheet could not be found with name: {self._filename}")
                logger.info(f"Creating a sheet with name: {self._filename}")
                self._gsheet = self._sheets_client.create(self._filename)

                self._gsheet.share(self._share_mail, perm_type="user", role="writer")

        return self._gsheet
