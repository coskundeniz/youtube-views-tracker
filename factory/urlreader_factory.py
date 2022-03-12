from exceptions import UnsupportedUrlFileError
from urlreader import urlreader
from urlreader.txt_reader import TxtReader
from urlreader.csv_reader import CsvReader
from urlreader.xlsx_reader import ExcelReader
from urlreader.gsheets_reader import GSheetsReader
from urlreader.channel_reader import ChannelReader
from utils import get_configuration


class UrlReaderFactory:
    """Factory class for url readers"""

    @staticmethod
    def get_urlreader(cmdline_args: "Namespace") -> urlreader.UrlReader:  # noqa: F821
        """Get specific url reader according to filetype

        If urlsfile argument is empty, channels will be used.

        Raises UnsupportedUrlFileError if file extension is not supported.

        :type cmdline_args: Namespace
        :param cmdline_args: Command line args returned by ArgumentParser
        :rtype: urlreader.UrlReader
        :returns: Concrete UrlReader object
        """

        reader = None

        config = get_configuration(cmdline_args.configfile)

        if cmdline_args.useconfig:
            url_file = config["urlsfile"]
        else:
            url_file = cmdline_args.urlsfile

        if not url_file:
            if cmdline_args.useconfig:
                channels = config["channels"]
            else:
                channels = cmdline_args.channels.split(",")
            reader = ChannelReader(channels)

        elif url_file.endswith(".txt"):
            reader = TxtReader(url_file)

        elif url_file.endswith(".csv"):
            url_column = UrlReaderFactory._get_url_column(cmdline_args, config)
            reader = CsvReader(url_file, url_column)

        elif url_file.endswith(".xlsx"):
            url_column = UrlReaderFactory._get_url_column(cmdline_args, config)
            reader = ExcelReader(url_file, url_column)

        elif url_file.startswith("gsheets-"):
            url_file = url_file.split("gsheets-")[1]
            url_column = UrlReaderFactory._get_url_column(cmdline_args, config)
            reader = GSheetsReader(url_file, url_column)

        else:
            message = "Unsupported url input file! Should be one of txt, csv, or xlsx"
            raise UnsupportedUrlFileError(message)

        return reader

    @staticmethod
    def _get_url_column(cmdline_args: "Namespace", config: dict) -> int:  # noqa: F821
        """Get url_column parameter

        :type cmdline_args: Namespace
        :param cmdline_args: Command line args returned by ArgumentParser
        :type config: dict
        :param config: Configuration as dict
        :rtype: int
        :returns: Url column index
        """

        url_column = config["url_column"] if cmdline_args.useconfig else cmdline_args.url_column

        return url_column
