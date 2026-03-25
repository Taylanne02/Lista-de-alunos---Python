import funcao

dados = {}
cont = 1

while True:
    print("Opções:")
    print("1 - Cadastrar aluno")
    print("2 - Listar nomes")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    
    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        g1 = int(input("Digite a nota da G1 do aluno: "))
        g2 = int(input("Digite a nota da G2 do aluno: "))

        dados[cont] = {
                'Nome': nome.strip(),
                'G1': g1,
                'G2': g2
            }

        cont += 1

        funcao.salvarDados('notas.txt', dados)
    
    elif opcao == 2:
        notas = funcao.lerNotas('notas.txt')
        if notas:
            for nota in notas:
                print(nota)
        else:
            print("Nenhum dado encontrado!")
        
    
    elif opcao == 3:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida, escolha uma das opções válidas!")

