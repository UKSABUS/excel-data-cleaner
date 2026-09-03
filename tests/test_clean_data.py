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

    cleaned, report = clean_dataframe(dataframe)

    assert len(cleaned) == 1
    assert cleaned["name"].tolist() == ["Ali"]
    assert report["empty_rows_removed"] == 1


def test_missing_values_are_reported():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", "Sara", "Reza"],
            "Age": [22, None, 27],
            "City": ["Tehran", "Shiraz", None],
        }
    )

    _, report = clean_dataframe(dataframe)

    assert report["missing_cells"] == 2
    assert report["missing_by_column"]["age"] == 1
    assert report["missing_by_column"]["city"] == 1


def test_data_types_are_reported():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", "Sara"],
            "Age": [22, 24],
        }
    )

    _, report = clean_dataframe(dataframe)

    assert report["data_types"]["name"] == "str"
    assert report["data_types"]["age"] == "int64"
def test_median_strategy_fills_numeric_missing_values():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", "Sara", "Reza"],
            "Age": [20, None, 30],
        }
    )

    cleaned, report = clean_dataframe(
        dataframe,
        missing_strategy="median",
    )

    assert cleaned["age"].isna().sum() == 0
    assert cleaned["age"].iloc[1] == 25
    assert report["missing_cells"] == 0


def test_drop_strategy_removes_rows_with_missing_values():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", "Sara", "Reza"],
            "Age": [20, None, 30],
        }
    )

    cleaned, report = clean_dataframe(
        dataframe,
        missing_strategy="drop",
    )

    assert len(cleaned) == 2
    assert cleaned["name"].tolist() == ["Ali", "Reza"]
    assert report["missing_cells"] == 0


def test_fill_strategy_handles_text_and_numeric_columns():
    dataframe = pd.DataFrame(
        {
            "Name": ["Ali", None, "Reza"],
            "Age": [20, None, 30],
        }
    )

    cleaned, report = clean_dataframe(
        dataframe,
        missing_strategy="fill",
        fill_value="Unknown",
    )

    assert cleaned["name"].tolist() == ["Ali", "Unknown", "Reza"]
    assert cleaned["age"].isna().sum() == 0
    assert cleaned["age"].iloc[1] == 25
    assert pd.api.types.is_numeric_dtype(cleaned["age"])
    assert report["missing_cells"] == 0