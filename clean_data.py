```python
import sys
from pathlib import Path

import pandas as pd


SUPPORTED_INPUT_FORMATS = {".csv", ".xlsx", ".xls"}
SUPPORTED_OUTPUT_FORMATS = {".csv", ".xlsx", ".xls"}


def load_file(file_path: Path) -> pd.DataFrame:
    """Load a CSV or Excel file into a Pandas DataFrame."""
    extension = file_path.suffix.lower()

    if extension == ".csv":
        return pd.read_csv(file_path)

    if extension in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)

    raise ValueError(
        f"Unsupported input format: {extension}. "
        f"Supported formats: {', '.join(sorted(SUPPORTED_INPUT_FORMATS))}"
    )


def clean_dataframe(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Clean and standardize a Pandas DataFrame."""

    original_rows = len(df)

    # Standardize column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    # Remove unnecessary whitespace from text cells
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for column in text_columns:
        df[column] = df[column].apply(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    duplicates_removed = int(df.duplicated().sum())
    df = df.drop_duplicates()

    # Generate cleaning report
    report = {
        "original_rows": original_rows,
        "final_rows": len(df),
        "duplicates_removed": duplicates_removed,
        "columns": len(df.columns),
        "missing_cells": int(df.isna().sum().sum()),
    }

    return df, report


def save_file(df: pd.DataFrame, file_path: Path) -> None:
    """Save a DataFrame as CSV or Excel."""

    extension = file_path.suffix.lower()

    if extension == ".csv":
        df.to_csv(file_path, index=False)
        return

    if extension in {".xlsx", ".xls"}:
        df.to_excel(file_path, index=False)
        return

    raise ValueError(
        f"Unsupported output format: {extension}. "
        f"Supported formats: {', '.join(sorted(SUPPORTED_OUTPUT_FORMATS))}"
    )


def print_report(report: dict, output_path: Path) -> None:
    """Print a formatted summary of the cleaning process."""

    print("\nCleaning completed successfully!")
    print("-" * 40)
    print(f"Original rows:      {report['original_rows']}")
    print(f"Final rows:         {report['final_rows']}")
    print(f"Duplicates removed: {report['duplicates_removed']}")
    print(f"Columns:            {report['columns']}")
    print(f"Missing cells:      {report['missing_cells']}")
    print("-" * 40)
    print(f"Saved to: {output_path}")


def main() -> None:
    """Run the command-line data cleaning workflow."""

    if len(sys.argv) != 3:
        print("Usage:")
        print("python clean_data.py input.csv cleaned_output.csv")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    try:
        print("Loading dataset...")
        dataframe = load_file(input_path)

        print("Cleaning dataset...")
        cleaned_dataframe, report = clean_dataframe(dataframe)

        save_file(cleaned_dataframe, output_path)
        print_report(report, output_path)

    except (ValueError, OSError, pd.errors.ParserError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
