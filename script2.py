# A ModalGR possui um sistema em desenvolvimento sobre notas musicais, no qual cada uma
# das 7 notas possui um grau representado por um algarismo romano conforme abaixo:
# A ideia é receber um vetor de notas e retornar um outro vetor com os respectivos graus da
# escala, por exemplo:
# Entrada: ['Ré', 'Sol', 'Dó']
# Saída: ['II', 'V', 'I']
# Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução!
# Após a finalização exibir em tela a saída de acordo com a entrada das notas musicais.

mapeamento_notas = {
    "Dó": "I",
    "Ré": "II",
    "Mi": "III",
    "Fá": "IV",
    "Sol": "V",
    "Lá": "VI",
    "Si": "VII"
}


def obter_notas():
    notas = []
    while True:
        nota = input("Digite uma das notas (Dó, Ré, Mi, Fá, Sol, Lá, Si) ou digite 0 para parar: ")

        if nota == "0":
            break

        if nota in mapeamento_notas:
            notas.append(nota)
        else:
            print("Nota não encontrada no mapeamento.")
    return notas


def converter_notas(notas):
    notas_convertidas = []
    for nota in notas:
        if nota in mapeamento_notas:
            nota_convertida = mapeamento_notas[nota]
            notas_convertidas.append(nota_convertida)
    return notas_convertidas


notas_brutas = obter_notas()
notas_convertidas = converter_notas(notas_brutas)
print("Respectivos graus da escala:", notas_convertidas)

