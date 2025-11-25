import pandas as pd
from src.load_data import read_heart_disease
from src.visualitation import plot_boxs, plot_nans
from src import RAW_DATA_PATH
from sklearn.preprocessing import StandardScaler

def eda():
    X, y = read_heart_disease(RAW_DATA_PATH) # leer los datos guardados
    print(80 * "=")
    
    
    print(X.head()) # mostrar las primeras filas
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

    return X, y

# función para tranformar los dataos
def transform_data(X, y):
    # Convertir la variable objetivo en binaria
    y = (y["num"] > 0).astype(int)
    X.dropna()

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return X, y

if __name__ == "__main__":
    from src.load_data import save_processed_data
    from matplotlib import pyplot as plt

    plt.rcParams["figure.constrained_layout.use"] = True

    X, y = eda()
    X, y = transform_data(X, y)
    save_processed_data(X, y)

