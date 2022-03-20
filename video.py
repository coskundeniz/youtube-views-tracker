from dataclasses import dataclass


@dataclass
class YoutubeVideo:

    url: str
    title: str
    views: int

    def __str__(self) -> str:

        return f"{self.views}, {self.title}, {self.url}"
