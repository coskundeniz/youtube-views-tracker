from argparse import ArgumentParser

from pytube import YouTube, Channel

from exceptions import (
    YTViewsTrackerException,
    UnsupportedUrlFileError,
    UrlFileDoesNotExistError,
    UnsupportedOutputFileError,
)
from factory.urlreader_factory import UrlReaderFactory
from factory.reporter_factory import ReporterFactory
from utils import logger
from yt_views import YoutubeViews


# https://pytube.io/en/latest/api.html#module-pytube.exceptions

# TODO: Get views for a list of video URLs (URLs can be read from txt, csv, xlsx, or Google Sheets)


def get_views_from_urls(urls):

    for url in urls:
        video = YouTube(url)
        print(f"Title: {video.title} - Views Count: {video.views}, Length: {video.length}")


def get_views_from_channel(channel_url):

    mychannel = Channel(channel_url)

    print(f"Channel name: {mychannel.channel_name}")
    print(f"Number of videos: {len(mychannel.videos)}")
    print(f"Number of video_urls: {len(mychannel.video_urls)}")

    for video in mychannel.videos:
        print(f"Title: {video.title} - Views Count: {video.views}")


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
        "-c", "--useconfig", action="store_true", help="Read configuration from file"
    )
    arg_parser.add_argument("-f", "--urlsfile", help="File to read video urls")
    arg_parser.add_argument("-ch", "--channels", help="Channel names separated by comma")
    arg_parser.add_argument("-ot", "--output_type", default="excel", help="Output file type")
    arg_parser.add_argument("-of", "--output_file", default="results.xlsx", help="Output file name")

    return arg_parser


def main():

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    if not (args.urlsfile or args.useconfig):
        arg_parser.print_help()
        raise SystemExit("Missing parameter!")

    # read video urls from txt, csv, or xlsx file
    try:
        url_reader = UrlReaderFactory.get_urlreader(args)
        reporter = ReporterFactory.get_reporter(args)
    except (
        UnsupportedUrlFileError,
        UnsupportedOutputFileError,
    ) as exp:
        handle_exception(exp)

    try:
        video_urls = url_reader.read_urls()
        # video_urls = Channel("https://www.youtube.com/c/ArjanCodes/").video_urls
    except UrlFileDoesNotExistError as exp:
        handle_exception(exp)

    # get/update view counts for the urls
    yt_views = YoutubeViews(video_urls=video_urls)
    yt_views.update()

    # update views on Excel
    reporter.update_views(yt_views.videos)


if __name__ == "__main__":

    main()
