"""
Tres amigos jogaram na loteria, caso eles ganharem, repatir o msm valor pros tres e o valor que cada um deu
para realizar a aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio e imprima quanto cada um ganharia do prêmio
com base no valor investido.
"""

Bruno = float(input('Quanto investiu o apostador Bruno (valor maior)? '))
Erick = float(input('Quanto investiu o apostador Erick (valor médio)? '))
Cassiano = float(input('Quanto investiu o apostador Cassiano (valor menor)? '))


total = Bruno + Erick + Cassiano
print(total)

print(total / 3)

print('Bruno Ganhou. ')

#  Ficou bem simples, a divisão por 3 foi pra ver o resultado final que o vencedor irá ganhar.
