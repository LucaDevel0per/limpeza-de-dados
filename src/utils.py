# FUNÇÕES (carregar_dados, analisar_sujeira, etc.)

import pandas as pd
from pandas.api.types import is_numeric_dtype, is_object_dtype
from pathlib import Path

arquivo_a_testar = Path('dados/NBA_PLAYERS.csv')
df = pd.read_csv(arquivo_a_testar)


def carregar_dados(caminho_ou_arquivo):
    """
    Tenta carregar um arquivo como CSV (com ',' ou ';') ou Excel.
    Retorna um DataFrame ou None se falhar.
    """
    if caminho_ou_arquivo is None:
        return None

    nome_arquivo = getattr(caminho_ou_arquivo, 'name', str(caminho_ou_arquivo))

    try:
        if nome_arquivo.endswith('.csv'):
            print("Tentando ler como CSV...")
            try:
                # Tenta com vírgula primeiro
                df = pd.read_csv(caminho_ou_arquivo)
                print("Lido como CSV (vírgula).")
                return df
            except Exception:
                # Se falhar, tenta com ponto e vírgula
                if hasattr(caminho_ou_arquivo, 'seek'):
                    caminho_ou_arquivo.seek(0)
                df = pd.read_csv(caminho_ou_arquivo, sep=';')
                print("Lido como CSV (ponto e vírgula).")
                return df
        elif nome_arquivo.endswith('.xlsx') or nome_arquivo.endswith('.xls'):
            print("Tentando ler como Excel...")
            df = pd.read_excel(caminho_ou_arquivo)
            print("Lido como Excel.")
            return df
        else:
            print("Formato de arquivo não suportado (apenas .csv ou .xlsx).")
            return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

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

df_carregado = carregar_dados(arquivo_a_testar)

def analise_sujeira(df_que_foi_carregado):
    if df_que_foi_carregado is not None:
        print("\n--- Análise de Sujeira ---")
        resultado_analise = analisar_sujeira(df_que_foi_carregado)

        # Verificar se o resultado é um dicionário antes de iterar
        if isinstance(resultado_analise, dict):
            # Imprimindo o resultado de forma legível
            for chave, valor in resultado_analise.items():
                if isinstance(valor, pd.Series):
                    print(f"\n{chave}:")
                    print(valor)
                else:
                    print(f"{chave}: {valor}")
        else:
            print(resultado_analise)  # Imprime a mensagem de erro
    else:
        print("Falha ao carregar o arquivo de teste.")

analise_sujeira(df_carregado)

def limpar_dados_basicos(df):
    if df is None:
        return None
    print("\n--- Iniciando Limpeza Básica ---")
    df_limpo = df.copy()

    for coluna in df_limpo.columns:
        # se a coluna tiver NaN
        if df_limpo[coluna].isnull().any():
            if is_numeric_dtype(df_limpo[coluna]):
                mediana = df_limpo[coluna].median()
                df_limpo[coluna].fillna(mediana, inplace=True)
                print(f"Coluna numérica '{coluna}' preenchida com mediana ({mediana:.2f}).")
            elif is_object_dtype(df_limpo[coluna]):
                df_limpo[coluna].fillna("Unknown", inplace=True)
                print(f"Coluna de objeto '{coluna}' preenchida com 'Unknown'.")
            else:
                print(f"Coluna '{coluna}' ({df_limpo[coluna].dtype}) com NaNs não tratada.")

    # Remove duplicatas
    duplicatas_antes = df_limpo.duplicated().sum()
    if duplicatas_antes > 0:
        df_limpo.drop_duplicates(inplace=True)
        print(f"{duplicatas_antes} linhas duplicadas foram removidas.")
    else:
        print("Nenhuma duplicata encontrada.")

    print("--- Limpeza Básica Concluída ---")
    return df_limpo

# df_carregado = carregar_dados(arquivo_a_testar)

def fazer_limpeza(df_carregado):
    if df_carregado is not None:
        # 1. Analisa ANTES
        print("\n--- ANÁLISE ANTES DA LIMPEZA ---")
        analise_antes = analisar_sujeira(df_carregado)
        if isinstance(analise_antes, dict):
            for k, v in analise_antes.items(): print(f"{k}: {v}" if not isinstance(v, pd.Series) else f"\n{k}:\n{v}")
        else:
            print(analise_antes)

        # 2. Limpa
        df_carregado_limpo = limpar_dados_basicos(df_carregado)

        # 3. Analisa DEPOIS
        print("\n--- ANÁLISE DEPOIS DA LIMPEZA ---")
        analise_depois = analisar_sujeira(df_carregado_limpo)
        if isinstance(analise_depois, dict):
            for k, v in analise_depois.items(): print(f"{k}: {v}" if not isinstance(v, pd.Series) else f"\n{k}:\n{v}")
        else:
            print(analise_depois)

    else:
        print("Falha ao carregar o arquivo da NBA.")

fazer_limpeza(df_carregado)