import mysql.connector
from mysql.connector import Error

def criar_tabela():
    try:
        # Conectar ao banco de dados com as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Criar um cursor para executar comandos no banco de dados
            cursor = conexao.cursor()

            # Comando SQL para criar uma tabela, se ela não existir
            criar_tabela_sql = """
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,  # ID será gerado automaticamente
                nome VARCHAR(255),                  # Nome do produto (texto)
                preco DECIMAL(10, 2),               # Preço do produto (número com duas casas decimais)
                quantidade INT                      # Quantidade do produto (número inteiro)
            )
            """

            # Executa o comando SQL para criar a tabela
            cursor.execute(criar_tabela_sql)
            print('Tabela criada com sucesso')

    except Error as e:
        # Se houver um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor
            conexao.close()  # Fecha a conexão com o banco de dados
            print('Conexão encerrada')

def inserir_produto(nome, preco, quantidade):
    try:
        # Conectar ao banco de dados com as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Criar um cursor para executar comandos no banco de dados
            cursor = conexao.cursor()

            # Comando SQL para inserir dados na tabela
            inserir_sql = """
            INSERT INTO produtos (nome, preco, quantidade)
            VALUES (%s, %s, %s)
            """

            # Dados a serem inseridos na tabela
            dados = (nome, preco, quantidade)

            # Executa o comando SQL para inserir os dados
            cursor.execute(inserir_sql, dados)

            # Confirma a inserção dos dados no banco de dados
            conexao.commit()

            print('Produto inserido com sucesso')

    except Error as e:
        # Se houver um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor
            conexao.close()  # Fecha a conexão com o banco de dados
            print('Conexão encerrada')

# Exemplo de uso
# Primeiro, cria a tabela (execute isso apenas uma vez)
criar_tabela()

# Em seguida, insere um produto na tabela
nome_produto = input("Digite o nome do produto: ")          # Pergunta o nome do produto
preco_produto = float(input("Digite o preço do produto: "))  # Pergunta o preço do produto
quantidade_produto = int(input("Digite a quantidade do produto: "))  # Pergunta a quantidade do produto
inserir_produto(nome_produto, preco_produto, quantidade_produto)  # Insere o produto na tabela
