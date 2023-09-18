def calculadora(numero_1, numero_2, operacao):
 

  if operacao == 1:
    return numero_1 + numero_2
  elif operacao == 2:
    return numero_1 - numero_2
  elif operacao == 3:
    return numero_1 * numero_2
  elif operacao == 4:
    return numero_1 / numero_2
  else:
    return 0


print(calculadora(10, 2, 1))  # 12
print(calculadora(10, 2, 2))  # 8
print(calculadora(10, 2, 3))  # 20
print(calculadora(10, 2, 4))  # 5
print(calculadora(10, 2, 5))  # 0
