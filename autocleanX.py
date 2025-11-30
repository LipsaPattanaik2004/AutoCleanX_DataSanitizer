import pandas as pd
from autoclean import load_csv, summarize_missing, simple_impute, validate_email, detect_outliers_iqr, basic_report

# Load data
raw = load_csv('data/raw_data.csv')
raw

print(summarize_missing(raw))

strategy = {'age':'median','salary':'mean','name':'Unknown'}
cleaned = simple_impute(raw.copy(), strategy)
print(cleaned)

raw['email_valid'] = raw['email'].apply(validate_email)
print(raw[['email','email_valid']])

raw['salary'] = pd.to_numeric(raw['salary'], errors='coerce')
outliers = detect_outliers_iqr(raw['salary'].dropna())
print('Outliers:\n', outliers)

report = basic_report(raw)
print(report)
raw.to_csv('data/raw_data_cleaned.csv', index=False)
print('Exported cleaned file to data/raw_data_cleaned.csv')
