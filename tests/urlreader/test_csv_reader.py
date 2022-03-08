import pytest

from exceptions import EmptyUrlListError
from urlreader.csv_reader import CsvReader


def test_read_urls_from_default_column():

    reader = CsvReader("tests/urlreader/urls_default.csv", 0)
    urls = reader.read_urls()

    assert len(urls) == 6


def test_read_urls_from_given_column():

    reader = CsvReader("tests/urlreader/urls_diff_column.csv", 1)
    urls = reader.read_urls()

    assert len(urls) == 6
    assert urls[0] == "https://www.youtube.com/watch?v=mM2-FPm1EhI"


def test_read_empty_url_list():

    with pytest.raises(EmptyUrlListError):
        reader = CsvReader("tests/urlreader/empty_urls.csv", 0)
        reader.read_urls()


def test_read_empty_url_list_from_given_column():

    with pytest.raises(EmptyUrlListError):
        reader = CsvReader("tests/urlreader/urls_diff_column_empty.csv", 1)
        reader.read_urls()
