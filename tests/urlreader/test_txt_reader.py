import pytest

from exceptions import UrlFileDoesNotExistError, EmptyUrlListError
from urlreader.urlreader import UrlReader
from urlreader.txt_reader import TxtReader


def test_non_existing_file():

    with pytest.raises(UrlFileDoesNotExistError):
        UrlReader.check_file_exists("non_existing_filepath.txt")


def test_read_urls():

    reader = TxtReader("tests/urlreader/urls.txt")
    urls = reader.read_urls()

    assert len(urls) == 6


def test_read_empty_url_list():

    with pytest.raises(EmptyUrlListError):
        reader = TxtReader("tests/urlreader/empty_urls.txt")
        reader.read_urls()


def test_read_more_than_1000_urls():

    reader = TxtReader("tests/urlreader/video_urls_more_than_1000.txt")
    urls = reader.read_urls()

    assert len(urls) == 1000
