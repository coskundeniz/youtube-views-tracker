import gspread
from gspread.spreadsheet import Spreadsheet
from gspread.exceptions import SpreadsheetNotFound

from exceptions import UrlFileDoesNotExistError, EmptyUrlListError
from utils import logger
from urlreader.urlreader import UrlReader


class GSheetsReader(UrlReader):
    """Url reader for Google Sheets

    :type filename: str
    :param filename: Name or url of the output file containing video urls
    :type url_column: int
    :param url_column: Url column index
    """

    def __init__(self, filename: str, url_column: int) -> None:

        self._filename = filename
        self._url_column = url_column
        self._sheets_client = gspread.service_account(filename="credentials.json")
        self._gsheet = None

    def read_urls(self):
        """Read urls from file

        :rtype: list
        :returns: List of video urls
        """

        gsheet = self._get_sheet()
        worksheet = gsheet.sheet1

        logger.info(f"Reading video urls from {self._filename}...")

        urls = worksheet.col_values(self._url_column + 1)

        logger.debug(f"Number of rows: {len(urls)}")

        if not urls:
            raise EmptyUrlListError("Video url list is empty! Please provide urls.")

        return urls

    def _get_sheet(self) -> Spreadsheet:
        """Open and return spreadsheet

        Raises UrlFileDoesNotExistError if file does not exist.

        :rtype: Spreadsheet
        :returns: Spreadsheet instance
        """

        try:
            logger.info(f"Opening sheet {self._filename}...")

            if self._gsheet is None:
                if "docs.google.com" in self._filename:
                    self._gsheet = self._sheets_client.open_by_url(self._filename)
                else:
                    self._gsheet = self._sheets_client.open(self._filename)

            return self._gsheet

        except SpreadsheetNotFound:
            message = f"Url file {self._filename} does not exist!"
            raise UrlFileDoesNotExistError(message)
