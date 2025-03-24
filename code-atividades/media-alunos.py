#Crie um programa que calcule a média aritmética de 8 notas de alunos.

soma = 0
n1 = float(input('Nota Aluno 1:'))
soma = soma +n1

n2 = float(input('Nota Aluno 2:'))
soma = soma +n2

n3 = float(input('Nota Aluno 3:'))
soma = soma +n3

n4 = float(input('Nota Aluno 4:'))
soma = soma +n4

n5 = float(input('Nota Aluno 5:'))
soma = soma +n5

n6 = float(input('Nota Aluno 6:'))
soma = soma +n6

n7 = float(input('Nota Aluno 7:'))
soma = soma +n7

n8 = float(input('Nota Aluno 8:'))
soma = soma +n8

media = soma + 8
media = soma/8
print('A media da turma foi {}'.format(round(media)))