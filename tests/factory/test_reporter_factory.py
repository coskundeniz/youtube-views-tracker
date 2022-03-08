import pytest

from exceptions import UnsupportedOutputFileError
from factory.reporter_factory import ReporterFactory
from reporter.excel_reporter import ExcelReporter
from reporter.gsheets_reporter import GSheetsReporter
from yt_views_tracker import get_arg_parser


@pytest.fixture
def config_data():

    return {
        "excel": {
            "output_type": "excel",
        },
        "gsheets": {
            "output_type": "gsheets",
        },
    }


@pytest.fixture
def arg_parser():
    return get_arg_parser()


def test_unsupported_output_file_type(arg_parser):

    with pytest.raises(UnsupportedOutputFileError):

        args = arg_parser.parse_args(["-ot", "xml"])
        ReporterFactory.get_reporter(args)


def test_get_reporter_for_excel(arg_parser, config_data):

    args = arg_parser.parse_args(["-ot", config_data["excel"]["output_type"]])

    reader = ReporterFactory.get_reporter(args)

    assert isinstance(reader, ExcelReporter)


def test_get_reporter_for_gsheets(arg_parser, config_data):

    args = arg_parser.parse_args(["-ot", config_data["gsheets"]["output_type"]])

    reader = ReporterFactory.get_reporter(args)

    assert isinstance(reader, GSheetsReporter)
