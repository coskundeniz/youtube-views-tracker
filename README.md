YouTube Views Tracker
=====================

This tool monitors view counts for YouTube videos and reports the results on Excel.
The user can use either video URLs to track video counts.

### Supported Functionalities

* Read urls from txt, csv, or xlsx file.
* Output results to Excel
* Chart for the most watched 10 videos for Excel output

---

## How to setup

* Run the following commands to install required packages

    * `cd <project directory>`
    * `python -m venv env`
    * `source env/bin/activate`
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
### Basic Usage

* For the most basic usage, the script requires at least one of “-c”, or “-f” options for config file, urls file and channel links respectively.
    * `python yt_views_tracker.py -c`
    * `python yt_views_tracker.py -f ~/video_urls.txt`

Results are written to results.xlsx file by default in views, title, url order.
Logs can be seen in the yt_views.log file in the project directory.

### Example Commands

* Read video URLs from video_urls.csv and output results to video_view_counts.xlsx file.
    * `python yt_views_tracker.py -f ~/video_urls.csv -of video_view_counts.xlsx`

* Use options from custom_config.json file.
    * `python yt_views_tracker.py -c -cf custom_config.json`

* Read video URLs from the third column of video_urls.csv file.
    * `python yt_views_tracker.py -f ~/video_urls.csv -uc 2`

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

## Support

If you need support, you can contact me by emailing to codenineeight@gmail.com with the “yt_views_tracker” prefix in the subject. You can also see my Upwork profile [here](https://www.upwork.com/freelancers/~011e3fe44e575092f0).
