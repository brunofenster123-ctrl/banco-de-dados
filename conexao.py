import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        # Configura os dados para abrir a comunicação com o banco
        conexao = mysql.connector.connect(
            host="localhost",          # Indica que o banco está no seu PC
            user="root",               # Usuário padrão do MySQL
            password="Bru1919@", # <-- APAGUE ISSO E COLOQUE A SUA SENHA DO MYSQL
            database="LOJA"            # Nome do banco de dados da lousa
        )
        
        if conexao.is_connected():
            print("\n=========================================")
            print("✨ SUCESSO: Conectado ao banco 'LOJA'!")
            print("=========================================")
            return conexao

    except Error as erro:
        print("\n=========================================")
        print("❌ ERRO: Falha na conexão.")
        print(f"Detalhe do erro: {erro}")
        print("=========================================")
        return None

# Executa o teste de conexão
if True:
    minha_conexao = conectar_banco()
    
    if minha_conexao:
        minha_conexao.close()
        print("🔌 Conexão fechada com segurança.")