import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import matplotlib.pyplot as plt

# --- Bloco para garantir que Python ache a pasta 'core' ---
PASTA_ATUAL = Path(__file__).parent
if str(PASTA_ATUAL) not in sys.path:
    sys.path.append(str(PASTA_ATUAL))
# -----------------------------------------------------------

try:
    from core.data_loader import carregar_dados
    from core.data_cleaner import analisar_sujeira, limpar_dados_basicos
    from core.data_analyzer import gerar_resumo
except ImportError as e:
    st.error(f"ERRO DE IMPORTAÇÃO: {e}.")
    st.stop()

# --- Funções de Exibição ---
def mostrar_analise(resultado_analise, titulo="Análise"):
    st.subheader(titulo)
    if isinstance(resultado_analise, dict):
        col1, col2 = st.columns(2)
        col1.metric("Linhas", resultado_analise['Formato (Linhas, Colunas)'][0])
        col1.metric("Colunas", resultado_analise['Formato (Linhas, Colunas)'][1])
        col2.metric("NaNs Totais", resultado_analise['Total de Células Vazias (NaN)'])
        col2.metric("Duplicatas", resultado_analise['Linhas Duplicadas'])
        st.write("NaNs por Coluna:")
        st.dataframe(resultado_analise['Células Vazias por Colunas'])
    else:
        st.error(resultado_analise)

# --- LAYOUT DO APP STREAMLIT ---
st.set_page_config(page_title="App Limpeza", layout="wide", initial_sidebar_state="expanded")
st.title("Ferramenta de Limpeza de Dados")
st.markdown("Suba seu arquivo CSV ou Excel e deixe a mágica acontecer!")

# --- Barra Lateral (Sidebar) ---
st.sidebar.header("1. Carregar Dados")
uploaded_file = st.sidebar.file_uploader("Escolha seu arquivo:", type=['csv', 'xlsx'])

# --- Lógica Principal ---
if uploaded_file is not None:
    # Inicializa o estado da sessão se um NOVO arquivo for carregado
    # ou se não houver df_original
    if 'nome_arquivo_carregado' not in st.session_state or st.session_state.nome_arquivo_carregado != uploaded_file.name:
        st.session_state.nome_arquivo_carregado = uploaded_file.name
        st.session_state.df_original = carregar_dados(uploaded_file)
        st.session_state.df_limpo = None  # Reseta o df_limpo
        st.session_state.limpeza_foi_aplicada = False # Reseta a flag de limpeza

    if st.session_state.df_original is not None:
        df_original_para_usar = st.session_state.df_original # Pega da sessão

        st.header("Análise Inicial")
        mostrar_analise(analisar_sujeira(df_original_para_usar))

        st.header("🧹 Opções de Limpeza")
        if st.button("✨ Aplicar Limpeza Básica! ✨", type="primary"):
            with st.spinner('Aplicando faxina... Aguarde!'):
                st.session_state.df_limpo = limpar_dados_basicos(df_original_para_usar) # Usa o original da sessão
            st.session_state.limpeza_foi_aplicada = True # SINALIZA que a limpeza ocorreu
            st.success("Limpeza básica aplicada com sucesso!")
            # Força um rerun para garantir que a interface se atualize corretamente com df_limpo
            st.rerun()


        # Só mostra essa parte se a limpeza JÁ FOI APLICADA
        if st.session_state.get('limpeza_foi_aplicada', False) and st.session_state.df_limpo is not None:
            df_para_exibir_e_analisar = st.session_state.df_limpo # Pega o limpo da sessão

            st.header("🧼 Análise Pós-Limpeza")
            mostrar_analise(analisar_sujeira(df_para_exibir_e_analisar))

            st.header("📊 Resumos e Gráficos")
            # Adicionar uma 'key' única para o selectbox é uma boa prática
            col_grupo = st.selectbox(
                "Escolha uma coluna para agrupar:",
                df_para_exibir_e_analisar.columns,
                key=f"selectbox_col_grupo_{st.session_state.nome_arquivo_carregado}" # Key única por arquivo
            )

            if col_grupo:
                resumo = gerar_resumo(df_para_exibir_e_analisar, col_grupo)
                if resumo is not None:
                    st.write(f"Resumo por '{col_grupo}':")
                    st.dataframe(resumo)

                    st.write(f"Gráfico por '{col_grupo}' (Top 10):")
                    try:
                        fig, ax = plt.subplots(figsize=(10, 6))
                        resumo.head(10).set_index(col_grupo)['Contagem'].plot(kind='barh', ax=ax, title=f'Top 10 {col_grupo}')
                        ax.set_xlabel("Contagem")
                        ax.set_ylabel(col_grupo)
                        plt.tight_layout()
                        st.pyplot(fig)
                    except Exception as e:
                        st.warning(f"Não foi possível gerar o gráfico para '{col_grupo}': {e}")
            
            # Botão de Download
            st.header("💾 Baixar Dados Limpos")
            # Usa o nome do arquivo original para o nome do arquivo limpo
            nome_base_arquivo = Path(st.session_state.nome_arquivo_carregado).stem
            csv_limpo = df_para_exibir_e_analisar.to_csv(index=False, sep=';').encode('utf-8')
            st.download_button(
                label="Baixar CSV Limpo",
                data=csv_limpo,
                file_name=f"{nome_base_arquivo}_limpo.csv",
                mime='text/csv',
            )

        elif st.session_state.df_original is not None and not st.session_state.get('limpeza_foi_aplicada', False):
            st.info("Clique no botão '✨ Aplicar Limpeza Básica! ✨' para processar os dados e ver mais opções.")

    else:
        st.error("Não foi possível ler o DataFrame do arquivo. Verifique o formato ou o conteúdo.")
else:
    st.info("Aguardando o upload de um arquivo na barra lateral...")