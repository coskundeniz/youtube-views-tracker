from abc import ABC, abstractmethod


class UrlReader(ABC):
    """Base class for url readers"""

    @abstractmethod
    def read_urls(self) -> list:
        """Read urls from file"""
