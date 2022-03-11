YouTube Views Tracker
=====================

YouTube Views Tracker with Excel and Google Sheets Integration


https://stackoverflow.com/questions/261638/how-do-i-protect-python-code-from-being-read-by-users

https://wiki.python.org/moin/Asking%20for%20Help/How%20do%20you%20protect%20Python%20source%20code%3F

## How to setup




## How to use


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

6. Share your document with the value of "client_email" field.


## How to run tests

`pytest -vs`

`coverage run --omit *dist-packages* -m pytest -vs`


### How to check coverage

`coverage report --omit *dist-packages*`
`coverage html --omit *dist-packages*`