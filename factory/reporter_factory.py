from exceptions import UnsupportedOutputFileError
from reporter import reporter
from reporter.excel_reporter import ExcelReporter
from reporter.gsheets_reporter import GSheetsReporter
from utils import get_configuration


class ReporterFactory:
    """Factory class for url readers"""

    @staticmethod
    def get_reporter(cmdline_args) -> reporter.Reporter:
        """Get specific reporter

        Raises UnsupportedOutputFileError if output format is not supported.

        :type cmdline_args: Namespace
        :param cmdline_args: Command line args returned by ArgumentParser
        :rtype: urlreader.UrlReader
        :returns: Concrete UrlReader object
        """

        reporter = None

        if cmdline_args.useconfig:
            config = get_configuration()
            output_type = config["output_type"]
            output_file = config["output_file"]
        else:
            output_type = cmdline_args.output_type
            output_file = cmdline_args.output_file

        if output_type == "excel":
            reporter = ExcelReporter(output_file)
        elif output_type == "gsheets":
            reporter = GSheetsReporter(output_file)
        else:
            message = "Unsupported output file! Should be one of excel, gsheets"
            raise UnsupportedOutputFileError(message)

        return reporter