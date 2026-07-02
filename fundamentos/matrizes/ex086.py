matriz = [[0,0,0],[0,0,0],[0,0,0]]
calculo = soma_c = maior = 0
for l in range(0,3):
   for c in  range(0,3):
      matriz [l] [c] = int(input(f'Digite um valor para [{l},{c}]: '))
      if matriz [l] [c] % 2 == 0:
          calculo += matriz [l] [c]
      if c == 2:
         soma_c += matriz [l] [c]
for c in range(0,3):
   if c == 0:
      maior = matriz [1] [c]
   elif matriz [1] [c] > maior:
         maior = matriz [1] [c]
print('=='*25)
for l in range(0,3):
   for c in range(0,3):
      print(f'[{matriz[l][c]:^5}]',end='')
   print()
print('=='*25)
print(f'Soma dos valores pares: {calculo}')
print(f'Soma dos valores da terceira coluna: {soma_c}')
print(f'Maior valor da segunda linha: {maior}')
