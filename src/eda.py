import pandas as pd
from src.visualitation import plot_boxs, plot_nans
from sklearn.preprocessing import StandardScaler

def eda(X, y) -> None:
    """ Análisis exploratorio de datos (EDA)
    Args:
        X (pd.DataFrame): características
        y (pd.DataFrame): variable objetivo
    """
    print(80 * "=", "\n", X.head()) # mostrar las primeras filas
    print(80 * "=")
    

    print(X.info()) # información general del dataframe
    print(80 * "=")

    
    print(X.describe()) # estadísticas descriptivas
    print(80 * "=")


    # Hay desvalance entre clases?
    print(pd.value_counts(y["num"])) ; print(80 * "=")


    # Por valores faltantes analisamos las variables 'ca' y 'thal'
    print(pd.value_counts(X["ca"])) ; print(80 * "=")
    print(pd.value_counts(X["thal"])) ; print(80 * "=")

    plot_boxs(X[["ca", "thal"]])
    plot_nans(X[["ca", "thal"]])
    
    return


def transform_data(X, y):
    """
    Transformar los datos
    Args:
        X (pd.DataFrame): características
        y (pd.DataFrame): variable objetivo
    Returns:
        X (np.ndarray): características transformadas
        y (pd.Series): variable objetivo transformada
    """
    y = (y["num"] > 0).astype(int)           # Convertir variable a binaria
    data = X.copy() ; data["y"] = y.values   # para droppear junto etiquetas
    data = data.dropna()                     # eliminar filas con NaNs
    y = data["y"] ; X = data.drop(columns=["y"])    # separar etiquetas

    scaler = StandardScaler()   # escalar
    X = scaler.fit_transform(X)

    return X, y


if __name__ == "__main__":
    from src.load_data import save_heart_disease
    from src import PROCESSED_DATA_PATH, RAW_DATA_PATH
    from src.load_data import read_heart_disease
    from matplotlib import pyplot as plt

    plt.rcParams["figure.constrained_layout.use"] = True # layout de las figuras

    X, y = read_heart_disease(RAW_DATA_PATH)    # leer los datos crudos
    eda(X, y)                                   # ejecutar EDA
    X, y = transform_data(X, y)                 # transformar los datos
    save_heart_disease(X, y, PROCESSED_DATA_PATH) # guardar los datos procesados

