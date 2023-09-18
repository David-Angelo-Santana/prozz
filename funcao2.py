def calculadora():
  

  operações = {
    1: "Soma",
    2: "Subtração",
    3: "Multiplicação",
    4: "Divisão",
  }

  
  while True:
   

    print("Escolha uma operação:")
    for opcao, descricao in operações.items():
      print(f"{opcao}: {descricao}")

    

    try:
      opcao = int(input())
    except ValueError:
      print("Essa opção não existe")
      continue

   

    if opcao in operações:
    

      primeiro_valor = float(input("Digite o primeiro valor: "))
      segundo_valor = float(input("Digite o segundo valor: "))

     

      resultado = None
      if opcao == 1:
        resultado = primeiro_valor + segundo_valor
      elif opcao == 2:
        resultado = primeiro_valor - segundo_valor
      elif opcao == 3:
        resultado = primeiro_valor * segundo_valor
      elif opcao == 4:
        resultado = primeiro_valor / segundo_valor

      

      print(f"O resultado é {resultado}")

   
    if opcao == 0:
      break


if __name__ == "__main__":
  calculadora()
