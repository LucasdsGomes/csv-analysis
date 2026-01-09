import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("O arquivo CSV está vazio.")

    return df
