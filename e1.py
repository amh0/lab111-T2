# 1. Ingrese un tiempo X que estará representado en segundos, 
# luego ingrese el tiempo que tomará en realizarse una tarea Z
# representado en segundos, minutos y horas. Se pide verificar
# si con el tiempo X se puede finalizar la tarea Z

tiempo = int(input('Ingrese tiempo disponible en segundos: '))
print('Ingrese tiempo de la tarea')
tareaSeg = int(input('Segundos: '))
tareaMin = int(input('Minutos: '))
tareaHrs = int(input('Horas : '))

tareaTiempo = (tareaHrs * 3600) + (tareaMin * 60) + tareaSeg
calc = tiempo / tareaTiempo

if calc >= 1 :
    print('Si se puede realizar la tarea.')
else :
    print('No se puede realizar la tarea.')

# Hagi Argani Mamani  
