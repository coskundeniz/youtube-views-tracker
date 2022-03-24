YouTube Views Tracker
=====================

YouTube Views Tracker with Excel and Google Sheets Integration

### Supported Functionalities

* Read urls from txt, csv, xlsx, or Google Sheets file.
* Read video urls from channel link
* Output results to Excel
* Chart for the most watched 10 videos for Excel output
* Output results to Google Sheets

---

## How to setup

* Run the following command to install required packages

    * `python -m pip install -r requirements.txt`

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

---

## How to use

```sh
usage: python yt_views_tracker.py [-h] [-c] [-cf CONFIGFILE] [-f URLSFILE] [-ch CHANNELS] [-ot OUTPUT_TYPE] [-of OUTPUT_FILE] [-uc URL_COLUMN] [-sm SHARE_MAIL]

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
```

* If you will use Google Sheets for getting video url inputs, add "gsheets-" prefix to the urlsfile(f) parameter.

    * `python yt_views_tracker.py -f gsheets-video_urls`
    * `python yt_views_tracker.py -f gsheets-video_urls -uc 2`
    * `python yt_views_tracker.py -f gsheets-https://docs.google.com/spreadsheets/d/1dtFZbg4Gm8mCopO9fpZ-DwJ37uLMopgLePgFdigutuI`

    * `python yt_views_tracker.py -f ~/video_urls.txt -ot gsheets -of view_results -sm codenineeight@gmail.com`

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
    }
    ```

    * *urlsfile* field must be empty.

---

## How to run tests

* `pytest -vs`

### How to check coverage

* `coverage run --omit *dist-packages* -m pytest -vs`
* `coverage report --omit *dist-packages,yt_views_tracker.py*`
* `coverage html --omit *dist-packages,yt_views_tracker.py*`
