def preparar_dados_para_modelo(df):
    agrupado = df.groupby(['estado', 'municipio', 'bioma', 'ano', 'mes', 'dia'], as_index=False)\
                  .agg({'qtd_focos': 'sum'})

    agrupado['risco_alto'] = (agrupado['qtd_focos'] > 5).astype(int)

    return agrupado