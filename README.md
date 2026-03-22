# CSV Data Pipeline

A modular Python pipeline for **cleaning, analyzing, and summarizing CSV data**.

This project demonstrates how raw CSV data can be transformed into **reliable insights** using a structured data-processing workflow built with **pandas** and **NumPy**.

---

## Pipeline Flow

CSV File -> file_cleaner -> data_analyzer -> data_formatter -> CLI Output

Each stage has a **single responsibility**, making the pipeline easy to maintain and extend.

---

## Features

- CSV file validation and loading
- Column name normalization
- Removal of empty or invalid rows
- Numeric score validation
- Statistical analysis (min, max, average)
- Performance categorization
- Human-readable and machine-readable output
- Modular pipeline architecture

---
## CLI Input Structure

### Without output File (prints to console) 
```bash
$ python -m cli.cli_tool data/sample_data.csv -m human
$ python -m cli.cli_tool data/sample_data.csv -m machine
```
### With output file (saves result to a file)
```bash
$ python -m cli.cli_tool data/sample_data.csv -m human -o data/human_output.txt
$ python -m cli.cli_tool data/sample_data.csv -m machine -o data/machine_output.json
```

## Example Input
```csv
name,score
Alice,90
Bob,85
Charlie,70
Dana,92
```
---

## Example Human-Readable Output
```txt
Statistics:
- Highest Score: 92.00
- Lowest Score: 70.00
- Average Score: 84.25

Performance:
- Excellent: Alice, Dana
- Good: Bob
- Needs Improvement: Charlie

Metadata:
- Number of Rows (original): 4
- Number of Rows Missing values: 0
- Number of Rows with invalid scores: 0
- Number of Rows (after cleaning): 4
```

## Example Machine Readable Output
```json
{
  "Status": "Success",
  "Statistics": {
    "Highest Score": 92.0,
    "Lowest Score": 70.0,
    "Average Score": 84.25
  },
  "Performance": {
    "Excellent": ["Alice", "Dana"],
    "Good": ["Bob"],
    "Needs Improvement": ["Charlie"]
  },
  "Metadata": {
    "Number of Rows (original)": 4,
    "Number of Rows Missing values": 0,
    "Number of Rows with invalid scores": 0,
    "Number of Rows (after cleaning)": 4
  }
}
```
---

## Tech Stack

- Python
- NumPy
- Pandas
- Argparse

---

## Setup

Clone the repository and install dependencies:
```bash
$ git clone https://github.com/fikunmi-2/csv-data-pipeline.git
$ cd csv-data-pipeline
$ pip install -r requirements.txt
```

---

## Goal

This project was built to practice:

- modular Python architecture
- data validation pipelines
- pandas data analysis
- building simple CLI data tools
