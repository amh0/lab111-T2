# 2. Utilizando los coeficientes (a, b, c) de una ecuación 
# de segundo grado se pide mostrar la naturaleza de sus raíces

print('Ecuacion cuadratica:\tax^2 + bx + c')
a = int(input('Ingrese el coeficiente "a": '))
b = int(input('Ingrese el coeficiente "b": '))
c = int(input('Ingrese el coeficiente "c": '))

raiz = b**2 - 4*a*c 

if raiz > 0 :
    print('Las raices son reales y diferentes.')
elif raiz < 0 :
    print('Las raices son complejas.')
else :
    print('Las raíces son reales e iguales.')

# Hagi Argani Mamani
