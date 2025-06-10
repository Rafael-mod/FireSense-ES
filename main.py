from src.carregar_dados import carregar_dados
from src.analise_dados import preparar_dados_para_modelo
from src.modelagem import treinar_modelo
from src.visualizacoes import grafico_top_municipios, criar_mapa_focos_por_ano
from src.previsao import prever_municipios_mes_com_grafico

# Caminhos dos CSV
arquivos = [
    'data/focos_es_2020.csv',
    'data/focos_es_2021.csv',
    'data/focos_es_2022.csv',
    'data/focos_es_2023.csv',
    'data/focos_es_2024.csv'
]

# Pipeline
df = carregar_dados(arquivos)
agrupado = preparar_dados_para_modelo(df)
modelo, le_municipio, le_bioma, le_estado = treinar_modelo(agrupado)
# Visualizações
grafico_top_municipios(df)
prever_municipios_mes_com_grafico(
    modelo=modelo,
    agrupado=agrupado,
    le_municipio=le_municipio,
    ano=2025,
    mes=1
)
criar_mapa_focos_por_ano(df, ano=2024)
