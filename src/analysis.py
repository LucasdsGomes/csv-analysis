import pandas as pd

def analyze_column(df, column_name):
    serie = df[column_name]

    if not pd.api.types.is_numeric_dtype(serie):
        raise TypeError("A coluna não é numérica.")

    stats = {
        "media": serie.mean(),
        "mediana": serie.median(),
        "min": serie.min(),
        "max": serie.max(),
        "desvio_padrao": serie.std()
    }

    return stats
