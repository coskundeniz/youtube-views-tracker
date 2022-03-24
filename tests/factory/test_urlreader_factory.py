import pytest

from exceptions import UnsupportedUrlFileError
from factory.urlreader_factory import UrlReaderFactory
from urlreader.txt_reader import TxtReader
from urlreader.csv_reader import CsvReader
from urlreader.xlsx_reader import ExcelReader
from yt_views_tracker import get_arg_parser


@pytest.fixture
def config_data():

    return {
        "txt": {"urlsfile": "tests/urlreader/urls.txt"},
        "csv": {
            "urlsfile": "tests/urlreader/urls_default.csv",
            "urlsfile_diff_column": "tests/urlreader/urls_diff_column.csv",
        },
        "xlsx": {
            "urlsfile": "tests/urlreader/urls_default.xlsx",
            "urlsfile_diff_column": "tests/urlreader/urls_diff_column.xlsx",
        },
        "output_type": "excel",
        "output_file": "test_results.xlsx",
        "url_column": "0",
        "url_diff_column": "1",
    }


@pytest.fixture
def arg_parser():
    return get_arg_parser()


def test_unsupported_input_file_type(arg_parser):

    with pytest.raises(UnsupportedUrlFileError):

        args = arg_parser.parse_args(["-f", "tests/urls.xml"])
        UrlReaderFactory.get_urlreader(args)


def test_get_urlreader_for_txt(arg_parser, config_data):

    args = arg_parser.parse_args(["-f", config_data["txt"]["urlsfile"]])

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, TxtReader)


def test_get_urlreader_for_txt_using_configfile(arg_parser):

    args = arg_parser.parse_args(["--useconfig"])

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, TxtReader)


def test_get_urlreader_for_csv(arg_parser, config_data):

    args = arg_parser.parse_args(["-f", config_data["csv"]["urlsfile"]])

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, CsvReader)
    assert reader._url_column == 0


def test_get_urlreader_for_csv_diff_column(arg_parser, config_data):

    args = arg_parser.parse_args(
        ["-f", config_data["csv"]["urlsfile_diff_column"], "-uc", config_data["url_diff_column"]]
    )

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, CsvReader)
    assert reader._url_column == 1


def test_get_urlreader_for_xlsx(arg_parser, config_data):

    args = arg_parser.parse_args(["-f", config_data["xlsx"]["urlsfile"]])

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, ExcelReader)
    assert reader._url_column == 0


def test_get_urlreader_for_xlsx_diff_column(arg_parser, config_data):

    args = arg_parser.parse_args(
        ["-f", config_data["xlsx"]["urlsfile_diff_column"], "-uc", config_data["url_diff_column"]]
    )

    reader = UrlReaderFactory.get_urlreader(args)

    assert isinstance(reader, ExcelReader)
    assert reader._url_column == 1
