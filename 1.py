Cadastros = []

def cadastrar(Cadastros):
    usuario = input("Digite seu nome de usuario! ")
    senha = input("Digite sua senha ")
    for cadastro in Cadastros:
        if cadastro['usuario'] == usuario:
            print("Usuário já cadastrado!")
            return
    
    dados = {'usuario': usuario, 'senha': senha}
    Cadastros.append(dados)

def entrar():
    if len(Cadastros) == 0:
        print(f"\nNão há usuários cadastrados\n{'='*50}")
        return
    Usuario = input("Digite seu nome de usuario ")
    Senha = input("Digite sua senha ")
    login_valido = False
    for cadastro in Cadastros:
        if cadastro['usuario'] == Usuario and cadastro['senha'] == Senha:
            print(f"Seja bem vindo {Usuario}")
            login_valido = True
            break
    if not login_valido:
        print(f"\nA sua senha ou seu nome de usuário estão incorretos. Tente novamente\n{'='*50}")

while True:
    try:
        opções = int(input("\nSeja bem vindo ao site teste\n1.Entrar\n2.Cadastrar\n3.Sair\n"))
        match opções:
            case 1:
                entrar()
            case 2:
                cadastrar(Cadastros)
            case 3:
                break
    except ValueError:
        print("Opção inválida. Digite um número de 1 a 3.")