from loader import load_csv
from analysis import analyze_column
from visualization import plot_histogram

def main():
    df = load_csv("../data/data.csv")

    print("\nColunas disponíveis:")
    for i, col in enumerate(df.columns):
        print(f"{i} - {col}")

    while True:
        escolha = input("\nDigite o número da coluna (-1 para sair): ")

        if escolha == "-1":
            break

        if not escolha.isdigit():
            print("Digite um número válido.")
            continue

        idx = int(escolha)

        if idx < 0 or idx >= len(df.columns):
            print("Número inválido.")
            continue

        column_name = df.columns[idx]

        try:
            stats = analyze_column(df, column_name)
        except TypeError as e:
            print(e)
            continue

        print(f"\nEstatísticas de {column_name}:")
        for k, v in stats.items():
            print(f"{k}: {v:.2f}")

        gerar = input("Deseja gerar histograma? (s/n): ").lower()
        if gerar == "s":
            plot_histogram(df[column_name], column_name)

if __name__ == "__main__":
    main()
