import os
from abc import ABC, abstractmethod

from exceptions import UrlFileDoesNotExistError


class UrlReader(ABC):
    """Base class for url readers"""

    @abstractmethod
    def read_urls(self) -> list:
        """Read urls from file"""

    def check_file_exists(self, filepath: str) -> None:
        """Check if given filepath exists

        Raises UrlFileDoesNotExistError if file does not exist.

        :type filepath: str
        :param filepath: Path of the input file
        """

        if not os.path.exists(filepath):
            message = f"Url file {filepath} does not exist!"
            raise UrlFileDoesNotExistError(message)
