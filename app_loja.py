import pandas as pd
import mysql.connector
import streamlit as st

# Configuração inicial do Front-end
st.set_page_config(page_title="Exercício Loja", page_icon="🏬", layout="centered")

st.title("🏬 Exercício Banco: LOJA")
st.markdown("---")
st.subheader("dominios&Ballak)")

st.markdown("""
    <style>
        /* 1. Muda o fundo de toda a tela para um degradê moderno */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
        }
        
        /* 2. Deixa as tabelas brancas, com bordas arredondadas e sombra */
        .stDataFrame, table, [data-testid="stTable"] {
            background-color: white !important;
            border-radius: 12px !important;
            box-shadow: 0 8px 16px rgba(0,0,0,0.08) !important;
            padding: 15px !important;
        }

        /* 3. Melhora a cor e fonte dos títulos e textos */
        h1, h2, h3, span, p {
            color: #2c3e50 !important;
            font-family: 'Segoe UI', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SUA FUNÇÃO DE CONEXÃO ORIGINAL ---
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bru1919@",  # Sua senha mantida aqui
            database="LOJA",
        )
        return conexao
    except mysql.connector.Error as erro:
        st.error(f"Erro ao conectar ao banco de dados: {erro}")
        return None


# --- FUNÇÃO PARA BUSCAR E COMBINAR OS DADOS ---
def carregar_dados():
    conexao = conectar_banco()

    if conexao is None:
        return None

    # Passo 4 do quadro: Query com INNER JOIN juntando as duas tabelas
    query = """
    SELECT 
        c.COD AS 'Código Cliente',
        c.NOME AS 'Nome Cliente',
        c.CPF AS 'CPF Cliente',
        p.NOME AS 'Nome Produto'
    FROM CLI c
    INNER JOIN PROD p ON c.COD = p.CODCLI;
    """
    try:
        df = pd.read_sql(query, conexao)
        conexao.close()
        return df
    except Exception as e:
        st.error(f"Erro ao executar a consulta SQL: {e}")
        conexao.close()
        return None


# --- RENDERIZAÇÃO DO FRONT-END ---
dados_tabela = carregar_dados()

if dados_tabela is not None:
    st.success("✅ Conexão estabelecida e dados carregados do MySQL!")
    st.write("Dados da tabela combinados via SQL:")

    # Passo 3: Mostra o Front-end visual com os dados na tela
    st.dataframe(dados_tabela, use_container_width=True, hide_index=True)
else:
    st.warning(
        "Não foi possível exibir os dados. Verifique se as tabelas TAB_PROD e TAB_CLI existem no seu banco."
    )