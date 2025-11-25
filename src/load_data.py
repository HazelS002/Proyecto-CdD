from ucimlrepo import fetch_ucirepo
import pandas as pd


def get_heart_disease() -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """ Descarga el conjunto de datos de heart disease desde UCI ML Repository
    Returns:
        X (pd.DataFrame): características
        y (pd.DataFrame): variable objetivo
        metadata (dict): metadatos del conjunto de datos
    """
    heart_disease = fetch_ucirepo(id=45)    # fetch dataset
    X, y = heart_disease.data.features, heart_disease.data.targets 
    metadata = heart_disease.metadata

    return X, y, metadata

def save_heart_disease(X, y, path:str) -> None:
    """ Guarda los datos de heart disease en archivos CSV
    Args:
        X (pd.DataFrame): características
        y (pd.DataFrame): variable objetivo
        path (str): ruta donde se guardarán los archivos
    """
    X, y = pd.DataFrame(X), pd.DataFrame(y) # convertir a DataFrame
    

    X.to_csv(path + "heart_disease_X.csv", index=False)
    y.to_csv(path + "heart_disease_y.csv", index=False)
    return

def read_heart_disease(path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """ Lee los datos de heart disease desde archivos CSV
    Args:
        path (str): ruta donde se encuentran los archivos
    Returns:
        X (pd.DataFrame): características
        y (pd.DataFrame): variable objetivo
    """

    X = pd.read_csv(path + "heart_disease_X.csv")
    y = pd.read_csv(path + "heart_disease_y.csv")

    return X, y

if __name__ == "__main__":
    """ Guardar los datos crudos de heart disease"""
    from src import RAW_DATA_PATH

    X, y, metadata = get_heart_disease()
    save_heart_disease(X, y, RAW_DATA_PATH)

    print(metadata)
    
