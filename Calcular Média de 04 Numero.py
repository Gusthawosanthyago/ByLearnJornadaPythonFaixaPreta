# Outra forma de Calcular media.

print("Escreva a nota do aluno para saber qual foi sua média. Assim sabera se foi aprovado ou reprovado!")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Definimos o que é verificar uma aprovação.
def verificar_aprovacao():
    media = calcular_media([nota1, nota2, nota3, nota4])

    if media >= 6:
      print("O aluno foi Aprovado!")
    else:
      print("O aluno foi Reprovado!")

# Definimos o que é Calcular Média.
def calcular_media(notas):
    quantidade = len(notas)

    soma = 0
    for nota in notas:
        soma = soma + nota

    media = soma / quantidade

    return media

# Chamamos (executamos) a função de verificar Aprovação.
verificar_aprovacao()
