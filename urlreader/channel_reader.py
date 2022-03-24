from pytube import Channel
from urllib.error import HTTPError

from utils import logger
from urlreader.urlreader import UrlReader


class ChannelReader(UrlReader):
    """Url reader for channel videos

    :type channel_urls: list
    :param channel_urls: List of channel names
    """

    def __init__(self, channel_urls: list[str]) -> None:

        self._channel_urls = channel_urls

        if len(self._channel_urls) > 5:
            max_channels = UrlReader.MAX_CHANNEL_COUNT
            logger.warning(
                f"Max number of channels reached! Using first {max_channels} channels..."
            )
            self._channel_urls = channel_urls[:max_channels]

    def read_urls(self) -> list[str]:
        """Extract video urls from given channels

        :rtype: list
        :returns: List of video urls
        """

        urls = []
        for channel_url in self._channel_urls:
            logger.info(f"Reading video urls from {channel_url}...")
            channel = self._construct_channel(channel_url.strip())

            try:
                urls.extend(channel.video_urls)
            except HTTPError:
                logger.error(f"Invalid channel url: {channel_url} Skipping...")

        return urls

    def _construct_channel(self, channel_url: str) -> Channel:
        """Construct channel object from channel url

        :type channel_url: str
        :param channel_url: Channel url
        :rtype: Channel
        :returns: Channel instance
        """

        return Channel(channel_url)
