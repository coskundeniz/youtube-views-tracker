from pytube import Channel

from utils import logger
from urlreader.urlreader import UrlReader


class ChannelReader(UrlReader):
    """Url reader for channel videos

    :type channel_urls: list
    :param channel_urls: List of channel names
    """

    def __init__(self, channel_urls: list[str]) -> None:

        # TODO: get first 3 or 5 according to package
        self._channel_urls = channel_urls

    def read_urls(self) -> list:
        """Extract video urls from given channels

        :rtype: list
        :returns: List of video urls
        """

        urls = []
        for channel_url in self._channel_urls:
            logger.info(f"Reading video urls from {channel_url}...")
            channel = self._construct_channel(channel_url.strip())
            urls.extend(channel.video_urls)

        return urls

    def _construct_channel(self, channel_url: str) -> Channel:
        """Construct channel object from channel url

        :type channel_url: str
        :param channel_url: Channel url
        :rtype: Channel
        :returns: Channel instance
        """

        return Channel(channel_url)
