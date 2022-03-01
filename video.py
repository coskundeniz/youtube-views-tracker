from dataclasses import dataclass


@dataclass
class YoutubeVideo:

    url: str
    title: str
    views: int
