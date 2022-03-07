import pytest

from video import YoutubeVideo


def test_video_creation():

    video = YoutubeVideo(
        url="https://www.youtube.com/watch?v=gxUq5Kt83V4",
        title="Darbuka solo before class",
        views=185,
    )

    assert isinstance(video, YoutubeVideo)
    assert video.title == "Darbuka solo before class"
    assert video.views == 185


def test_video_creation_missing_parameter():

    with pytest.raises(TypeError):
        YoutubeVideo(
            url="https://www.youtube.com/watch?v=gxUq5Kt83V4", title="Darbuka solo before class"
        )
