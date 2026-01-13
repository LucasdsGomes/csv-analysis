from main import quality_report
import pandas as pd

def generate_report(df: pd.DataFrame, column: str) -> dict:
    quality = quality_report(df, column)

    # 🔹 OUTLIERS: garantir serialização
    outliers = quality.get("outliers", [])

    if isinstance(outliers, pd.Series):
        outliers = outliers.tolist()

    if isinstance(outliers, pd.DataFrame):
        outliers = outliers.to_dict(orient="records")

    report = {
        "column": column,
        "type": "numeric" if pd.api.types.is_numeric_dtype(df[column]) else "categorical",

        "missing": {
            "count": int(quality["missing"]["count"]),
            "percent": float(quality["missing"]["percent"])
        },

        "outliers": outliers,

        "summary": {
            k: float(v)
            for k, v in quality.get("stats", {}).items()
            if pd.notna(v)
        }
    }

    return report
