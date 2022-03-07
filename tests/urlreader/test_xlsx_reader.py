from urlreader.xlsx_reader import ExcelReader


def test_read_urls_from_default_column():

    reader = ExcelReader("tests/urlreader/urls_default.xlsx", 0)
    urls = reader.read_urls()

    assert len(urls) == 6


def test_read_urls_from_given_column():

    reader = ExcelReader("tests/urlreader/urls_diff_column.xlsx", 1)
    urls = reader.read_urls()

    assert len(urls) == 6
    assert urls[0] == "https://www.youtube.com/watch?v=mM2-FPm1EhI"
