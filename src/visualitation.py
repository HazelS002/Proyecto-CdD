import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_correlation_matrix(corr_matrix):
    sns.clustermap(corr_matrix, annot=True, fmt=".2f", cmap='Greens')
    plt.title('Matriz de Correlación')
    plt.xticks(rotation=45)
    plt.show()

def plot_nans(X):
    sns.heatmap(X.isna(), cbar=False, yticklabels=False, cmap='grey')
    plt.title('Mapa de Valores Faltantes')
    plt.xticks(rotation=45)
    plt.show()

def plot_boxs(X):
    sns.boxplot(data=X)
    plt.title('Boxplots de las Variables')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    pass