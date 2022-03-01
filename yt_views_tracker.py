from argparse import ArgumentParser

from pytube import YouTube, Channel

from factory.urlreader_factory import UrlReaderFactory
from utils import logger
from yt_views import YoutubeViews


# https://pytube.io/en/latest/api.html#module-pytube.exceptions

# TODO: Get views for a list of video URLs (URLs can be read from txt, csv, xlsx, or Google Sheets)


def get_views_from_urls(urls):

    for url in urls:
        video = YouTube(url)
        print(
            f"Title: {video.title} - Views Count: {video.views}, Length: {video.length}"
        )


def get_views_from_channel(channel_url):

    mychannel = Channel(channel_url)

    print(f"Channel name: {mychannel.channel_name}")

    for video in mychannel.videos:
        print(f"Title: {video.title} - Views Count: {video.views}")


def get_arg_parser() -> ArgumentParser:
    """Get argument parser

    :rtype: ArgumentParser
    :returns: ArgumentParser object
    """

    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-c", "--useconfig", action="store_true", help="Read configuration from file"
    )
    arg_parser.add_argument("-f", "--urlsfile", help="File to read urls")

    return arg_parser


def main():

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    # read urls from txt, csv, or xlsx
    url_reader = UrlReaderFactory.get_urlreader(args)
    video_urls = url_reader.read_urls()

    # get view counts for the urls
    views = YoutubeViews(video_urls=video_urls)
    views.update()

    for v in views.videos:
        # logger.info(f"Title: {v.title} - Url: {v.url} - Views Count: {v.views}")
        logger.info(f"Title: {v.title} - Views Count: {v.views}")

    # update views on Excel


if __name__ == "__main__":

    main()
