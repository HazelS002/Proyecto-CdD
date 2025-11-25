from ucimlrepo import fetch_ucirepo 
from src import RAW_DATA_PATH
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

def read_heart_disease() -> tuple[pd.DataFrame, pd.DataFrame]:
    X = pd.read_csv(RAW_DATA_PATH + "heart_disease_X.csv")
    y = pd.read_csv(RAW_DATA_PATH + "heart_disease_y.csv")

    return X, y

if __name__ == "__main__":
    print(save_heart_disease())
    
