import pandas as pd
from pandas.api.types import is_numeric_dtype, is_object_dtype

def analisar_sujeira(df):
    if df is None:
        return "Erro: Nenhum DataFrame para analisar."

    num_linhas, num_colunas = df.shape
    nans_por_coluna = df.isnull().sum()
    total_nans = nans_por_coluna.sum()
    num_duplicadas = df.duplicated().sum()

    analise = {
        'Formato (Linhas, Colunas)': (num_linhas, num_colunas),
        'Total de Células Vazias (NaN)': int(total_nans),
        'Linhas Duplicadas': int(num_duplicadas),
        'Células Vazias por Colunas': nans_por_coluna
    }
    return analise

def limpar_dados_basicos(df):
    if df is None:
        return None
    print("\n--- Iniciando Limpeza Básica ---")
    df_limpo = df.copy()

    # Remoção de coluna fantasma 'Unnamed: 0'
    if 'Unnamed: 0' in df_limpo.columns:
        df_limpo.drop(columns=['Unnamed: 0'], inplace=True)
        print("Coluna 'Unnamed: 0' removida.")
    for coluna in df_limpo.columns:
        # se a coluna tiver NaN
        if df_limpo[coluna].isnull().any():
            if is_numeric_dtype(df_limpo[coluna]):
                mediana = df_limpo[coluna].median()
                # df_limpo[coluna].fillna(mediana, inplace=True)
                df_limpo[coluna] = df_limpo[coluna].fillna(mediana)
                print(f"Coluna numérica '{coluna}' preenchida com mediana ({mediana:.2f}).")
            elif is_object_dtype(df_limpo[coluna]):
                # df_limpo[coluna].fillna("Unknown", inplace=True)
                df_limpo[coluna] = df_limpo[coluna].fillna("Unknown")
                print(f"Coluna de objeto '{coluna}' preenchida com 'Unknown'.")
            else:
                print(f"Coluna '{coluna}' ({df_limpo[coluna].dtype}) com NaNs não tratada.")

    # Remove duplicatas
    duplicatas_antes = df_limpo.duplicated().sum()
    if duplicatas_antes > 0:
        # df_limpo.drop_duplicates(inplace=True)
        df_limpo = df_limpo.drop_duplicates()
        print(f"{duplicatas_antes} linhas duplicadas foram removidas.")
    else:
        print("Nenhuma duplicata encontrada.")

    print("--- Limpeza Básica Concluída ---")
    return df_limpo