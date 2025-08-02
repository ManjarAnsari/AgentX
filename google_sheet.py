
import pandas as pd

def get_sheet_data():
    url = "https://docs.google.com/spreadsheets/d/1w6uiuYFjXlVfNRTlNxmcAp03YJkbLjaZQwg6OhZt0rk/export?format=csv"
    try:
        df = pd.read_csv(url)
        return df.to_string(index=False)
    except:
        return "Google Sheet data not available."
