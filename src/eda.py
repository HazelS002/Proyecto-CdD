import pandas as pd
from src.load_data import read_heart_disease
import seaborn as sns
import matplotlib.pyplot as plt

def eda():
    X, y = read_heart_disease()
    print(80 * "=")
    
    print(X.head())
    print(80 * "=")
    
    print(X.info())
    print(80 * "=")
    
    print(X.describe())
    print(80 * "=")


    # Hay desvalance entre clases?
    print(pd.value_counts(y["num"]))
    print(80 * "=")


    # Por valores faltantes analisamos las variables 'ca' y 'thal'
    print(pd.value_counts(X["ca"]))
    print(80 * "=")

    print(pd.value_counts(X["thal"]))
    print(80 * "=")

    sns.boxplot(data=X[["ca", "thal"]])
    plt.show()


    return

if __name__ == "__main__":
    eda()