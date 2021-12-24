"""
Tres amigos jogaram na loteria, caso eles ganharem, repatir o msm valor pros tres e o valor que cada um deu
para realizar a aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio e imprima quanto cada um ganharia do prêmio
com base no valor investido.
"""
total = 1000000

Bruno = float(input('Quanto investiu o apostador Bruno (valor maior)? '))
Erick = float(input('Quanto investiu o apostador Erick (valor médio)? '))
Cassiano = float(input('Quanto investiu o apostador Cassiano (valor menor)? '))


print(Bruno + Erick + Cassiano)


print('Bruno tem {} % do total'.format((Bruno / total) * 100))
print('Erick tem {} % do total'.format((Erick / total) * 100))
print('Cassiano tem {} % do total'.format((Erick / total) * 100))

premio = float(input('Quanto foi o prêmio da loteria?\n'))

print('Bruno tem {} % do premio'.format((Bruno / total) * premio))
print('Erick tem {} % do premio'.format((Erick / total) * premio))
print('Cassiano tem {} % do premio'.format((Cassiano / total) * premio))

resultado_Bruno = Bruno / total * premio
resultado_Erick = Erick / total * premio
resultado_Cassiano = Cassiano / total * premio

print('Resultado Bruno {}'.format((Bruno / total) * premio))
print('Resultado Erick {}'.format((Erick / total) * premio))
print('Resultado Cassiano {}'.format((Cassiano / total) * premio))
