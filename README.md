YouTube Views Tracker
=====================

YouTube Views Tracker with Excel and Google Sheets Integration


https://stackoverflow.com/questions/261638/how-do-i-protect-python-code-from-being-read-by-users

https://wiki.python.org/moin/Asking%20for%20Help/How%20do%20you%20protect%20Python%20source%20code%3F

## How to setup




## How to use

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
        "share_mail": "codenineeight@gmail.com"
    }
    ```

    * urlsfile field must be empty.


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

* `coverage report --omit *dist-packages*`
* `coverage html --omit *dist-packages*`