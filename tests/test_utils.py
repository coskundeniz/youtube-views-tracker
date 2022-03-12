import pytest

from utils import get_configuration


@pytest.fixture
def config_data():
    return get_configuration()


def test_config_keys(config_data):

    assert "urlsfile" in config_data.keys()
    assert "channels" in config_data.keys()
    assert "output_type" in config_data.keys()
    assert "output_file" in config_data.keys()
    assert "url_column" in config_data.keys()
    assert "share_mail" in config_data.keys()


def test_config_default_values(config_data):

    assert config_data["urlsfile"] == "/home/coskun/video_urls.txt"
    assert config_data["channels"] == [
        "https://www.youtube.com/c/ArjanCodes/",
        "https://www.youtube.com/user/coskundenize",
    ]
    assert config_data["output_type"] == "excel"
    assert config_data["output_file"] == "results.xlsx"
    assert config_data["url_column"] == 0
    assert config_data["share_mail"] == "coskun.denize@gmail.com"
