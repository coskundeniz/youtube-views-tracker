import pytest
from datetime import datetime

from yt_views import YoutubeViews


@pytest.fixture
def video_urls():

    return [
        "https://www.youtube.com/watch?v=gxUq5Kt83V4",  # solo, 180+
        "https://www.youtube.com/watch?v=3T4uDDfR43Y",  # memories, 200+
    ]


def test_create_with_video_urls(video_urls):

    yt_views = YoutubeViews(video_urls=video_urls)

    assert isinstance(yt_views, YoutubeViews)
    assert len(yt_views.videos) == 0


def test_create_with_video_urls_more_than_hundred():

    video_urls = open("tests/urlreader/urls_more_than_hundred.txt").read().splitlines()
    yt_views = YoutubeViews(video_urls=video_urls)
    yt_views.update()

    assert isinstance(yt_views, YoutubeViews)
    assert len(yt_views.videos) == len(video_urls)


@pytest.mark.skipif(datetime.now().strftime("%A") != "Monday", reason="Test once a week on Monday")
def test_create_with_video_urls_more_than_thousand():

    video_urls = open("tests/urlreader/video_urls_more_than_1000.txt").read().splitlines()
    yt_views = YoutubeViews(video_urls=video_urls[:1000])
    yt_views.update()

    assert isinstance(yt_views, YoutubeViews)
    assert len(yt_views.videos) == 1000


def test_create_without_keyword_argument(video_urls):

    with pytest.raises(TypeError):
        YoutubeViews(video_urls)


def test_update_views(video_urls):

    yt_views = YoutubeViews(video_urls=video_urls)
    yt_views.update()

    assert len(yt_views.videos) == len(video_urls)
    assert yt_views.videos[0].views > 180
    assert yt_views.videos[1].views > 200


def test_members_only_video():

    members_only_video_url = ["https://www.youtube.com/watch?v=jHZJGAEX-9E"]

    yt_views = YoutubeViews(video_urls=members_only_video_url)
    yt_views.update()

    assert len(yt_views.videos) == 1


def test_private_video_url(capfd):

    private_video_url = ["https://youtu.be/87rW_ZeLt3g"]

    yt_views = YoutubeViews(video_urls=private_video_url)
    yt_views.update()

    _, err = capfd.readouterr()

    assert len(yt_views.videos) == 0
    assert "Video https://youtu.be/87rW_ZeLt3g is unavailable, skipping..." in err
