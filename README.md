# PROJECT OVERVIEW
__________________________
AutoCleanX_DataSanitizer is a Python-based automated data cleaning and validation tool designed to simplify preprocessing workflows. It identifies missing values, performs configurable imputations, validates email formats, detects numeric outliers, and exports clean datasets—making it ideal for analytics and data engineering tasks.

## KEY FEATURES
__________________________
Missing value detection & summary
Customizable imputation strategies (mean/median/mode/constant)
Email validity check using regex
Outlier detection using IQR technique
Automated dataset summary reports
Cleaned dataset export for downstream tasks

## TECH STACK
__________________________
Python, Pandas, Regex
Jupyter Notebook
Custom reusable module: autoclean.py

## PROJECT STRUCTURE
__________________________

AutoCleanX_DataSanitizer/
│── autoclean.py
│── autocleanx_notebook.ipynb
│── README.md
└── data/
    └── raw_data.csv

## HOW TO USE
__________________________
Load data using load_csv()
Summarize missing values using summarize_missing()
Apply imputations using simple_impute()
Validate emails using regex-based checks
Detect numeric outliers using IQR filtering
Export cleaned dataset for further analysis

## FUTURE ENHANCEMENTS
__________________________
Add CLI tool (autocleanx --file input.csv)
Build a Streamlit-based UI for drag-and-drop cleaning
Add automated rule-based validation using JSON config
Create versioned releases and pip package

# LIPSA PATTANAIK | ITER SOA UNIVERSITY
