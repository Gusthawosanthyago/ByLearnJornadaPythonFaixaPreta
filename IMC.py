# IMC => Peso (KG) / Altura (M)²

def numero_quadrado(numero):
  quadrado = numero * numero
  
  return quadrado

def calcular_imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)

  imc = peso / altura_quadrada

  return imc

def classificar(imc):
  if imc < 18.5:
    print("Magreza!")
    
  elif imc >= 18.5 and imc < 25:
    print("Normal!")
    
  elif imc >= 25 and imc < 30:
    print("Sobrepeso!")

  elif imc >= 30 and imc < 40:
    print("Obesidade!")
  elif imc > 40:
    print("Obesidade Grave!")

peso = float(input("Insira seu peso (Kg): "))
altura = float(input("Insira sua altura (M) "))

meu_imc = calcular_imc(peso, altura)

classificar(meu_imc)
