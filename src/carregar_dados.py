import pandas as pd

def carregar_dados(arquivos):
    lista_df = []
    for arquivo in arquivos:
        df_temp = pd.read_csv(arquivo, sep=';', encoding='utf-8')
        df_temp['data_pas'] = pd.to_datetime(df_temp['data_pas'], errors='coerce')
        lista_df.append(df_temp)

    df = pd.concat(lista_df, ignore_index=True)
    df = df.dropna(subset=['data_pas'])

    df['ano'] = df['data_pas'].dt.year
    df['mes'] = df['data_pas'].dt.month
    df['dia'] = df['data_pas'].dt.day
    df['dia_semana'] = df['data_pas'].dt.dayofweek
    df['qtd_focos'] = 1

    return df