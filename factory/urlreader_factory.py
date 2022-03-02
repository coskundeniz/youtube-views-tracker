from exceptions import UnsupportedUrlFileError
from urlreader import urlreader
from urlreader.txt_reader import TxtReader
from urlreader.csv_reader import CsvReader
from urlreader.xlsx_reader import ExcelReader
from utils import get_configuration


class UrlReaderFactory:
    """Factory class for url readers"""

    @staticmethod
    def get_urlreader(cmdline_args) -> urlreader.UrlReader:
        """Get specific url reader according to filetype

        Raises UnsupportedUrlFileError if file extension is not supported.

        :type cmdline_args: Namespace
        :param cmdline_args: Command line args returned by ArgumentParser
        :rtype: urlreader.UrlReader
        :returns: Concrete UrlReader object
        """

        reader = None

        if cmdline_args.useconfig:
            config = get_configuration()
            url_file = config["urlsfile"]
        else:
            url_file = cmdline_args.urlsfile

        if url_file.endswith(".txt"):
            reader = TxtReader(url_file)
        elif url_file.endswith(".csv"):
            reader = CsvReader(url_file)
        elif url_file.endswith(".xlsx"):
            reader = ExcelReader(url_file)
        else:
            message = "Unsupported url input file! Should be one of txt, csv, or xlsx"
            raise UnsupportedUrlFileError(message)

        return reader
