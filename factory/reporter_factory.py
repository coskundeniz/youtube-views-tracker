from exceptions import UnsupportedOutputFileError
from reporter import reporter
from reporter.excel_reporter import ExcelReporter
from reporter.gsheets_reporter import GSheetsReporter
from utils import get_configuration


class ReporterFactory:
    """Factory class for reporters"""

    @staticmethod
    def get_reporter(cmdline_args: "Namespace") -> reporter.Reporter:  # noqa: F821
        """Get specific reporter

        Raises UnsupportedOutputFileError if output format is not supported.

        :type cmdline_args: Namespace
        :param cmdline_args: Command line args returned by ArgumentParser
        :rtype: reporter.Reporter
        :returns: Concrete Reporter object
        """

        reporter = None

        config = get_configuration(cmdline_args.configfile)

        if cmdline_args.useconfig:
            output_type = config["output_type"]
            output_file = config["output_file"]
        else:
            output_type = cmdline_args.output_type
            output_file = cmdline_args.output_file

        if output_type == "excel":
            reporter = ExcelReporter(output_file)

        elif output_type == "gsheets":
            share_mail = config["share_mail"] if cmdline_args.useconfig else cmdline_args.share_mail
            reporter = GSheetsReporter(output_file, share_mail)

        else:
            message = "Unsupported output file! Should be one of excel, gsheets"
            raise UnsupportedOutputFileError(message)

        return reporter
