YouTube Views Tracker
=====================

YouTube Views Tracker with Excel Integration

### Supported Functionalities

* Read urls from txt, csv, or xlsx file.
* Read video urls from channel link
* Output results to Excel
* Chart for the most watched 10 videos for Excel output

---

## How to setup

* Run the following command to install required packages

    * `python -m pip install -r requirements.txt`

---

## How to use

```sh
usage: python yt_views_tracker.py [-h] [-c] [-cf CONFIGFILE] [-f URLSFILE] [-ot OUTPUT_TYPE] [-of OUTPUT_FILE] [-uc URL_COLUMN]

optional arguments:
  -h, --help                                    show this help message and exit
  -c, --useconfig                               Read configuration from config.json file
  -cf CONFIGFILE, --configfile CONFIGFILE       Read configuration from given file
  -f URLSFILE, --urlsfile URLSFILE              File to read video urls
  -ot OUTPUT_TYPE, --output_type OUTPUT_TYPE    Output file type (excel)
  -of OUTPUT_FILE, --output_file OUTPUT_FILE    Output file name
  -uc URL_COLUMN, --url_column URL_COLUMN       Url column index for csv, or xlsx input
```

* Example commands

    * `python yt_views_tracker.py -f video_urls.txt`
    * `python yt_views_tracker.py -f video_urls.csv -uc 2`
    * `python yt_views_tracker.py -c`
    * `python yt_views_tracker.py -c -cf my_custom_config.json`

---

## How to run tests

* `pytest -vs`

### How to check coverage

* `coverage run --omit *dist-packages* -m pytest -vs`
* `coverage report --omit *dist-packages,yt_views_tracker.py*`
* `coverage html --omit *dist-packages,yt_views_tracker.py*`
