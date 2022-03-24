from argparse import ArgumentParser

from exceptions import (
    YTViewsTrackerException,
    UnsupportedUrlFileError,
    UrlFileDoesNotExistError,
    UnsupportedOutputFileError,
    EmptyUrlListError,
    MissingShareMailError,
    UnsupportedConfigFileError,
)
from factory.urlreader_factory import UrlReaderFactory
from factory.reporter_factory import ReporterFactory
from utils import logger
from yt_views import YoutubeViews


__author__ = "Coşkun Deniz <codenineeight@gmail.com>"


def handle_exception(exp: YTViewsTrackerException) -> None:
    """Print the error message and exit

    :type exp: YTViewsTrackerException
    :param exp: Exception raised by the views tracker components
    """

    logger.error(exp)
    raise SystemExit() from exp


def get_arg_parser() -> ArgumentParser:
    """Get argument parser

    :rtype: ArgumentParser
    :returns: ArgumentParser object
    """

    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-c", "--useconfig", action="store_true", help="Read configuration from config.json file"
    )
    arg_parser.add_argument(
        "-cf",
        "--configfile",
        default="config.json",
        help="Read configuration from given file",
    )
    arg_parser.add_argument("-f", "--urlsfile", help="File to read video urls")
    arg_parser.add_argument(
        "-ot", "--output_type", default="excel", help="Output file type (one of excel, gsheets)"
    )
    arg_parser.add_argument("-of", "--output_file", default="results.xlsx", help="Output file name")
    arg_parser.add_argument(
        "-uc",
        "--url_column",
        type=int,
        default=0,
        help="Url column index for csv, xlsx, or Google Sheets input",
    )

    return arg_parser


def main(args) -> None:
    """Entry point for the tool

    :type args: Namespace
    :pram args: Command line args returned by ArgumentParser
    """

    if not (args.urlsfile or args.channels or args.useconfig):
        arg_parser.print_help()
        raise SystemExit("Missing parameter!")

    try:
        url_reader = UrlReaderFactory.get_urlreader(args)
    except (UnsupportedUrlFileError, UnsupportedConfigFileError) as exp:
        handle_exception(exp)

    # read video urls from txt, csv, xlsx, Google Sheets file or channel links
    try:
        video_urls = url_reader.read_urls()
    except (UrlFileDoesNotExistError, EmptyUrlListError) as exp:
        handle_exception(exp)

    try:
        reporter = ReporterFactory.get_reporter(args)
    except (UnsupportedOutputFileError, MissingShareMailError, UnsupportedConfigFileError) as exp:
        handle_exception(exp)

    # get/update view counts for the urls
    yt_views = YoutubeViews(video_urls=video_urls)
    yt_views.update()

    # update views on Excel or Google Sheets
    reporter.update_views(yt_views.videos)

    logger.info("Completed views update.")


if __name__ == "__main__":

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        logger.info("Program ended manually.")
