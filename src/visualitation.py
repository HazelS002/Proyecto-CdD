import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np


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


def plot_matrix_confusion(X_test, y_test, models:dict[str, object]) -> None:
    _, axes = plt.subplots(1, 3)

    for i, (name, model) in enumerate(models.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)

        sns.heatmap(cm, annot=True, cmap='Greens', ax=axes[i], cbar=False,
                    xticklabels=['No Enfermo', 'Enfermo'],
                    yticklabels=['No Enfermo', 'Enfermo'])
        # plt.xticks(rotation=45) ; plt.yticks(rotation=45)
        axes[i].set_title(f'{name}')

    axes[1].set_xlabel('Predicción')
    axes[0].set_ylabel('Real')

    plt.suptitle('Matriz de Confusión para modelos')
    plt.show()


def plot_feature_importance(model, feature_names, top_n=None):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    if top_n is not None: indices = indices[:top_n]

    sorted_importances = importances[indices]
    sorted_features = [feature_names[i] for i in indices]

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=sorted_importances,
        y=sorted_features,
        hue=sorted_features,   # Se usa hue para evitar el warning
        dodge=False,
        legend=False,          # Ocultar leyenda ya que no aporta información
        palette="viridis"
    )

    plt.xlabel("Importancia")
    plt.ylabel("Características")
    plt.title("Importancia de las Características (Random Forest)")
    plt.show()

def plot_logistic_coefficients(model, feature_names, top_n=None):
    # Extraer coeficientes
    coefs = model.coef_[0]

    # Ordenar por magnitud absoluta
    indices = np.argsort(np.abs(coefs))[::-1]

    if top_n is not None: indices = indices[:top_n]

    sorted_coefs = coefs[indices]
    sorted_features = [feature_names[i] for i in indices]

    sns.barplot(
        x=sorted_coefs,
        y=sorted_features,
        orient="h",
        palette="viridis",
        legend=False,
        hue=sorted_features,
        dodge=False
    )

    plt.title("Coeficientes de la Regresión Logística")
    plt.xlabel("Coeficiente")
    plt.ylabel("Características")
    plt.tight_layout()
    plt.show()

def plot_nn_metrics(model):
    loss_values = model.loss_curve_
    sns.lineplot(x=range(len(loss_values)), y=loss_values)
    plt.xlabel("Épocas")
    plt.ylabel("Loss")
    plt.title("Curva de Pérdida de la Red Neuronal")
    plt.show()

if __name__ == "__main__":
    pass