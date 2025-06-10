import pandas as pd
import matplotlib.pyplot as plt


def prever_municipios_mes_com_grafico(modelo, agrupado, le_municipio, ano, mes):
    """
    Faz uma previsão dos municípios com maior risco de incêndio para um mês específico
    e gera um gráfico de barras com os 10 maiores.

    Parâmetros:
    - modelo: modelo treinado (RandomForest)
    - agrupado: dataframe agrupado
    - le_municipio: label encoder treinado para municípios
    - ano: ano da previsão (int)
    - mes: mês da previsão (int)

    Retorna:
    - ranking: lista com os 10 municípios e suas probabilidades de risco
    """

    municipios = agrupado['municipio'].unique()
    previsoes = []

    for municipio in municipios:
        try:
            cod_municipio = le_municipio.transform([municipio])[0]
            cod_estado = agrupado[agrupado['municipio'] == municipio]['estado_cod'].iloc[0]
            cod_bioma = agrupado[agrupado['municipio'] == municipio]['bioma_cod'].iloc[0]

            entradas = pd.DataFrame({
                'estado_cod': [cod_estado] * 30,
                'municipio_cod': [cod_municipio] * 30,
                'bioma_cod': [cod_bioma] * 30,
                'ano': [ano] * 30,
                'mes': [mes] * 30,
                'dia': list(range(1, 31))
            })

            prob_risco = modelo.predict_proba(entradas)[:, 1]
            media_prob = prob_risco.mean()

            previsoes.append((municipio, media_prob))
        except Exception as e:
            print(f"Erro no município {municipio}: {e}")

    ranking = sorted(previsoes, key=lambda x: x[1], reverse=True)[:10]

    municipios_top = [item[0] for item in ranking]
    probs_top = [item[1] for item in ranking]

    print(f"\n🔮 Previsão de risco médio para {mes:02d}/{ano}:")
    for municipio, prob in ranking:
        print(f"{municipio}: {prob:.2%} de risco médio no mês")

    # Plotar gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(municipios_top, probs_top, color='darkred')
    plt.title(f'🔥 Top 10 municípios com maior risco de incêndio em {mes:02d}/{ano}')
    plt.ylabel('Probabilidade média de risco')
    plt.xlabel('Município')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    return ranking