import pytest

from exceptions import UrlFileDoesNotExistError
from urlreader.urlreader import UrlReader
from urlreader.txt_reader import TxtReader


def test_non_existing_file():

    with pytest.raises(UrlFileDoesNotExistError):
        UrlReader.check_file_exists("non_existing_filepath.txt")


def test_read_urls():

    reader = TxtReader("tests/urlreader/urls.txt")
    urls = reader.read_urls()

    assert len(urls) == 6
