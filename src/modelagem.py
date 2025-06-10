from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def treinar_modelo(agrupado):
    # Codificar variáveis categóricas
    le_bioma = LabelEncoder()
    le_municipio = LabelEncoder()
    le_estado = LabelEncoder()

    agrupado['bioma_cod'] = le_bioma.fit_transform(agrupado['bioma'])
    agrupado['municipio_cod'] = le_municipio.fit_transform(agrupado['municipio'])
    agrupado['estado_cod'] = le_estado.fit_transform(agrupado['estado'])

    # Definir features e alvo
    X = agrupado[['estado_cod', 'municipio_cod', 'bioma_cod', 'ano', 'mes', 'dia']]
    y = agrupado['risco_alto']

    # Dividir treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Criar e treinar o modelo
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Avaliar o modelo
    y_pred = modelo.predict(X_test)

    print("🔍 Acurácia:", accuracy_score(y_test, y_pred))
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

    # Matriz de confusão
    plt.figure(figsize=(6, 5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='YlOrRd', fmt='d')
    plt.title('Matriz de Confusão')
    plt.xlabel('Previsto')
    plt.ylabel('Real')
    plt.show()

    # Retorna o modelo e os encoders
    return modelo, le_municipio, le_bioma, le_estado