# 🃏 Ferramenta de Limpeza e Análise de Dados 

Bem-vindo à Ferramenta de Limpeza e Análise de Dados! Esta aplicação web interativa foi construída para ajudar você a carregar seus datasets (CSV ou Excel), identificar problemas comuns, aplicar uma limpeza básica e obter alguns insights rápidos, tudo isso com alguns cliques e um toque de caos organizado!

➡️ **Teste a Ferramenta Online Aqui:** https://projeto-limpeza.streamlit.app/

## 📖 Guia do Usuário: Como Usar a Ferramenta Web

Esta ferramenta foi projetada para ser intuitiva. Siga os passos abaixo para limpar e analisar seus dados:

### Passo 1: Carregue Seu Arquivo
* Na barra lateral à esquerda, você encontrará a seção "1. Carregar Dados".
* Clique no botão "Escolha seu arquivo:" e selecione um arquivo `.csv` ou `.xlsx` do seu computador.
* Formatos aceitos: CSV (separado por vírgula ou ponto e vírgula) e Excel (.xlsx, .xls).

### Passo 2: Diagnóstico Inicial
* Assim que o arquivo for carregado com sucesso, a aplicação exibirá uma "Análise Inicial".
* Você verá:
    * O formato do seu dataset (número de linhas e colunas).
    * O total de células vazias (NaNs) e o número de linhas duplicadas.
    * Uma tabela detalhando a contagem de células vazias por coluna.
    * As primeiras linhas do seu DataFrame original para uma rápida inspeção visual (desmarque a caixa de seleção "Mostrar DataFrame Original Completo" para ver a tabela inteira).

### Passo 3: Invoque a Limpeza Mágica!
* Abaixo da análise inicial, você encontrará a seção "Opções de Limpeza".
* Clique no botão "✨ Aplicar Limpeza Básica! ✨".
* A ferramenta aplicará automaticamente as seguintes ações:
    * Removerá a coluna "Unnamed: 0", se existir (um resquício comum de índices salvos).
    * Preencherá valores numéricos ausentes com a **mediana** da respectiva coluna.
    * Preencherá valores de texto (objeto) ausentes com a string **"Unknown"**.
    * Removerá quaisquer linhas que sejam **exatamente duplicadas**.
* Aguarde a mensagem de sucesso!

### Passo 4: Contemple a Ordem Pós-Limpeza
* Após a limpeza, uma nova seção "Análise Pós-Limpeza" aparecerá.
* Ela mostrará as mesmas métricas da análise inicial, mas agora para o seu DataFrame limpo. Idealmente, você verá "0" para NaNs Totais e Duplicatas.
* Você também pode visualizar o DataFrame limpo (completo ou as primeiras linhas usando a caixa de seleção).

### Passo 5: Extraia Insights com Resumos e Gráficos
* Na seção "Resumos e Gráficos":
    * Use a caixa de seleção "Escolha uma coluna para agrupar:" para selecionar uma coluna do seu dataset limpo.
    * A ferramenta gerará automaticamente uma tabela resumindo a contagem de ocorrências para cada valor único na coluna escolhida.
    * Um gráfico de barras horizontais mostrando o Top 10 dessas contagens também será exibido.

### Passo 6: Leve Seus Tesouros Limpos!
* Na seção "Baixar Dados Limpos":
    * Você terá botões para baixar seu DataFrame agora limpo nos formatos `.csv` (separado por ponto e vírgula) ou `.xlsx` (Excel).
    * Os arquivos terão "_limpo" adicionado ao nome original.

---

## 👨‍💻 Para Desenvolvedores: Rodando o Projeto Localmente

Se você deseja explorar o código, modificá-lo ou rodá-lo no seu próprio ambiente:

### Visão Geral Técnica
Esta aplicação é construída em Python, utilizando principalmente as bibliotecas Pandas para manipulação de dados e Streamlit para a interface web interativa. Matplotlib é usado nos bastidores pelo Pandas para a geração de gráficos.

### Pré-requisitos
* Python 3.7 ou superior.
* pip (gerenciador de pacotes Python).

### Configuração do Ambiente
1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    git clone https://github.com/LucaDevel0per/limpeza-de-dados.git
    cd limpeza_dados
    ```
2.  **(Recomendado) Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows: venv\Scripts\activate
    # No macOS/Linux: source venv/bin/activate
    ```
3.  **Instale as dependências:**
    Navegue até a pasta raiz do projeto (onde o arquivo `requirements.txt` está localizado) e execute:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Aplicativo
1.  Navegue no terminal até a pasta raiz do projeto.
2.  Execute o comando:
    ```bash
    streamlit run src/app.py
    ```
3.  O aplicativo deverá abrir automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

---

## ✨ Funcionalidades Implementadas
* Upload de arquivos `.csv` (com separadores `,` ou `;`) e `.xlsx`.
* Análise detalhada de valores ausentes (NaNs) e linhas duplicadas.
* Limpeza automatizada:
    * Remoção da coluna "Unnamed: 0".
    * Imputação de NaNs numéricos pela mediana.
    * Imputação de NaNs textuais por "Unknown".
    * Remoção de linhas duplicadas.
* Visualização interativa dos DataFrames (original e limpo).
* Geração de resumos agrupados por coluna selecionada pelo usuário.
* Geração de gráfico de barras para os resumos.
* Download dos dados limpos em formatos `.csv` e `.xlsx`.

## 🛠️ Tecnologias Utilizadas
* Python
* Pandas
* Streamlit
* Matplotlib

## 📂 Estrutura do Projeto
```bash
seu_projeto_limpeza/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/      # Dados brutos originais para teste
│   └── processed/ # Onde os dados limpos do app são salvos (opcional)
└── src/
├── init.py
├── app.py      # Script principal do Streamlit
└── core/
├── init.py
├── data_analyzer.py
├── data_cleaner.py
└── data_loader.py
```

## 💡 Melhorias Futuras 

Este projeto é uma base sólida, mas sempre pode evoluir! Algumas ideias para expandir e aprimorar esta ferramenta no futuro incluem:

* **Limpeza de Dados Mais Interativa e Granular:**
    * Permitir que o usuário escolha a **estratégia de imputação para `NaN`s por coluna** (ex: média, mediana, moda, valor específico, ou até mesmo não preencher).
    * Opção para o usuário **selecionar manualmente colunas para remover**.
    * Ferramentas básicas de **limpeza de texto** (converter para minúsculas/maiúsculas, remover espaços extras, substituir texto).
    * Detecção e opções de tratamento para **outliers** em colunas numéricas.
    * Conversão de tipos de dados mais inteligente e com feedback para o usuário.

* **Análises e Resumos Mais Avançados:**
    * Permitir **múltiplas agregações** no `groupby` diretamente pela interface (ex: contar e somar uma coluna ao mesmo tempo).
    * Cálculo e exibição de uma **matriz de correlação** para colunas numéricas.
    * Opções para **transformação de variáveis** (ex: log, normalização).

* **Visualizações Mais Ricas e Interativas:**
    * Adicionar mais tipos de gráficos (histogramas, gráficos de dispersão, box plots), permitindo ao usuário selecionar as colunas.
    * Integrar bibliotecas como **Plotly Express** ou **Altair** para gráficos mais interativos e com mais opções de customização.

* **Melhorias na Experiência do Usuário (UX):**
    * Implementar um sistema para **salvar e carregar "perfis de limpeza"** ou "receitas" de transformações para serem aplicadas a datasets semelhantes.
    * Um **histórico ou log** mais detalhado das transformações aplicadas ao dataset.
    * Suporte a **arrastar e soltar (drag and drop)** para o upload de arquivos.
    * Opções de **temas visuais** para o app.

* **Expansão das Fontes de Dados:**
    * Permitir a conexão com **bancos de dados simples** (como SQLite) para carregar dados.
    * Carregar dados a partir de **URLs**.

*Sinta-se à vontade para abrir uma "issue" no GitHub com novas ideias ou até mesmo enviar um "pull request" com sua própria ideia!*


## 👤 Autor
Desenvolvido com um toque de loucura organizada por **LucaDevel0per** 🃏

➡️ **Meu GitHub:** https://github.com/LucaDevel0per

---

![Coringa da Programação](assets/img/coringa_do_pandas-certo.png)