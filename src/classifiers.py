import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import joblib
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score,\
    recall_score, f1_score, balanced_accuracy_score
from src import MODELS_PATH

def classifiers(X_train, y_train):
    """ Entrena varios clasificadores y devuelve un diccionario con los modelos
    entrenados
    Args:
        X_train (np.ndarray): características de entrenamiento
        y_train (np.ndarray): variable objetivo de entrenamiento
    Returns:
        models (dict): diccionario con los modelos entrenados
    """
    # bosque aleatorio
    rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    rf.fit(X_train, y_train)

    # losgistica
    lr = LogisticRegression(random_state=42, max_iter=1000, C=1.0)
    lr.fit(X_train, y_train)


    # red neuronal
    nn = MLPClassifier(hidden_layer_sizes=(50, 25), activation='relu', 
                       random_state=42, max_iter=1000, alpha=0.01)
    nn.fit(X_train, y_train)

    models = {
        'Random Forest': rf,
        'Logistic Regression': lr,
        'Neural Network': nn
    }

    return models
    
def save_models(models:dict[str, object]) -> None:
    """ Guarda los modelos entrenados en archivos .joblib
    Args:
        models (dict): diccionario con los modelos entrenados
    """

    for name, model in models.items():
        joblib.dump(model, MODELS_PATH +\
                    f'{name.lower().replace(" ", "-")}.joblib')

def load_models() -> dict[str, object]:
    """ Carga los modelos entrenados desde archivos .joblib
    Returns:
        models (dict): diccionario con los modelos entrenados
    """
    rf = joblib.load(MODELS_PATH + 'random-forest.joblib')
    lr = joblib.load(MODELS_PATH + 'logistic-regression.joblib')
    nn = joblib.load(MODELS_PATH + 'neural-network.joblib')

    models = {
        'Random Forest': rf,
        'Logistic Regression': lr,
        'Neural Network': nn
    }

    return models

def evaluate_classifiers(X_test, y_test, models:dict[str, object]) -> None:
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        bal_acc = balanced_accuracy_score(y_test, y_pred)

        print(f"\n{name}")
        
        print(f"\tRecall (Sensitivity): {recall:.3f}")
        print(f"\tAccuracy:             {accuracy:.3f}")
        print(f"\tBalanced Accuracy:    {bal_acc:.3f}")
        print(f"\tAUC-ROC:              {auc:.3f}")
        print(f"\tPrecision:            {precision:.3f}")
        print(f"\tF1-score:             {f1:.3f}")

    return



if __name__ == "__main__":
    from src.load_data import read_heart_disease
    from src import PROCESSED_DATA_PATH
    from sklearn.model_selection import train_test_split
    from src.visualitation import plot_matrix_confusion, plot_nn_metrics,\
        plot_logistic_coefficients, plot_feature_importance
    from matplotlib import pyplot as plt

    plt.rcParams["figure.constrained_layout.use"] = True # layout de las figuras

    X, y = read_heart_disease(PROCESSED_DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42,
                                                        stratify=y)

    # # Entrenar y guardar modelos
    # models = classifiers(X_train, y_train.values.ravel())
    # save_models(models)

    models = load_models()  # Cargar modelos entrenados
    evaluate_classifiers(X_test, y_test.values.ravel(), models)

    features_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                      "thalach", "exang", "oldpeak", "slope", "ca", "thal"]

    plot_feature_importance(models['Random Forest'], features_names)

    plot_logistic_coefficients(models['Logistic Regression'], features_names)

    plot_nn_metrics(models['Neural Network'])


    plot_matrix_confusion(X_test, y_test, models)

