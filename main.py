import pandas as pd
from pathlib import Path

arquivo_a_testar = Path('dados/NBA_PLAYERS.csv')
# arquivo_a_testar.touch()

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

if df_carregado is not None:
    print("\n--- Análise de Sujeira ---")
    resultado_analise = analisar_sujeira(df_carregado)

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


