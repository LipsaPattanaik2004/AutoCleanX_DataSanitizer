"""
AutoCleanX - simple reusable cleaning utilities
"""
import pandas as pd
import re

def load_csv(path):
    return pd.read_csv(path)

def summarize_missing(df):
    return df.isnull().sum()

def simple_impute(df, strategy=None):
    """
    strategy: dict column -> value or 'median'/'mean'/'mode'
    """
    for col, strat in (strategy or {}).items():
        if strat == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif strat == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif strat == 'mode':
            df[col].fillna(df[col].mode().iloc[0], inplace=True)
        else:
            df[col].fillna(strat, inplace=True)
    return df

def validate_email(email):
    if pd.isnull(email):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, str(email)))

def detect_outliers_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series[(series < lower) | (series > upper)]

def basic_report(df):
    report = {}
    report['rows'] = len(df)
    report['columns'] = len(df.columns)
    report['missing'] = df.isnull().sum().to_dict()
    return report
