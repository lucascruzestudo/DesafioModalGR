from datetime import datetime, date


def cadastrar_colaborador():
    colaborador = {}

    colaborador['nome'] = input("Digite seu nome: ")

    while True:
        admissao_input = input("Informe sua data de admissão (dd/mm/aaaa): ")

        try:
            admissao = datetime.strptime(admissao_input, "%d/%m/%Y").date()
            diferenca_dias = (date.today() - admissao).days
            if diferenca_dias < (365 * 5):
                print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
                exit(1)
            else:
                colaborador['admissao'] = admissao
                break
        except ValueError:
            print("Insira uma data válida! Utilize o formato dd/mm/aaaa.")

    while True:
        try:
            salario = int(input("Informe seu salário atual: "))
            colaborador['salario'] = salario
            break
        except ValueError:
            print("Insira um valor válido!")

    while True:
        try:
            emprestimo = int(input("Informe o valor do empréstimo: "))
            if (emprestimo <= (salario * 2)) and (emprestimo % 2 == 0):
                colaborador['emprestimo'] = emprestimo
                break
            else:
                print("Insira um valor válido!")
        except ValueError:
            print("Insira um valor válido!")

    return colaborador


def calcular_notas(emprestimo, notas):
    resultado_notas = []

    for nota in notas:
        quantidade = emprestimo // nota
        emprestimo %= nota

        if quantidade > 0:
            resultado_notas.append(f"{quantidade} x {nota} reais")

    return resultado_notas


def chamar_menu(emprestimo):
    while True:
        print("\nMENU")
        print("Escolha como deseja tirar o valor do empréstimo\n")
        print("1. Notas de maior valor")
        print("2. Notas de menor valor")
        print("3. Notas meio a meio")

        while True:
            try:
                opcao = int(input("\nEscolha uma opção: "))
                if 1 <= opcao <= 3:
                    print('\n')
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Opção inválida!")

        if opcao == 1:
            resultado = calcular_notas(emprestimo, [100, 50, 20, 10, 5, 2])
            print('Notas de maior valor: ')
            for nota in resultado:
                print(nota)
            break

        elif opcao == 2:
            resultado = calcular_notas(emprestimo, [20, 10, 5, 2])
            print('Notas de menor valor: ')
            for nota in resultado:
                print(nota)
            break

        elif opcao == 3:
            resultado_a = calcular_notas(int(emprestimo / 2), [100, 50, 20, 10, 5, 2])
            resultado_b = calcular_notas(int(emprestimo / 2), [20, 10, 5, 2])

            print(f'{int(emprestimo / 2)} reais em notas de maior valor:')
            for nota in resultado_a:
                print(nota)
            print('\n')

            print(f'{int(emprestimo / 2)} reais em notas de menor valor:')
            for nota in resultado_b:
                print(nota)
            print('\n')
            break


colaborador = cadastrar_colaborador()
chamar_menu(colaborador["emprestimo"])
