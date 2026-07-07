from time import sleep
students = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)
    students.append(dados[:])
    dados.clear()
    resp = '-'
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*45)
print(f'{"No.":<5} {"Nome:":<10} {"Média:":>8}')
print('--'*20)
for i,aluno in enumerate(students, start = 1):
    print(f'{i:<5} {aluno[0]:<10} {aluno[3]:>8.1f}')
print('--'*25)
while True:
    show = int(input('Quer ver as notas de qual aluno? (999 para parar): '))
    while (show <1 or show > len(students)) and show != 999:
        show = int(input('Opção inválida! Quer ver as notas de qual aluno? (999 para parar): '))
    if show == 999:
        break
    print('=='*25)
    print(f'As notas de {students[show-1][0]} são {students [show-1][1]} e {students [show-1][2]}' )
    print('=='*25)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('FINALIZADO')