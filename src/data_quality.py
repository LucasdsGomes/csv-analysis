import pandas as pd

# Checando qualidade dos dados

def check_missing_values(df):
    total = df.shape[0]
    missing = df.isnull().sum()
    missing_percent = (missing / total) * 100

    return pd.DataFrame({
        "faltantes": missing,
        "percentual_faltantes": missing_percent.round(2)
    })

def detect_outliers_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = series[(series < lower) | (series > upper)]
    return outliers