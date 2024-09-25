import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def clasificacion_arbol_decision():
    interacciones = pd.read_csv('../../data/interacciones.csv')

    interacciones['Compra'] = interacciones['Acción'].apply(lambda x: 1 if x == 'Compra' else 0)
    
    X = interacciones[['ID_Usuario', 'ID_Producto']]  
    y = interacciones['Compra']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    column_transformer = ColumnTransformer(
        transformers=[('onehot', OneHotEncoder(handle_unknown='ignore'), ['ID_Usuario', 'ID_Producto'])],
        remainder='passthrough'
    )

    clf = Pipeline(steps=[
        ('preprocessor', column_transformer),
        ('classifier', DecisionTreeClassifier(random_state=42, class_weight='balanced'))  
    ])

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo de Árbol de Decisión: {accuracy:.2f}')
    
    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Compra', 'Compra'], yticklabels=['No Compra', 'Compra'])
    plt.xlabel('Predicción')
    plt.ylabel('Real')
    plt.title('Matriz de Confusión')
    plt.savefig('matriz_confusion.png') 
    print("Matriz de confusión guardada como 'matriz_confusion.png'.")

    y_prob = clf.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)
    
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], linestyle='--', color='grey')
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title('Curva ROC')
    plt.legend()
    plt.savefig('curva_roc.png')  
    print("Curva ROC guardada como 'curva_roc.png'.")

    param_grid = {
        'classifier__max_depth': [None, 10, 20, 30],
        'classifier__min_samples_split': [2, 10, 20],
        'classifier__min_samples_leaf': [1, 5, 10]
    }

    grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print(f"Mejores hiperparámetros encontrados: {grid_search.best_params_}")
    print(f"Precisión tras ajuste de hiperparámetros: {grid_search.best_score_:.2f}")

if __name__ == '__main__':
    clasificacion_arbol_decision()
