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
