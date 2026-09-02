# Excel Data Cleaner 🧹📊

A lightweight Python tool for cleaning and standardizing messy CSV and Excel datasets.

This project demonstrates practical data-processing and automation skills using **Python, Pandas, and OpenPyXL**.

---

## 🚀 Features

* Clean and standardize column names
* Remove unnecessary whitespace from text fields
* Remove completely empty rows
* Detect and remove duplicate records
* Count missing values
* Generate a cleaning summary
* Read CSV and Excel files
* Export cleaned CSV or Excel files

---

## 🛠️ Technologies

* **Python 3**
* **Pandas**
* **OpenPyXL**

---

## 📁 Project Structure

```text
excel-data-cleaner/
│
├── clean_data.py          # Main data-cleaning script
├── sample.csv             # Example messy dataset
├── cleaned_output.csv     # Example cleaned dataset
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git configuration
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/UKSABUS/excel-data-cleaner.git
cd excel-data-cleaner
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### CSV

```bash
python clean_data.py sample.csv cleaned_output.csv
```

### Excel

```bash
python clean_data.py input.xlsx cleaned_output.xlsx
```

The program automatically detects the input file format based on its extension.

---

## 📊 Example

The included `sample.csv` intentionally contains:

* Duplicate records
* Inconsistent whitespace
* Missing values
* Non-standard column formatting

Running the script produces a cleaned dataset and displays a summary such as:

```text
Loading dataset...
Cleaning dataset...

Cleaning completed successfully!
-----------------------------------
Original rows:      6
Final rows:         4
Duplicates removed: 2
Columns:            4
Missing cells:      1
-----------------------------------
Saved to: cleaned_output.csv
```

---

## 📈 Cleaning Report

The tool reports:

| Metric             | Description                    |
| ------------------ | ------------------------------ |
| Original rows      | Number of rows before cleaning |
| Final rows         | Number of rows after cleaning  |
| Duplicates removed | Duplicate records removed      |
| Columns            | Number of dataset columns      |
| Missing cells      | Total missing values           |

---

## 🎯 Use Cases

This tool can be useful for basic preprocessing of:

* CSV datasets
* Excel spreadsheets
* Survey data
* Experimental datasets
* Small research datasets
* Administrative data

It is designed as a simple command-line utility that can be adapted for different datasets.

---

## 🧪 Example Workflow

```text
Messy CSV / Excel
       ↓
Load dataset
       ↓
Standardize column names
       ↓
Trim text values
       ↓
Remove empty rows
       ↓
Remove duplicates
       ↓
Generate report
       ↓
Export cleaned dataset
```

---

## 💡 What I Learned

Through this project I practiced:

* Working with Pandas DataFrames
* Reading and writing CSV/Excel files
* Data cleaning and preprocessing
* Handling missing values
* Detecting duplicate records
* Basic command-line Python programs
* Structuring a small Python project
* Writing technical documentation

---

## 🔬 Future Improvements

Planned improvements include:

* Automatic missing-value handling
* Configurable cleaning rules
* Support for more file formats
* Interactive command-line options
* Detailed data-quality reports
* Unit tests
* Logging

---

## 👤 About

I'm a Microbiology graduate building practical skills in **Python, data analysis, scientific computing, and bioinformatics**.

My long-term interests include:

* Bioinformatics
* Genomics
* Scientific data analysis
* Computational biology
* Automation

This repository is part of my growing portfolio of practical Python and bioinformatics projects.

---

## 📄 License

This project is available for educational and portfolio purposes.

