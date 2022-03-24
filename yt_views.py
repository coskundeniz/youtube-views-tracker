from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from utils import logger
from video import YoutubeVideo


class YoutubeViews:
    """Get view counts for given video urls

    :type video_urls: list
    :param video_urls: List of video urls
    """

    def __init__(
        self,
        *,
        video_urls: Optional[list[str]] = None,
    ) -> None:

        self._video_urls = video_urls
        self._videos = []

    def update(self) -> None:
        """Update views of all videos"""

        num_workers = self._get_max_workers()

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            results = executor.map(self._update_view, self._video_urls)

            for result in results:
                if result:
                    self._videos.append(result)
                    logger.debug(result)

    def _update_view(self, video_url: str) -> Optional[YoutubeVideo]:
        """Get title and view count information for the given video url

        Raises VideoUnavailable if video is not accessible or PytubeError
        for other issues.

        :type video_url: str
        :param video_url: Video url
        :rtype: YoutubeVideo or None
        :returns: YoutubeVideo if video is available, otherwise None
        """

        youtube_video = None
        try:
            video = YouTube(video_url)
            youtube_video = YoutubeVideo(video_url, video.title, video.views)
        except VideoUnavailable:
            logger.error(f"Video {video_url} is unavailable, skipping...")

        return youtube_video

    @property
    def videos(self) -> list[YoutubeVideo]:
        """Return all video objects

        :rtype: list
        :returns: List of all videos
        """

        return self._videos

    def _get_max_workers(self) -> int:
        """Calculate number of workers

        :rtype: int
        :returns: Max number of threads to be used
        """

        workers = 0
        num_urls = len(self._video_urls)

        if num_urls <= 100:
            workers = num_urls
        else:
            workers = (num_urls / 10) * 2

        return workers
