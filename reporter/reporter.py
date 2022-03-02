from abc import ABC, abstractmethod


class Reporter(ABC):
    """Base class for reporters"""

    @abstractmethod
    def update_views(self, videos) -> None:
        """Update view counts for videos on the output file"""
