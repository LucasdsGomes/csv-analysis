import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_histogram(serie, column_name, save=False):
    plt.figure()
    plt.hist(serie, bins=10)
    plt.title(f"Distribuição de {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequência")

    if save:
        os.makedirs("./reports/plots", exist_ok=True)
        filename = f"{column_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = f"./reports/plots/{filename}"
        plt.savefig(filepath)
        print(f"\nGráfico salvo em {filepath}")
    else:
        plt.show()

    plt.close()

def plot_boxplot(series, column_name):
    plt.figure()
    plt.boxplot(series.dropna(), vert=False)
    plt.title(f"Boxplot - {column_name}")
    plt.xlabel(column_name)
    plt.tight_layout()
    plt.show()

