import mysql.connector
from mysql.connector import Error

# Função para criar a tabela 'produtos' no banco de dados
def criar_tabela():
    try:
        # Conecta ao banco de dados usando as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Cria um cursor, que é como uma ferramenta para enviar comandos SQL ao banco de dados
            cursor = conexao.cursor()

            # Comando SQL para criar uma tabela chamada 'produtos', se ela ainda não existir
            criar_tabela_sql = """
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,  # 'id' é um número que aumenta automaticamente e é a chave principal
                nome VARCHAR(255),                  # 'nome' é um texto de até 255 caracteres
                preco DECIMAL(10, 2),               # 'preço' é um número com até 10 dígitos no total e 2 casas decimais
                quantidade INT                      # 'quantidade' é um número inteiro
            )
            """

            # Executa o comando SQL para criar a tabela
            cursor.execute(criar_tabela_sql)
            print('Tabela criada com sucesso')

    except Error as e:
        # Se ocorrer um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor para liberar recursos
            conexao.close()  # Fecha a conexão com o banco de dados

# Função para inserir um novo produto na tabela 'produtos'
def inserir_produto(nome, preco, quantidade):
    try:
        # Conecta ao banco de dados usando as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Cria um cursor para enviar comandos SQL ao banco de dados
            cursor = conexao.cursor()

            # Comando SQL para adicionar um novo produto na tabela
            inserir_sql = """
            INSERT INTO produtos (nome, preco, quantidade)
            VALUES (%s, %s, %s)
            """

            # Dados do produto a serem inseridos
            dados = (nome, preco, quantidade)

            # Executa o comando SQL para inserir os dados na tabela
            cursor.execute(inserir_sql, dados)

            # Confirma a inserção dos dados no banco de dados
            conexao.commit()

            print('Produto inserido com sucesso')

    except Error as e:
        # Se ocorrer um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor para liberar recursos
            conexao.close()  # Fecha a conexão com o banco de dados

# Função para remover um produto da tabela pelo nome
def remover_produto(nome):
    try:
        # Conecta ao banco de dados usando as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Cria um cursor para enviar comandos SQL ao banco de dados
            cursor = conexao.cursor()

            # Comando SQL para remover um produto da tabela pelo nome
            remover_sql = """
            DELETE FROM produtos
            WHERE nome = %s
            """

            # Dados do produto a ser removido
            dados = (nome,)

            # Executa o comando SQL para remover o produto da tabela
            cursor.execute(remover_sql, dados)

            # Confirma a remoção dos dados no banco de dados
            conexao.commit()

            print('Produto removido com sucesso')

    except Error as e:
        # Se ocorrer um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor para liberar recursos
            conexao.close()  # Fecha a conexão com o banco de dados

# Função para exibir todos os produtos na tabela
def mostrar_produtos():
    try:
        # Conecta ao banco de dados usando as informações fornecidas
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor do banco de dados
            user='root',         # Nome de usuário do banco de dados
            password='escola',   # Senha do banco de dados
            database='loja'      # Nome do banco de dados
        )

        if conexao.is_connected():   # Verifica se a conexão foi bem-sucedida
            print('Conectado ao banco de dados')

            # Cria um cursor para enviar comandos SQL ao banco de dados
            cursor = conexao.cursor()

            # Comando SQL para selecionar todos os produtos da tabela
            selecionar_sql = """
            SELECT * FROM produtos
            """

            # Executa o comando SQL para selecionar todos os produtos
            cursor.execute(selecionar_sql)

            # Obtém todos os registros da consulta
            produtos = cursor.fetchall()

            # Verifica se há produtos e os exibe
            if produtos:
                print('Produtos disponíveis:')
                for produto in produtos:
                    # Exibe os detalhes de cada produto
                    print(f'ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}')
            else:
                print('Nenhum produto encontrado.')

    except Error as e:
        # Se ocorrer um erro, exibe a mensagem de erro
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():   # Verifica se a conexão está aberta
            cursor.close()  # Fecha o cursor para liberar recursos
            conexao.close()  # Fecha a conexão com o banco de dados

# Função que exibe o menu de opções para o usuário
def menu():
    while True:
        # Exibe as opções disponíveis para o usuário
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Mostrar todos os produtos")
        print("4. Sair")

        # Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            # Se o usuário escolher a opção 1, adiciona um produto
            nome_produto = input("Digite o nome do produto: ")  # Pergunta o nome do produto
            preco_produto = float(input("Digite o preço do produto: "))  # Pergunta o preço do produto
            quantidade_produto = int(input("Digite a quantidade do produto: "))  # Pergunta a quantidade do produto
            inserir_produto(nome_produto, preco_produto, quantidade_produto)  # Insere o produto na tabela
        elif opcao == '2':
            # Se o usuário escolher a opção 2, remove um produto
            nome_produto_remover = input("Digite o nome do produto a ser removido: ")  # Pergunta o nome do produto a ser removido
            remover_produto(nome_produto_remover)  # Remove o produto com o nome fornecido
        elif opcao == '3':
            # Se o usuário escolher a opção 3, mostra todos os produtos
            mostrar_produtos()  # Exibe todos os produtos da tabela
        elif opcao == '4':
            # Se o usuário escolher a opção 4, sai do programa
            print("Saindo...")
            break
        else:
            # Se o usuário escolher uma opção inválida, exibe uma mensagem de erro
            print("Opção inválida. Tente novamente.")

# Primeiro, cria a tabela (execute isso apenas uma vez)
criar_tabela()

# Exibe o menu para o usuário e garante que a mensagem de conexão encerrada seja exibida apenas ao sair do programa
try:
    menu()
finally:
    # Mensagem final que será exibida quando o usuário sair do programa
    print('Conexão encerrada')
