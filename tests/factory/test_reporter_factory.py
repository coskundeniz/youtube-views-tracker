import pytest

from exceptions import UnsupportedOutputFileError, MissingShareMailError
from factory.reporter_factory import ReporterFactory
from reporter.excel_reporter import ExcelReporter
from reporter.gsheets_reporter import GSheetsReporter
from yt_views_tracker import get_arg_parser


@pytest.fixture
def config_data():

    return {
        "excel": {"output_type": "excel"},
        "gsheets": {"output_type": "gsheets", "share_mail": "codenineeight@gmail.com"},
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


def test_get_reporter_for_excel_using_configfile(arg_parser):

    args = arg_parser.parse_args(["--useconfig"])

    reader = ReporterFactory.get_reporter(args)

    assert isinstance(reader, ExcelReporter)


def test_get_reporter_for_gsheets(arg_parser, config_data):

    args = arg_parser.parse_args(
        ["-ot", config_data["gsheets"]["output_type"], "-sm", config_data["gsheets"]["share_mail"]]
    )

    reader = ReporterFactory.get_reporter(args)

    assert isinstance(reader, GSheetsReporter)


def test_get_reporter_for_gsheets_with_missing_share_mail(arg_parser, config_data):

    args = arg_parser.parse_args(["-ot", config_data["gsheets"]["output_type"]])

    with pytest.raises(MissingShareMailError):
        ReporterFactory.get_reporter(args)
