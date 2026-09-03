import sys
from pathlib import Path

import pandas as pd


def load_file(file_path):
    """Load a CSV or Excel file into a Pandas DataFrame."""
    extension = file_path.suffix.lower()

    if extension == ".csv":
        return pd.read_csv(file_path)

    if extension in [".xlsx", ".xls"]:
        return pd.read_excel(file_path)

    raise ValueError("Supported formats: CSV, XLSX, XLS")


def clean_dataframe(df):
    """Clean and standardize a dataset."""

    original_rows = len(df)

    # Standardize column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    # Remove unnecessary spaces from text cells
    for column in df.select_dtypes(include=["object", "string"]).columns:
        df[column] = df[column].apply(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    report = {
        "original_rows": original_rows,
        "final_rows": len(df),
        "duplicates_removed": int(duplicates_removed),
        "columns": len(df.columns),
        "missing_cells": int(df.isna().sum().sum()),
    }

    return df, report


def save_file(df, file_path):
    """Save the cleaned DataFrame as CSV or Excel."""

    extension = file_path.suffix.lower()

    if extension == ".csv":
        df.to_csv(file_path, index=False)

    elif extension in [".xlsx", ".xls"]:
        df.to_excel(file_path, index=False)

    else:
        raise ValueError("Output must be CSV or Excel")


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("python clean_data.py input.csv cleaned_output.csv")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    try:
        print("Loading dataset...")

        dataframe = load_file(input_path)

        print("Cleaning dataset...")

        cleaned_dataframe, report = clean_dataframe(dataframe)

        save_file(cleaned_dataframe, output_path)

        print("\nCleaning completed successfully!")
        print("-" * 35)
        print(f"Original rows:      {report['original_rows']}")
        print(f"Final rows:         {report['final_rows']}")
        print(f"Duplicates removed: {report['duplicates_removed']}")
        print(f"Columns:            {report['columns']}")
        print(f"Missing cells:      {report['missing_cells']}")
        print("-" * 35)
        print(f"Saved to: {output_path}")

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
