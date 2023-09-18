def calcular_idade():
 

  ano_atual = 2022

  

  nome = input("Digite seu nome completo: ")

 

  while True:
    try:
      ano_nascimento = int(input("Digite seu ano de nascimento: "))
    except ValueError:
      print("Ano de nascimento inválido.")
      continue

    

    if ano_nascimento < 1922 or ano_nascimento > 2021:
      print("Ano de nascimento inválido.")
      continue

    break

  

  idade = ano_atual - ano_nascimento

  

  print(f"Olá, {nome}! Sua idade é de {idade} anos.")


if __name__ == "__main__":
  calcular_idade()
