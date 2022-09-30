import pandas as pd

def clean_dataset(frame):
    """
    Clean birthdays dataset.

    Args:
        frame (pd.DataFrame): The data frame to be cleaned

    Returns:
        pd.DataFrame: The cleaned data frame
    """
    frame["day_of_year"] = frame["date"].dt.dayofyear
    frame = frame.groupby(["date", "wday", "day_of_year"]).agg(
        births=("births", "sum"), month=("month", "first")
    ).reset_index()
    return frame