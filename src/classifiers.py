import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import joblib
from sklearn.metrics import roc_auc_score
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
        joblib.dump(model, MODELS_PATH + f'{name.lower().replace(" ", "-")}.joblib')

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
        accuracy = np.mean(y_pred == y_test)
        auc = roc_auc_score(y_test, y_prob)
        print(f"{name} - Accuracy: {accuracy:.3f}, AUC-ROC: {auc:.3f}")

    return


if __name__ == "__main__":
    from src.load_data import read_heart_disease
    from src import PROCESSED_DATA_PATH
    from sklearn.model_selection import train_test_split

    X, y = read_heart_disease(PROCESSED_DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # # Entrenar y guardar modelos
    # models = classifiers(X_train, y_train.values.ravel())
    # save_models(models)

    models = load_models()
    evaluate_classifiers(X_test, y_test.values.ravel(), models)





# # print(f"Importancia características: {rf.feature_importances_[:3]}...")  # Primeras 3
# # print(f"Coeficientes rango: [{lr.coef_.min():.3f}, {lr.coef_.max():.3f}]")
# # print(f"Arquitectura: {nn.hidden_layer_sizes}")


# # =============================================================================
# # COMPARACIÓN FINAL
# # =============================================================================
# print("\n" + "="*60)
# print("COMPARACIÓN FINAL")
# print("="*60)

# models = {
#     'Random Forest': (y_pred_rf, y_prob_rf, False),
#     'Regresión Logística': (y_pred_lr, y_prob_lr, True),
#     'Red Neuronal': (y_pred_nn, y_prob_nn, True)
# }

# print("\nMÉTRICAS COMPARATIVAS:")
# print(f"{'Modelo':<20} {'Accuracy':<10} {'AUC-ROC':<10} {'Requiere Escalado'}")
# for name, (y_pred, y_prob, scaled) in models.items():
#     acc = np.mean(y_pred == y_test)
#     auc = roc_auc_score(y_test, y_prob)
#     scale_flag = "Sí" if scaled else "No"
#     print(f"{name:<20} {acc:<10.3f} {auc:<10.3f} {scale_flag:<15}")

# # =============================================================================
# # RESULTADOS ESPERADOS
# # =============================================================================
# print("\n" + "="*60)
# print("RESULTADOS ESPERADOS:")
# print("1. Random Forest: ~0.85 accuracy - Más estable, menos overfitting")
# print("2. Regresión Logística: ~0.82 accuracy - Buen balance interpretabilidad/performance")  
# print("3. Red Neuronal: ~0.83 accuracy - Potencial mejor performance con tuning")
# print("\nOBSERVACIÓN: Red Neuronal puede sufrir overfitting sin regularización adecuada")