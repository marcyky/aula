matricula = int(input('Digite sua matrícula: '))
av1 = float(input('Digite sua nota AV1: '))
av2 = float(input('Digite sua nota AV2: '))

media = (av1 + av2) / 2

print ('Sua media é {}'. format(media))

if (media < 6):
    print ('Você precisa fazer a AV3')

elif (media >= 6):
    print ('Você já passou, não precisa fazer a AV3')