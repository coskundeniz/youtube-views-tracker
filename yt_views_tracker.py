from pytube import YouTube, Channel


# https://pytube.io/en/latest/api.html#module-pytube.exceptions

# TODO: use logging

# TODO: use class

# TODO: use ???


def get_views_from_urls(urls):

    for url in urls:
        video = YouTube(url)
        print(
            f"Title: {video.title} - Views Count: {video.views}, Length: {video.length}"
        )


def get_views_from_channel(channel_url):

    mychannel = Channel(channel_url)

    print(f"Channel name: {mychannel.channel_name}")

    for video in mychannel.videos:
        print(f"Title: {video.title} - Views Count: {video.views}")


def main():

    pass


if __name__ == "__main__":

    main()
