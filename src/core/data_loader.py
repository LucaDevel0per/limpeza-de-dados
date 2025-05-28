import pandas as pd

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