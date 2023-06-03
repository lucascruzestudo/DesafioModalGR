# 1) A ModalGR possui um sistema em desenvolvimento que recebe dois vetores de 20 números
# inteiros. A partir desses valores armazenar em um terceiro vetor números que se repetem, por
# exemplo:
# Entradas: a = [1, 2, 3, ... ] e b = [4, 2, 4, ... ]
# Saída: [2]

def set_vetor():
    vetor = []
    for i in range(20):
        while True:
            try:
                num = int(input(f"Digite o valor {i+1}: "))
                vetor.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")
    return vetor

def separar_repetidos(vetor_a, vetor_b):
    vetor_separado = []
    for num in vetor_a:
        if num in vetor_b and num not in vetor_separado:
            vetor_separado.append(num)
    return vetor_separado

# Se necessário informar valores utilize a função set_vetor()
# vetor_a = set_vetor()
# vetor_b = set_vetor()

vetor_a = [1, 2, 3, 7, 186, 9, 6, 44, 2, 1,
           18, 26, 23, 73, 21, 64, 123, 83, 12, 52]
vetor_b = [4, 2, 4, 33, 81, 123, 7, 23, 1, 79,
           45, 93, 124, 93, 12, 64, 71, 23, 17, 94]

vetor_separado = separar_repetidos(vetor_a, vetor_b)

print('Valores repetidos entre os vetores: ', vetor_separado)
