YouTube Views Tracker
=====================

This tool monitors view counts for YouTube videos and reports the results on Excel or Google Sheets documents.
The user can use either video URLs or channel links to track video counts.


### Supported Functionalities

* Read urls from txt, csv, xlsx, or Google Sheets file.
* Read video urls from channel link
* Output results to Excel
* Chart for the most watched 10 videos for Excel output
* Output results to Google Sheets
* Schedule for repeated runs
* Run as Docker container

See the user manual [here](https://github.com/coskundeniz/youtube-views-tracker/blob/main/docs/user_manual.pdf)

---

## How to setup

* Run the following commands to install required packages

    * `cd <project directory>`
    * `python -m venv env`
    * `source env/bin/activate`
    * `python -m pip install -r requirements.txt`

### How to create Docker image manually

* Install docker from [here](https://docs.docker.com/get-docker/) and run the following command in the project directory.

    * `docker build -t yt_views_tracker .`

* Creating a tar file from Docker image

    * `docker save yt_views_tracker:latest | gzip > yt_views_tracker.tar.gz`

* Loading the tar image

    * `docker load -i yt_views_tracker.tar.gz`

### Creating project on Google Cloud Console

1. Go to Google Developers Console and create a new project.

    https://console.cloud.google.com

2. Enable "Google Drive API"

    https://console.cloud.google.com/apis/library/drive.googleapis.com

3. Enable "Google Sheets API"

    https://console.cloud.google.com/apis/library/sheets.googleapis.com

4. Create credentials -> Service Account from "APIs & Services"

5. After creating credentials, add key -> JSON

    * Save download file as "credentials.json" and copy to project directory.

6. Share your document with the value of "client_email" field if you will read urls from Google Sheets.

---

## How to use

```sh
usage: python yt_views_tracker.py [-h] [-c] [-cf CONFIGFILE] [-f URLSFILE] [-ch CHANNELS] [-ot OUTPUT_TYPE] [-of OUTPUT_FILE] [-uc URL_COLUMN] [-sm SHARE_MAIL] [-s SCHEDULE]

optional arguments:
  -h, --help                                    show this help message and exit
  -c, --useconfig                               Read configuration from config.json file
  -cf CONFIGFILE, --configfile CONFIGFILE       Read configuration from given file
  -f URLSFILE, --urlsfile URLSFILE              File to read video urls
  -ch CHANNELS, --channels CHANNELS             Channel urls separated by comma
  -ot OUTPUT_TYPE, --output_type OUTPUT_TYPE    Output file type (one of excel, gsheets)
  -of OUTPUT_FILE, --output_file OUTPUT_FILE    Output file name
  -uc URL_COLUMN, --url_column URL_COLUMN       Url column index for csv, xlsx, or Google Sheets input
  -sm SHARE_MAIL, --share_mail SHARE_MAIL       Mail address to share Google Sheets document
  -s SCHEDULE, --schedule SCHEDULE              Interval to run as scheduled task
```

### Basic Usage

* For the most basic usage, the script requires at least one of “-c”, “-f”, or “-ch” options for config file, urls file and channel links respectively.
    * `python yt_views_tracker.py -c`
    * `python yt_views_tracker.py -f ~/video_urls.txt`
    * `python yt_views_tracker.py -ch "https://www.youtube.com/c/ArjanCodes/"`

Results are written to results.xlsx file by default in views, title, url order.
Logs can be seen in the yt_views.log file in the project directory.

### Example Commands

* Read video URLs from video_urls.csv and output results to video_view_counts.xlsx file.
    * `python yt_views_tracker.py -f ~/video_urls.csv -of video_view_counts.xlsx`

* Use options from custom_config.json file.
    * `python yt_views_tracker.py -c -cf custom_config.json`

* Read video URLs from the third column of video_urls.csv file.
    * `python yt_views_tracker.py -f ~/video_urls.csv -uc 2`

* If you will use Google Sheets for getting video URL inputs, add “gsheets-” prefix to the urlsfile(f) parameter.
    * `python yt_views_tracker.py -f gsheets-video_urls`

	This command will read URLs from Google Sheets document named “video_urls”.

* Read video URLs from Google Sheets document using file link.
    * `python yt_views_tracker.py -f gsheets-https://docs.google.com/spreadsheets/d/1dtFZbg4Gm8mCopO9fpZ-DwJ37uLMopgLePgFdigutuI`

* Read video URLs from txt file and output results to Google Sheets document named “view_results”.
    * `python yt_views_tracker.py -f ~/video_urls.txt -ot gsheets -of view_results -sm codenineeight@gmail.com`

	Share mail parameter is needed, so that you can see the document on your account.

* If you will use config file and read URLs from channel links, you should keep the urlsfile field empty in the json file.
    ```json
    {
        "urlsfile": "",
        "channels": [
            "https://www.youtube.com/c/ArjanCodes/",
            "https://www.youtube.com/c/Coreyms"
        ],
        "output_type": "excel",
        "output_file": "results.xlsx",
        "url_column": 0,
        "share_mail": "codenineeight@gmail.com",
        "schedule": "NONE"
    }
    ```

    * `python yt_views_tracker.py -c`


### How to run Docker image

* Run the following command first for once.

    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker`

* If you will use with Google Sheets, copy your credentials file to the shared directory.
    * `sudo cp /path/to/credentials.json /var/lib/docker/volumes/view_results_volume/_data`

* If you will use the urls file, copy urls file to the shared directory.
    * `sudo cp ~/video_urls.txt /var/lib/docker/volumes/view_results_volume/_data`

* Run the container by passing arguments as usual.
    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker -f video_urls.txt`
    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker -ch "https://www.youtube.com/c/ArjanCodes/"`
    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker -f gsheets-video_urls`
    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker -f video_urls.txt -ot gsheets -of view_results -sm codenineeight@gmail.com`

* Copy the results to a different directory on the host device.
    * `sudo cp /var/lib/docker/volumes/view_results_volume/_data/results.xlsx ~/views_output`

or

* Copy your config file to the shared directory.
    * `sudo cp ~/views_output/config_for_docker.json /var/lib/docker/volumes/view_results_volume/_data/`

* Run the container with "-c" and "-cf" options.
    * `docker run --rm -it -v view_results_volume:/src yt_views_tracker -c -cf config_for_docker.json`


* See [here](https://docs.docker.com/desktop/windows/#file-sharing) for sharing on Windows.


### Scheduling

* You can run the script in scheduled intervals. Scheduling is not active by default so the script will run only once and exit after completion. You have 9 scheduling options as shown below.
    1. 10 minutes (MIN10)
    2. 15 minutes (MIN15)
    3. 30 minutes (MIN30)
    4. 1 hour (HOUR1)
    5. 3 hours (HOUR3)
    6. 6 hours (HOUR6)
    7. 8 hours (HOUR8)
    8. 12 hours (HOUR12)
    9. Once a day at “HH:MM”

* Run every 30 minutes
    * `python yt_views_tracker.py -f video_urls.csv -s MIN30`

* Run once a day at 15:30
    * `python yt_views_tracker.py -f video_urls.csv -s 15:30`

---

## How to run tests

* `python -m pip install pytest`
* `pytest -vs`

### How to check coverage

* `python -m pip install coverage`

* `coverage run --omit *dist-packages* -m pytest -vs`
* `coverage report --omit *dist-packages,yt_views_tracker.py*`
* `coverage html --omit *dist-packages,yt_views_tracker.py*`

You can see the report by opening index.html file located under htmlcov folder in the project directory.

---

## Support

If you need support, you can contact me by emailing to codenineeight@gmail.com with the “yt_views_tracker” prefix in the subject. You can also see my Upwork profile [here](https://www.upwork.com/freelancers/~011e3fe44e575092f0).

If you benefit from this tool, please consider donating using the sponsor links.