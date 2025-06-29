import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import MarkerCluster


def grafico_top_municipios(df):
    ranking_df = df.groupby('municipio', as_index=False)['qtd_focos'].sum()
    ranking_df = ranking_df.sort_values(by='qtd_focos', ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    plt.bar(ranking_df['municipio'], ranking_df['qtd_focos'], color='darkorange')
    plt.title('🔥 Top 10 Municípios com Mais Focos (2020-2024)')
    plt.ylabel('Quantidade de Focos')
    plt.xlabel('Município')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

#GRÁFICO HTML COM FOLIUM
def criar_mapa_focos_por_ano(df, ano):
    df_mapa = df[df['ano'] == ano]

    mapa = folium.Map(location=[-20.3155, -40.3128], zoom_start=7)
    marker_cluster = MarkerCluster().add_to(mapa)

    for _, row in df_mapa.iterrows():
        if not pd.isnull(row['lat']) and not pd.isnull(row['lon']):
            folium.CircleMarker(
                location=[row['lat'], row['lon']],
                radius=4,
                popup=f"Município: {row['municipio']}<br>Data: {row['data_pas'].date()}",
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.7
            ).add_to(marker_cluster)

    nome_arquivo = f"outputs/mapa_focos_{ano}.html"
    mapa.save(nome_arquivo)
    print(f"✅ Mapa salvo como {nome_arquivo}")



    #gráfico ideia do professor

def grafico_linhas_cachoeiro(df):
    # Filtra apenas os dados de Cachoeiro de Itapemirim
    df_cachoeiro = df[df['municipio'].str.lower() == 'cachoeiro de itapemirim']

    # Agrupa por ano e soma os focos
    dados_anuais = df_cachoeiro.groupby('ano')['qtd_focos'].sum().reset_index()

    # Gera o gráfico de linha
    plt.figure(figsize=(10, 5))
    plt.plot(dados_anuais['ano'], dados_anuais['qtd_focos'], marker='o', linestyle='-', color='firebrick')
    plt.title('📈 Focos de Incêndio em Cachoeiro de Itapemirim (2020–2024)')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de Focos')
    plt.grid(True)
    plt.xticks(dados_anuais['ano'])  # Garante que só os anos da base apareçam
    plt.tight_layout()
    plt.show()