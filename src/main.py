from loader import load_csv
from analysis import analyze_column
from visualization import plot_histogram
from datetime import datetime
import os
import argparse
from data_quality import check_missing_values, detect_outliers_iqr
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        description="Análise exploratória de dados (EDA)"
    )

    parser.add_argument(
        "--file",
        type=str,
        default="../data/data.csv",
        help="Caminho do arquivo CSV"
    )

    parser.add_argument(
        "--column",
        type=str,
        help="Nome da coluna para análise"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Analisar todas as colunas numéricas"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Salvar estatísticas em arquivo"
    )

    parser.add_argument(
        "--plot",
        action="store_true",
        help="Gerar histograma da coluna"
    )

    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verificar qualidade dos dados da coluna especificada"
    )

    parser.add_argument(
        "--save-quality",
        action="store_true",
        help="Salvar relatório de qualidade dos dados"
    )

    return parser.parse_args()


def save_stats(stats, title):
    os.makedirs("./reports", exist_ok=True)

    filename = f"{title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = f"./reports/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Estatísticas de {title}\n")
        f.write("-" * 30 + "\n")
        for k, v in stats.items():
            f.write(f"{k}: {v:.2f}\n")

    print(f"📄 Estatísticas salvas em {filepath}")

def format_value(value):
    if isinstance(value, pd.Series):
        return value.iloc[0]
    return value

def save_quality_report(column, missing_stats, outliers):
    os.makedirs("./reports", exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = f"./reports/qualidade_{column}_{timestamp}.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("RELATÓRIO DE QUALIDADE DE DADOS\n")
        f.write(f"Coluna analisada: {column}\n")
        f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")

        f.write("🔍 VALORES AUSENTES\n")
        f.write("-" * 50 + "\n")
        for k, v in missing_stats.items():
            f.write(f"{k:<25}: {format_value(v)}\n")

        f.write("\n🚨 OUTLIERS DETECTADOS\n")
        f.write("-" * 50 + "\n")

        if len(outliers) == 0:
            f.write("Nenhum outlier encontrado.\n")
        else:
            f.write(f"Total de outliers: {len(outliers)}\n\n")
            for i, val in enumerate(outliers.values, 1):
                f.write(f"{i:>3}. {val}\n")

    # Feedback no console
    print("\nRelatório de qualidade gerado com sucesso!")
    print(f"Arquivo: {filepath}\n")

def quality_report(df: pd.DataFrame, column: str) -> dict:
    series = df[column]

    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError("Nome/Departamento são colunas categóricas e não podem ser analisadas para qualidade numérica.")

    # 🔹 Missing
    missing_count = series.isna().sum()
    missing_percent = (missing_count / len(series)) * 100

    # 🔹 Outliers (IQR)
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1

    outliers = series[(series < Q1 - 1.5 * IQR) | (series > Q3 + 1.5 * IQR)]

    return {
        "missing": {
            "count": int(missing_count),
            "percent": float(missing_percent)
        },
        "outliers": outliers,
        "stats": series.describe().to_dict()
    }

def main():
    args = parse_args()

    df = load_csv(args.file)

    # 🔹 Análise de uma coluna específica
    if args.column:
        if args.column not in df.columns:
            print("Coluna não encontrada.")
            return

        try:
            stats = analyze_column(df, args.column)
        except TypeError as e:
            print(f"Erro ao analisar coluna: {e}")
            return

        print(f"\n📊 Estatísticas de {args.column}:")
        for k, v in stats.items():
            print(f"{k}: {v:.2f}")

        if args.save and not args.verify:
            save_stats(stats, args.column)


        if args.plot:
            plot_histogram(df[args.column], args.column, save=True)

        if args.verify:
            missing_stats = check_missing_values(df[[args.column]])
            outliers = detect_outliers_iqr(df[args.column])

            if args.save_quality:
                save_quality_report(args.column, missing_stats, outliers)
        return

    # 🔹 Análise de todas as colunas
    if args.all:
        geral_stats = {}

        for col in df.columns:
            try:
                stats = analyze_column(df, col)
                geral_stats[col] = stats
            except TypeError:
                continue

        if not geral_stats:
            print("Nenhuma coluna numérica encontrada.")
            return

        for col, stats in geral_stats.items():
            print(f"\n📊 Estatísticas de {col}:")
            for k, v in stats.items():
                print(f"{k}: {v:.2f}")

        if args.save:
            os.makedirs("./reports", exist_ok=True)
            filename = f"estatisticas_gerais_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            filepath = f"./reports/{filename}"

            with open(filepath, "w", encoding="utf-8") as f:
                for col, stats in geral_stats.items():
                    f.write(f"Estatísticas de {col}:\n")
                    for k, v in stats.items():
                        f.write(f"  {k}: {v:.2f}\n")
                    f.write("\n")

            print(f"\n📄 Estatísticas gerais salvas em {filepath}")

        return

    print("Nenhuma ação definida. Use --column ou --all.")


if __name__ == "__main__":
    main()
