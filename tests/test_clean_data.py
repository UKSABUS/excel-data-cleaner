import pandas as pd

from clean_data import clean_dataframe


def test_duplicate_rows_are_removed():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", "Ali", "Sara"],
            "Age": [22, 22, 24],
        }
    )

    cleaned, report = clean_dataframe(dataframe)

    assert len(cleaned) == 2
    assert report["duplicates_removed"] == 1


def test_column_names_are_standardized():
    dataframe = pd.DataFrame(
        {
            " First Name ": ["Ali"],
            "Age Value": [22],
        }
    )

    cleaned, _ = clean_dataframe(dataframe)

    assert list(cleaned.columns) == ["first_name", "age_value"]


def test_whitespace_is_removed():
    dataframe = pd.DataFrame(
        {
            "Name": ["  Ali  ", " Sara"],
        }
    )

    cleaned, _ = clean_dataframe(dataframe)

    assert cleaned["name"].tolist() == ["Ali", "Sara"]


def test_empty_rows_are_removed():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", None],
            "Age": [22, None],
        }
    )

    cleaned, _ = clean_dataframe(dataframe)

    assert len(cleaned) == 1
    assert cleaned["name"].tolist() == ["Ali"]

