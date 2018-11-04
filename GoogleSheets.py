"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
credentials = 1541288920087

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1047250279265-8jkm65nteb2h13vn7gh9rmhprrrcrn4e.apps.googleusercontent.com'  # TODO: Update placeholder value.

# The A1 notation of the values to update.
range_ = 'Class Data!A30'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'RAW'  # TODO: Update placeholder value.

value_range_body = {"anjsdfjsdfjnsd"}
    # will be replaced.


request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
