# 3. Dados 3 valores (horas, minutos y segundos) 
# se pide sumar un segundo.

horas = int(input('Ingrese horas: '))
minutos = int(input('Ingrese minutos: '))
segundos = int(input('Ingrese segundos: '))

segundos = segundos + 1

if segundos > 59:
    minutos = minutos + 1
    segundos = 0
    if minutos > 59:
        horas = horas + 1
        minutos = 0
        
print('Tiempo: ',horas,'h:',minutos,'m:',segundos,'s')

# Hagi Argani Mamani
