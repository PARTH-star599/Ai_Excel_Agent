import pandas as pd

FILE_NAME = "students.xlsx"


def load_excel():
    """Load the Excel file."""

    try:
        df = pd.read_excel(FILE_NAME)
        return df

    except Exception as e:
        print("Error loading Excel file:", e)
        return None


def get_excel_data():
    """Return Excel data as text."""

    df = load_excel()

    if df is None:
        return None

    return df.to_string(index=False)


def get_columns():
    """Return column names."""

    df = load_excel()

    if df is None:
        return []

    return list(df.columns)