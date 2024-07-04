# Catálogo de Filmes
catalogo = {}  # Define um dicionário vazio para armazenar os filmes

def adicionar_filme(titulo, diretor, ano, genero):
    # Função para adicionar um filme ao catálogo
    if titulo in catalogo:
        # Verifica se o filme já existe no catálogo
        print(f"Erro: O filme '{titulo}' já existe no catálogo.")
    else:
        # Adiciona o filme ao catálogo se não existir
        catalogo[titulo] = {
            'diretor': diretor,
            'ano': ano,
            'genero': genero
        }
        print(f"Filme '{titulo}' adicionado com sucesso.")

def atualizar_filme(titulo, diretor=None, ano=None, genero=None):
    # Função para atualizar as informações de um filme no catálogo
    if titulo in catalogo:
        # Verifica se o filme existe no catálogo
        if diretor:
            catalogo[titulo]['diretor'] = diretor
        if ano:
            catalogo[titulo]['ano'] = ano
        if genero:
            catalogo[titulo]['genero'] = genero
        print(f"Filme '{titulo}' atualizado com sucesso.")
    else:
        # Exibe uma mensagem de erro se o filme não existir no catálogo
        print(f"Erro: O filme '{titulo}' não existe no catálogo.")

def remover_filme(titulo):
    # Função para remover um filme do catálogo
    if titulo in catalogo:
        # Verifica se o filme existe no catálogo
        del catalogo[titulo]
        print(f"Filme '{titulo}' removido com sucesso.")
    else:
        # Exibe uma mensagem de erro se o filme não existir no catálogo
        print(f"Erro: O filme '{titulo}' não existe no catálogo.")

def visualizar_catalogo():
    # Função para visualizar todos os filmes no catálogo
    if catalogo:
        # Verifica se há filmes no catálogo
        print("\n----- Catálogo de Filmes -----")
        for titulo, info in catalogo.items():
            # Itera sobre cada filme e suas informações
            print(f"Título: {titulo}")
            print(f"  Diretor: {info['diretor']}")
            print(f"  Ano: {info['ano']}")
            print(f"  Gênero: {info['genero']}\n")
    else:
        # Exibe uma mensagem se o catálogo estiver vazio
        print("O catálogo está vazio.")

def menu():
    # Função principal que exibe o menu e gerencia a interação com o usuário
    while True:
        print("\n----- Catálogo de Filmes -----")
        print("1. Adicionar Filme")
        print("2. Atualizar Filme")
        print("3. Remover Filme")
        print("4. Visualizar Catálogo")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        # Solicita ao usuário que escolha uma opção

        if opcao == '1':
            # Adicionar filme
            titulo = input("Título do Filme: ").strip()
            if titulo:
                # Solicita as informações do filme
                diretor = input("Diretor: ").strip()
                ano = input("Ano de Lançamento: ").strip()
                genero = input("Gênero: ").strip()
                adicionar_filme(titulo, diretor, ano, genero)
            else:
                # Exibe uma mensagem de erro se o título for vazio
                print("Erro: O título do filme não pode ser vazio.")
        elif opcao == '2':
            # Atualizar filme
            titulo = input("Título do Filme: ").strip()
            if titulo in catalogo:
                # Solicita as novas informações do filme
                diretor = input("Novo Diretor (pressione enter para manter o atual): ").strip() or None
                ano = input("Novo Ano de Lançamento (pressione enter para manter o atual): ").strip() or None
                genero = input("Novo Gênero (pressione enter para manter o atual): ").strip() or None
                atualizar_filme(titulo, diretor, ano, genero)
            else:
                # Exibe uma mensagem de erro se o filme não existir no catálogo
                print(f"Erro: O filme '{titulo}' não existe no catálogo.")
        elif opcao == '3':
            # Remover filme
            titulo = input("Título do Filme: ").strip()
            remover_filme(titulo)
        elif opcao == '4':
            # Visualizar catálogo
            visualizar_catalogo()
        elif opcao == '5':
            # Sair do programa
            print("Saindo do programa...")
            break
        else:
            # Exibe uma mensagem de erro se a opção for inválida
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()