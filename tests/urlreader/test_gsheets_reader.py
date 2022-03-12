import pytest

from exceptions import UrlFileDoesNotExistError, EmptyUrlListError
from urlreader.gsheets_reader import GSheetsReader


def test_nonexisting_file():

    with pytest.raises(UrlFileDoesNotExistError):
        reader = GSheetsReader("non_existing_file", 0)
        reader.read_urls()


def test_read_urls_from_default_column():

    reader = GSheetsReader("video_urls_test", 0)
    urls = reader.read_urls()

    assert len(urls) == 6


def test_read_urls_from_given_column():

    reader = GSheetsReader("video_urls_test_diff_column", 1)
    urls = reader.read_urls()

    assert len(urls) == 6
    assert urls[0] == "https://www.youtube.com/watch?v=mM2-FPm1EhI"


def test_read_empty_url_list_from_given_column():

    with pytest.raises(EmptyUrlListError):
        reader = GSheetsReader("video_urls_test", 1)
        reader.read_urls()


def test_read_urls_with_inputfile_as_url():

    reader = GSheetsReader("video_urls_test", 0)

    input_file_url = reader._get_sheet().url
    reader_with_url = GSheetsReader(input_file_url, 0)

    urls = reader_with_url.read_urls()

    assert len(urls) == 6
    assert urls[0] == "https://www.youtube.com/watch?v=mM2-FPm1EhI"
