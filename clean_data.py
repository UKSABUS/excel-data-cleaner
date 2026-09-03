import argparse
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


def handle_missing_values(
    df: pd.DataFrame,
    strategy: str = "keep",
    fill_value: str = "Unknown",
) -> tuple[pd.DataFrame, int]:
    """Handle missing values using the selected strategy."""

    missing_before = int(df.isna().sum().sum())

    if strategy == "keep":
        return df, 0

    if strategy == "drop":
        cleaned = df.dropna()
        return cleaned, missing_before

    if strategy == "median":
        cleaned = df.copy()

        numeric_columns = cleaned.select_dtypes(include="number").columns

        for column in numeric_columns:
            if cleaned[column].isna().any():
                median_value = cleaned[column].median()

                if pd.notna(median_value):
                    cleaned[column] = cleaned[column].fillna(
                        median_value
                    )

        return cleaned, int(cleaned.isna().sum().sum())

    if strategy == "fill":
        cleaned = df.copy()

        numeric_columns = cleaned.select_dtypes(include="number").columns
        text_columns = cleaned.select_dtypes(
            include=["object", "string"]
        ).columns

        # Fill numeric columns with their median
        for column in numeric_columns:
            if cleaned[column].isna().any():
                median_value = cleaned[column].median()

                if pd.notna(median_value):
                    cleaned[column] = cleaned[column].fillna(
                        median_value
                    )

        # Fill text columns with the selected value
        for column in text_columns:
            cleaned[column] = cleaned[column].fillna(fill_value)

        return cleaned, int(cleaned.isna().sum().sum())

    raise ValueError(
        f"Unknown missing-value strategy: {strategy}"
    )


def clean_dataframe(
    df: pd.DataFrame,
    missing_strategy: str = "keep",
    fill_value: str = "Unknown",
) -> tuple[pd.DataFrame, dict]:
    """Clean and analyze a Pandas DataFrame."""

    original_rows = len(df)
    original_columns = len(df.columns)

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

    # Remove duplicate rows
    duplicates_removed = int(df.duplicated().sum())
    df = df.drop_duplicates()

    # Handle missing values
    df, remaining_missing = handle_missing_values(
        df,
        strategy=missing_strategy,
        fill_value=fill_value,
    )

    # Remove completely empty rows after missing-value handling
    empty_rows_removed = int(df.isna().all(axis=1).sum())
    df = df.dropna(how="all")

    # Analyze missing values after cleaning
    missing_by_column = df.isna().sum()
    missing_cells = int(missing_by_column.sum())

    # Analyze data types
    data_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

    report = {
        "original_rows": original_rows,
        "final_rows": len(df),
        "duplicates_removed": duplicates_removed,
        "empty_rows_removed": empty_rows_removed,
        "columns": original_columns,
        "missing_cells": missing_cells,
        "remaining_missing": remaining_missing,
        "missing_strategy": missing_strategy,
        "missing_by_column": missing_by_column.to_dict(),
        "data_types": data_types,
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
    """Print a detailed cleaning report."""

    print("\nDATA CLEANING REPORT")
    print("=" * 45)
    print(f"Rows before:        {report['original_rows']}")
    print(f"Rows after:         {report['final_rows']}")
    print(f"Duplicates removed: {report['duplicates_removed']}")
    print(f"Empty rows removed: {report['empty_rows_removed']}")
    print(f"Columns:            {report['columns']}")
    print(f"Missing strategy:   {report['missing_strategy']}")
    print(f"Missing cells:      {report['missing_cells']}")

    print("\nCOLUMN INFORMATION")
    print("-" * 45)

    for column, dtype in report["data_types"].items():
        missing = report["missing_by_column"].get(column, 0)

        print(
            f"{column:<20} | "
            f"{dtype:<10} | "
            f"missing: {missing}"
        )

    print("-" * 45)
    print(f"Saved to: {output_path}")


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Clean and standardize CSV or Excel datasets."
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input CSV or Excel file.",
    )

    parser.add_argument(
        "output_file",
        type=Path,
        help="Path for the cleaned output file.",
    )

    parser.add_argument(
        "--missing",
        choices=["keep", "drop", "median", "fill"],
        default="keep",
        help="Strategy for handling missing values.",
    )

    parser.add_argument(
        "--fill-value",
        default="Unknown",
        help="Value used when --missing fill is selected.",
    )

    return parser.parse_args()


def main() -> None:
    """Run the command-line data cleaning workflow."""

    args = parse_arguments()

    if not args.input_file.exists():
        print(f"Error: Input file not found: {args.input_file}")
        raise SystemExit(1)

    try:
        print("Loading dataset...")
        dataframe = load_file(args.input_file)

        print("Cleaning dataset...")
        cleaned_dataframe, report = clean_dataframe(
            dataframe,
            missing_strategy=args.missing,
            fill_value=args.fill_value,
        )

        save_file(cleaned_dataframe, args.output_file)
        print_report(report, args.output_file)

    except (ValueError, OSError, pd.errors.ParserError) as error:
        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()