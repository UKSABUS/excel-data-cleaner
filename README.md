# Excel Data Cleaner 🧹📊

A lightweight Python tool for cleaning and standardizing CSV and Excel datasets.

This project automates common data-cleaning tasks such as removing duplicate records, standardizing column names, trimming unnecessary whitespace, handling missing values, removing completely empty rows, and generating a simple cleaning report.

## Features

* Remove duplicate rows

* Standardize column names

* Trim unnecessary whitespace from text fields

* Remove completely empty rows

* Detect missing values

* Handle missing values using multiple strategies

* Fill missing numeric values using the column median

* Fill missing text values with a custom value

* Generate a cleaning summary

* Export cleaned datasets to CSV or Excel

* Supports reusable cleaning functions

* Includes automated tests with `pytest`

## Technologies

* Python

* Pandas

* OpenPyXL

* Pytest

## Project Structure

```text
excel-data-cleaner/

│

├── clean_data.py

├── sample.csv

├── cleaned_output.csv

├── requirements.txt

├── README.md

├── .gitignore

│

└── tests/

    └── test_clean_data.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/UKSABUS/excel-data-cleaner.git

cd excel-data-cleaner
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The tool works from the command line.

### Clean a CSV file

```bash
python clean_data.py sample.csv cleaned_output.csv
```

### Clean an Excel file

```bash
python clean_data.py input.xlsx cleaned_output.xlsx
```

The program loads the dataset, applies the selected cleaning operations, generates a summary report, and saves the cleaned dataset.

## Missing-Value Handling

The tool supports four strategies for handling missing values.

### Keep

Keep missing values unchanged:

```bash
python clean_data.py input.csv output.csv --missing keep
```

This is the default behavior.

### Drop

Remove rows containing missing values:

```bash
python clean_data.py input.csv output.csv --missing drop
```

### Median

Fill missing numeric values using the median of their column:

```bash
python clean_data.py input.csv output.csv --missing median
```

### Fill

Fill missing numeric values with the column median and missing text values with `Unknown`:

```bash
python clean_data.py input.csv output.csv --missing fill
```

A custom value can be used for missing text fields:

```bash
python clean_data.py input.csv output.csv --missing fill --fill-value "Not Available"
```

## Example

### Input

```text
Name,Email,Age,City
 Ali ,ALI@example.com,22, Tehran
Sara,sara@example.com,24,Shiraz
Ali,ALI@example.com,22, Tehran
 Reza ,reza@example.com,27,Tabriz
Maryam,maryam@example.com,,Isfahan
Sara,sara@example.com,24,Shiraz
```

### Command

```bash
python clean_data.py sample.csv cleaned_output.csv --missing fill
```

### Output

```text
DATA CLEANING REPORT
---------------------------------------------

Rows before:        6
Rows after:         4
Duplicates removed: 2
Empty rows removed: 0
Columns:            4
Missing strategy:   fill
Missing cells:      0

Saved to: cleaned_output.csv
```

## Cleaning Report

| Metric             | Result |
| ------------------ | -----: |
| Original rows      |      6 |
| Final rows         |      4 |
| Duplicates removed |      2 |
| Empty rows removed |      0 |
| Columns            |      4 |
| Missing cells      |      0 |

The report also provides information about each column, including its data type and remaining missing values.

## What the Tool Does

The cleaning pipeline performs the following operations:

1. Loads CSV or Excel data into a Pandas DataFrame.

2. Standardizes column names.

3. Removes unnecessary whitespace from text values.

4. Removes duplicate records.

5. Handles missing values according to the selected strategy.

6. Removes completely empty rows.

7. Calculates basic dataset statistics.

8. Generates a cleaning report.

9. Saves the cleaned dataset.

## Testing

The project includes automated tests covering the main cleaning operations and missing-value handling strategies.

Run the test suite with:

```bash
python -m pytest
```

Current test result:

```text
9 passed
```

The tests cover:

* Basic data cleaning

* Duplicate removal

* Column-name standardization

* Whitespace removal

* Missing-value detection

* `keep` strategy

* `drop` strategy

* `median` strategy

* `fill` strategy

* Numeric and text missing values

## Example Use Cases

This tool can be useful for:

* Cleaning survey datasets

* Preparing CSV files for analysis

* Removing duplicate customer records

* Standardizing exported spreadsheets

* Preparing datasets for data analysis

* Basic preprocessing before machine learning workflows

* Preparing datasets for bioinformatics analysis

## Future Improvements

Planned improvements include:

* Automatic data-type detection

* More detailed cleaning reports

* Outlier detection

* Advanced data validation

* More missing-value imputation methods

* Configurable duplicate detection

* Batch processing of multiple files

* JSON report generation

* Optional graphical interface

## About

This project was developed as a practical Python portfolio project focused on data cleaning, automation, and reproducible data-processing workflows.

## License

This project is licensed under the MIT License.


