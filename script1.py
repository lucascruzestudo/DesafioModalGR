# 1) A ModalGR possui um sistema em desenvolvimento que recebe dois vetores de 20 números
# inteiros. A partir desses valores armazenar em um terceiro vetor números que se repetem, por
# exemplo:
# Entradas: a = [1, 2, 3, ... ] e b = [4, 2, 4, ... ]
# Saída: [2]

vetor_a = [1, 2, 3, 7, 186, 9, 6, 44, 2, 1, 18, 26, 23, 73, 21, 64, 123, 83, 12, 52]
vetor_b = [4, 2, 4, 33, 81, 123, 7, 23, 1, 79, 45, 93, 124, 93, 12, 64, 71, 23, 17, 94]
vetor_final = []

for num in vetor_a:
    if num in vetor_b and num not in vetor_final:
        vetor_final.append(num)

print('Valores repetidos entre os vetores: ',vetor_final)