from random import randint
from time import sleep
print('-='*30)
print(f'{"MEGA SENA":^60}')
print('-='*30)
games_list = []
quant = int(input('Quantos Jogos deseja  sortear? '))
for l in range(quant):
    numbers = []
    while len(numbers) < 6:
        num = randint(1, 60)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    games_list.append(numbers)
print(f'-=-=Sorteando {quant} jogos-=-=')
for indice,jogo in enumerate(games_list, start = 1):
    print(f'Jogo {indice}: {jogo}')
    sleep(0.5)
print('**'*4 ,'BOA SORTE!','**'*4)