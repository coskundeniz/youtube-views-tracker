YouTube Views Tracker
=====================

YouTube Views Tracker with Excel and Google Sheets Integration


https://stackoverflow.com/questions/261638/how-do-i-protect-python-code-from-being-read-by-users

https://wiki.python.org/moin/Asking%20for%20Help/How%20do%20you%20protect%20Python%20source%20code%3F

## How to setup




## How to use

```sh
usage: python yt_views_tracker.py [-h] [-c] [-cf CONFIGFILE] [-f URLSFILE] [-ch CHANNELS] [-ot OUTPUT_TYPE] [-of OUTPUT_FILE] [-uc URL_COLUMN] [-sm SHARE_MAIL] [-s SCHEDULE]

optional arguments:
  -h, --help            show this help message and exit
  -c, --useconfig       Read configuration from config.json file
  -cf CONFIGFILE, --configfile CONFIGFILE
                        Read configuration from given file
  -f URLSFILE, --urlsfile URLSFILE
                        File to read video urls
  -ch CHANNELS, --channels CHANNELS
                        Channel urls separated by comma
  -ot OUTPUT_TYPE, --output_type OUTPUT_TYPE
                        Output file type (one of excel, gsheets)
  -of OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name
  -uc URL_COLUMN, --url_column URL_COLUMN
                        Url column index for csv, xlsx, or Google Sheets input
  -sm SHARE_MAIL, --share_mail SHARE_MAIL
                        Mail address to share Google Sheets document
  -s SCHEDULE, --schedule SCHEDULE
                        Interval to run as scheduled task
```

* If you will use Google Sheets for getting video url inputs, add "gsheets-" prefix to the urlsfile(f) parameter.

    * python yt_views_tracker.py -f gsheets-video_urls
    * python yt_views_tracker.py -f gsheets-video_urls -uc 2
    * python yt_views_tracker.py -f gsheets-https://docs.google.com/spreadsheets/d/1dtFZbg4Gm8mCopO9fpZ-DwJ37uLMopgLePgFdigutuI

* yt_views_tracker.py -f ~/video_urls.txt -ot gsheets -of view_results

* config.json example for channels

    ```json
    {
        "urlsfile": "",
        "channels": [
            "https://www.youtube.com/c/ArjanCodes/",
            "https://www.youtube.com/user/coskundenize"
        ],
        "output_type": "excel",
        "output_file": "results.xlsx",
        "url_column": 0,
        "share_mail": "codenineeight@gmail.com",
        "schedule": "NONE"
    }
    ```

    * urlsfile field must be empty.

### Scheduling Options

* Scheduling interval options

    - NONE (default)
    - 10 minutes
    - 15 minutes
    - 30 minutes
    - 1 hour
    - 3 hours
    - 6 hours
    - 8 hours
    - 12 hours
    - Once a day at "HH:MM"


### Creating project on Google Cloud Console

* https://docs.gspread.org/en/latest/oauth2.html

1. Create a new project

2. Enable "Google Drive API"

    https://console.cloud.google.com/apis/library/drive.googleapis.com

3. Enable "Google Sheets API"

    https://console.cloud.google.com/apis/library/sheets.googleapis.com

4. Create credentials -> Service Account from "APIs & Services"

5. After creating credentials, add key -> JSON

    * Save download file as "credentials.json" and copy to project directory.

6. Share your document with the value of "client_email" field if you will read urls from Google Sheets.


## How to run tests

* `pytest -vs`

* `coverage run --omit *dist-packages* -m pytest -vs`


### How to check coverage

* `coverage report --omit *dist-packages,yt_views_tracker.py*`
* `coverage html --omit *dist-packages,yt_views_tracker.py*`