import pytest

from urlreader.channel_reader import ChannelReader


@pytest.fixture
def channel_urls():

    return ["https://www.youtube.com/user/coskundenize"]


def test_read_urls_from_valid_channel(channel_urls):

    reader = ChannelReader(channel_urls)
    urls = reader.read_urls()

    assert len(urls) >= 12


def test_read_urls_from_invalid_channel(capfd, channel_urls):

    reader = ChannelReader([channel_urls[0] + "xX"])
    urls = reader.read_urls()

    _, err = capfd.readouterr()

    assert len(urls) == 0
    assert f"Invalid channel url: {channel_urls[0] + 'xX'} Skipping..." in err
