import matplotlib.pyplot as plt

def plot_histogram(serie, column_name):
    plt.hist(serie, bins=10)
    plt.title(f"Distribuição de {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequência")
    plt.show()
