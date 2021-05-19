# Listas de Animais

animais = []

animal = input("Digite o nome do seu animal de estimação ou digite 0 se não tiver nenhum: ")

while animal != "0":
      especie = input("Digite a espécie desse animal: ")
      animais.append([animal, especie])
      animal = input("Se tiver mais animais, digite o nome dele. Ou digite 0 se não tiver: ")

if len(animais) == 0:
    print("\n\nVocê tem os seguintes animais: ")
    for animal in animais:
        print("-Nome:", animal[0], "| espécie:", animal[1])
