import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPEDS_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPEDS_CREDS)
SHEET = GSPREAD_CLIENT.open('PP3')

page1 = SHEET.worksheet('page1') #worksheet is a method of the sheet and calls the page1 spreadsheet data

data = page1.get_all_values() #get_all_values is a gspread method that pulls all values from the page 1 sheet

print(data)
