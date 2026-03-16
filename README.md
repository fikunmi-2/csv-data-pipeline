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

## Example Input

```csv
name,score
Alice,90
Bob,85
Charlie,70
Dana,92
```

## Example Output
```csv
Highest Score: 92
Lowest Score: 70
Average Score: 84.25

Performance
Excellent: Alice, Dana
Good: Bob
Needs Improvement: Charlie
```
---

## Tech Stack

- Python
- NumPy
- Pandas

---

## Setup

Clone the repository and install dependencies:

- git clone https://github.com/fikunmi-2/csv-data-pipeline.git
- cd csv-data-pipeline
- pip install -r requirements.txt

---

## Goal

This project was built to practice:

- modular Python architecture
- data validation pipelines
- pandas data analysis
- building simple CLI data tools









