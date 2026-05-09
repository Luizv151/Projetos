Alunos = []

def adicionar_aluno(Alunos):
    Nome = str (input ("Digite o nome do aluno "))
    Idade = int (input ("Digite a idade do aluno "))
    
    while True:
        Nota = float (input ("Digite a nota do aluno "))
        if Nota >= 0.0 and Nota <= 10.0:
            
            break
        else:
            print ("Nota invalida a nota deve ser de 0 a 10")
    dados = {
        'nome': Nome,
        'idade': Idade,
        'nota': Nota,
        }
    Alunos.append(dados)

def listar_alunos(Alunos):
    if len(Alunos) == 0:
        print ("\nNão á alunos cadastrados")
        return
    for Aluno in Alunos:
        print (f"\nNome do Aluno {Aluno['nome']}\n Idade do Aluno {Aluno['idade']}\n Nota do Aluno{Aluno['nota']}\n")
        

def buscar_aluno(nome_aluno):
    if len(Alunos) == 0:
        print ("\nNão á alunos cadastrados")
        return
    for Aluno in Alunos:
        if Aluno['nome'].lower() == nome_aluno.lower():
            print (f"\nAluno encontrado\n Nome: {Aluno['nome']}\n Idade: {Aluno['idade']}\n Nota: {Aluno['nota']}")
            break
        else:
            print ("\nAluno não cadastrado")


def remover_aluno(nome_aluno):
    if len(Alunos) == 0:
        print ("\nNão á alunos cadastrados")
        return
    for Aluno in Alunos:
        if Aluno['nome'].lower() == nome_aluno.lower():
            Alunos.remove(Aluno)
            print (f"Aluno: {nome_aluno} removido com sucesso")
            break
        else:
            print ("Aluno não encontrado")


def media_geral(Alunos):
    if len(Alunos) == 0:
        print ("\nNão á alunos cadastrados")
        return
    soma = 0
    for Aluno in Alunos:
        soma += Aluno['nota']
    media = soma / len(Aluno)
    print (f"\nA Media de todas as notas é igual a {media:.2f}")









while True:
        opção = int (input ("\nBem vindo ao site de cadastros Oque deseja fazer?\n1.Adicionar Aluno\n2.Listar Todos os Alunos\n3.Buscar Aluno Pelo Nome\n4.Remover Aluno\n5.Mostrar Medias Geral\n6.Sair\n"))

        match opção:
            case 1:
                adicionar_aluno(Alunos)
            case 2:
                listar_alunos(Alunos)
            case 3:
                nome_aluno = str (input ("Digite o nome do aluno "))
                buscar_aluno(nome_aluno)
            case 4:
                nome_aluno = str (input ("Digite o nome do aluno "))
                remover_aluno(nome_aluno)
            case 5:
                media_geral(Alunos)
            case 6:
                break
            case _:    
                print ("Opção invalida Você deve escolher entre 1 a 6")