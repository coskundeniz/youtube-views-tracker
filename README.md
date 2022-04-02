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

---

## How to setup

* Run the following commands to install required packages

    * `cd <project directory>`
    * `python -m venv env`
    * `source env/bin/activate`
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
### Basic Usage

* For the most basic usage, the script requires at least one of “-c”, “-f”, or “-ch” options for config file, urls file and channel links respectively.
    * `python yt_views_tracker.py -c`
    * `python yt_views_tracker.py -f ~/video_urls.txt`
    * `python yt_views_tracker.py -ch “https://www.youtube.com/c/ArjanCodes/”`

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
