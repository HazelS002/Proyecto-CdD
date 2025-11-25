from ucimlrepo import fetch_ucirepo 
from src import RAW_DATA_PATH, PROCESSED_DATA_PATH
import pandas as pd


def get_heart_disease() -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    heart_disease = fetch_ucirepo(id=45)    # fetch dataset
    X, y = heart_disease.data.features, heart_disease.data.targets 
    metadata = heart_disease.metadata

    return X, y, metadata

def save_heart_disease() -> dict:
    X, y, metadata = get_heart_disease()
    
    X.to_csv(RAW_DATA_PATH + "heart_disease_X.csv", index=False)
    y.to_csv(RAW_DATA_PATH + "heart_disease_y.csv", index=False)

    return metadata

def read_heart_disease(path) -> tuple[pd.DataFrame, pd.DataFrame]:
    X = pd.read_csv(path + "heart_disease_X.csv")
    y = pd.read_csv(path + "heart_disease_y.csv")

    return X, y

def save_processed_data(X: pd.DataFrame, y: pd.DataFrame) -> None:
    pd.DataFrame(X).to_csv(PROCESSED_DATA_PATH+"heart_disease_X_processed.csv",
                           index=False)
    pd.DataFrame(y).to_csv(PROCESSED_DATA_PATH+"heart_disease_y_processed.csv",
                           index=False)

if __name__ == "__main__":
    """ Guardar los datos crudos de heart disease"""
    print(save_heart_disease()) # mostrar metadata
    
