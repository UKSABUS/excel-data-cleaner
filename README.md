# Excel Data Cleaner 🧹📊

A lightweight Python tool for cleaning and standardizing CSV and Excel datasets.

This project automates common data-cleaning tasks such as removing duplicate records, standardizing column names, trimming unnecessary whitespace, removing completely empty rows, and generating a simple cleaning report.

## Features

* Remove duplicate rows
* Standardize column names
* Trim unnecessary whitespace from text fields
* Remove completely empty rows
* Detect missing values
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

The program loads the dataset, applies the cleaning operations, generates a summary report, and saves the cleaned dataset.

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

### Output

```text
Cleaning completed successfully!
----------------------------------------
Original rows:      6
Final rows:         4
Duplicates removed: 2
Columns:            4
Missing cells:      1
----------------------------------------
Saved to: cleaned_output.csv
```

## Cleaning Report

| Metric             | Result |
| ------------------ | -----: |
| Original rows      |      6 |
| Final rows         |      4 |
| Duplicates removed |      2 |
| Columns            |      4 |
| Missing cells      |      1 |

## What the Tool Does

The cleaning pipeline performs the following operations:

1. Loads CSV or Excel data into a Pandas DataFrame.
2. Standardizes column names.
3. Removes unnecessary whitespace from text values.
4. Removes completely empty rows.
5. Detects and removes duplicate records.
6. Calculates basic dataset statistics.
7. Saves the cleaned dataset.

## Testing

The project includes automated tests covering the main cleaning operations.

Run the test suite with:

```bash
python -m pytest
```

Expected result:

```text
4 passed
```

## Example Use Cases

This tool can be useful for:

* Cleaning survey datasets
* Preparing CSV files for analysis
* Removing duplicate customer records
* Standardizing exported spreadsheets
* Preparing datasets for data analysis
* Basic preprocessing before machine learning workflows

## Future Improvements

Planned improvements include:

* Missing-value handling strategies
* Automatic data-type detection
* More detailed cleaning reports
* Support for larger datasets
* Configurable cleaning options
* Batch processing of multiple files
* Optional graphical interface

## About

This project was developed as a practical Python portfolio project focused on data cleaning, automation, and reproducible data-processing workflows.

## License

This project is licensed under the MIT License.

