import pytest

from exceptions import MissingShareMailError
from reporter.gsheets_reporter import GSheetsReporter
from video import YoutubeVideo


@pytest.fixture
def reporter():

    output_file = "test_views"
    share_mail = "codenineeight@gmail.com"
    reporter = GSheetsReporter(output_file, share_mail)
    yield reporter

    gsheet = reporter._get_sheet()
    reporter._sheets_client.del_spreadsheet(gsheet.id)


@pytest.fixture
def reporter_with_url():

    output_file = "test_views_url"
    share_mail = "codenineeight@gmail.com"
    reporter = GSheetsReporter(output_file, share_mail)
    yield reporter

    gsheet = reporter._get_sheet()
    reporter._sheets_client.del_spreadsheet(gsheet.id)


@pytest.fixture
def videos():

    return [
        YoutubeVideo(
            url="https://www.youtube.com/watch?v=gxUq5Kt83V4",
            title="Darbuka solo before class",
            views=185,
        ),
        YoutubeVideo(
            url="https://www.youtube.com/watch?v=3T4uDDfR43Y",
            title="Thursday Memories",
            views=208,
        ),
        YoutubeVideo(
            url="https://www.youtube.com/watch?v=G0f9ms4tPjI",
            title="Dehollo - I",
            views=41,
        ),
    ]


def test_create_reporter_without_share_mail():

    with pytest.raises(MissingShareMailError):
        GSheetsReporter("test_views", None)


def test_create_gsheets_report(reporter, videos):

    reporter.update_views(videos)

    gsheet = reporter._get_sheet()
    worksheet = gsheet.sheet1

    total_rows = len(worksheet.get_values())

    assert total_rows == 3
    assert worksheet.cell(1, 2).value == videos[0].title
    assert worksheet.cell(2, 3).value == videos[1].url
    assert worksheet.cell(3, 1).value == str(videos[2].views)


def test_create_gsheets_report_with_existing_report(reporter, videos):

    reporter.update_views(videos)
    reporter.update_views(videos)

    gsheet = reporter._get_sheet()
    worksheet = gsheet.sheet1

    total_rows = len(worksheet.get_values())

    assert total_rows == 3
    assert worksheet.cell(1, 2).value == videos[0].title
    assert worksheet.cell(2, 3).value == videos[1].url
    assert worksheet.cell(3, 1).value == str(videos[2].views)


def test_create_gsheets_report_with_url(reporter_with_url, videos):

    output_file = reporter_with_url._get_sheet().url
    share_mail = "codenineeight@gmail.com"
    reporter = GSheetsReporter(output_file, share_mail)

    reporter.update_views(videos)

    gsheet = reporter._get_sheet()
    worksheet = gsheet.sheet1

    total_rows = len(worksheet.get_values())

    assert total_rows == 3
    assert worksheet.cell(1, 2).value == videos[0].title
    assert worksheet.cell(2, 3).value == videos[1].url
    assert worksheet.cell(3, 1).value == str(videos[2].views)
