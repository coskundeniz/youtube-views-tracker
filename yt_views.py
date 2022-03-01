from typing import Optional

from pytube import YouTube, Channel

# from video import YoutubeVideo


class YoutubeViews:
    """Get view counts for given urls or channel videos

    :type video_urls: list
    :param video_urls: List of video urls
    :type channels: list
    :param channels: List of channel names
    """

    def __init__(
        self,
        *,
        video_urls: Optional[list[str]] = None,
        channels: Optional[list[str]] = None,
    ) -> None:

        self._video_urls = video_urls
        self._channels = channels
        self._videos = []

    def update(self):

        self._videos = [YouTube(url) for url in self._video_urls]

    @property
    def videos(self) -> list[YouTube]:

        return self._videos
