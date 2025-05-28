import pandas as pd
from pathlib import Path
import sys

PASTA_ATUAL = Path(__file__).parent
PASTA_SRC = PASTA_ATUAL # Neste caso, é a mesma
print(PASTA_SRC)

if str(PASTA_SRC) not in sys.path:
    sys.path.append(str(PASTA_SRC))

print("--- Tentando importar módulos ---")
try:
    from core.data_loader import carregar_dados
    from core.data_cleaner import analisar_sujeira, limpar_dados_basicos
    from core.data_analyzer import gerar_resumo
    print(">>> Módulos importados! ✅")
except ImportError as err:
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"!!! ERRO CRÍTICO DE IMPORTAÇÃO: {err}")
    sys.exit(1)

def rodar_teste_completo(caminho_arquivo_teste):
    print("INIcIANDO TESTE DE FLUXO")

    # 1. Carregar
    df = carregar_dados(caminho_ou_arquivo) 

    if df is None:
        print(">>> TESTE FALHOU: Não foi possível carregar os dados.")
        return
    
    print("Dados carregados com sucesso. ✅")

    #2. Analisar antes
    print("\n>>> Analisando ANTES...")
    analise_antes = analisar_sujeira(df)
    print(analise_antes)

    # 3. Limpeza
    print("\n>>> Limpando...")
    df_limpo = limpar_dados_basicos(df)
    if df_limpo is None:
        pass
        return
    print("\n>>> Dados Limpos.")

    # 4. Analisar Depois
    analise_depois = analisar_sujeira(df_limpo)
    print(analise_depois)

    # 5. Gerar Resumo
    print("\n>>> Gerando Resumo por 'Position'...")
    resumo = gerar_resumo(df_limpo, 'Position') # Usando 'Position' como exemplo
    if resumo is not None:
        print(resumo.head())
        print(">>> Resumo gerado.")
    else:
        print(">>> TESTE FALHOU: Não foi possível gerar o resumo.")
        return

    print("\n--- ✅ TESTE DE FLUXO CONCLUÍDO COM SUCESSO! ---")

if __name__ == '__main__':
    caminho_ou_arquivo = Path(__file__).parent.parent / 'dados' / 'NBA_PLAYERS.csv'

    print(f"Usando o arquivo de teste: '{caminho_ou_arquivo}'.")

    rodar_teste_completo(caminho_ou_arquivo)