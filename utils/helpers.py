from datetime import datetime
import pandas as pd
import pytz


def get_current_timestamp():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime("%Y%m%d%H%M")

def save_to_excel(df, prefix="tweets"):
    filename = f"{prefix}_{get_current_timestamp()}.xlsx"
    df.to_excel(filename, index=False)
    return filename