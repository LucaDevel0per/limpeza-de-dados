import pandas as pd

def gerar_resumo(df, coluna_grupo):
    """
    Agrupa o DataFrame pela coluna_grupo e conta as ocorrências.
    Retorna um DataFrame com o resumo ordenado.
    """
    if df is None or coluna_grupo not in df.columns:
        print(f"Erro: DataFrame nulo ou coluna '{coluna_grupo}' não encontrada.")
        return None

    print(f"\n--- Gerando Resumo por '{coluna_grupo}' ---")
    try:
        resumo = df.groupby(coluna_grupo).size().reset_index(name='Contagem')
        resumo_ordenado = resumo.sort_values(by='Contagem', ascending=False)
        return resumo_ordenado
    except Exception as e:
        print(f"Erro ao gerar resumo: {e}")
        return None

# (Poderíamos adicionar a função .agg() aqui também no futuro)