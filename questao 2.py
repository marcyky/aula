import datetime
from datetime import time
nome = input('Digite seu nome: ')
idade = int(input ('Digite sua idade: '))

x = datetime.datetime.now() 

ano = x.year - idade

print ('{} nasceu no ano de {}'. format(nome, ano))