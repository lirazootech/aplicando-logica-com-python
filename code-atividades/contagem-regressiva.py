#Estruturas de Repetições
#Atividades de fixação
#Desenvolva um programa que faça uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Resolução do desafio acima:

import time # Vamos importar o módulo time para usar a função sleep,
for i in range(10, -1, -1): # Começa em 10, vai até 0 decrementando de 1 em 1;
    print(i)
    time.sleep(1) # Pausa de 1 segundo entre os números;
print('🎆 Feliz Ano Novo! 🎆') # Mensagem ao final da contagem;