import datetime
from datetime import time
idade = int(input('Digite sua idade: '))

dias = 365 * idade
horas = dias * 24

print ('Você já viveu {} dias. Isso significa {} horas'. format(dias, horas))