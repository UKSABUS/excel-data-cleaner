# Excel Data Cleaner 🧹📊

A Python tool for cleaning and standardizing messy CSV and Excel datasets.

## Features

- Remove duplicate records
- Standardize column names
- Remove unnecessary whitespace
- Remove completely empty rows
- Detect missing values
- Generate a cleaning report
- Export cleaned CSV or Excel files

## Technologies

- Python
- Pandas
- OpenPyXL

## Project Structure

    excel-data-cleaner/
    │
    ├── clean_data.py
    ├── requirements.txt
    ├── sample.csv
    ├── README.md
    └── .gitignore

## Installation

Clone the repository and install the required packages:

    pip install -r requirements.txt

## Usage

For CSV files:

    python clean_data.py sample.csv cleaned_output.csv

For Excel files:

    python clean_data.py input.xlsx cleaned_output.xlsx

## Example

The included `sample.csv` contains intentionally messy data,
including duplicate records, unnecessary whitespace, and missing values.

The program processes the dataset and produces a cleaned output file.

## Cleaning Report

The program reports:

- Original number of rows
- Final number of rows
- Number of duplicates removed
- Number of columns
- Number of missing cells

## Purpose

This project demonstrates practical Python skills in:

- Data cleaning
- Data preprocessing
- Pandas
- CSV/Excel processing
- Basic automation

## Author

Microbiology graduate interested in Python,
data analysis, scientific computing, and bioinformatics.
