#!/usr/bin/env python3
# Programita para implementar el método de bisección

# Busca un cero de f en el intervalo [a,b]
# tol= tolerancia prescripta para detener el método numérico
# (si no sería un ciclo infinito)

# Hipótesis: las del teorema de Bolzano
# f(a) y f(b) deben tener signos opuestos
# f debe ser continua en [a,b]

# Usamos una llamada recursiva por motivos didácticos.
# (Es más fácil de entender)


def biseccion(f, a, b, n=1, tol=1e-11):
    
    # La variable n cuenta las iteraciones
    # tol especifica la tolerancia permitida 
    # al método numérico
    
    print("n= ",n,": Bisección en el intervalo", 
                  "[", a,",", b, "]")
    if abs(b - a) < tol:
        return a
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) > 0:
        if f(b) > 0:
            raise Exception ("Error: hipótesis!")
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(c) > 0:
            # sabemos que f(b)<0 y f(c)>0
            return biseccion(f, c, b, n + 1, tol)
        else:
            # sabemos que f(a)>0 y  f(c)<0
            return biseccion(f, a, c, n + 1, tol)
    else:
        # caso en que f(a)<0
        if f(b) < 0:
            raise Exception ("Error: hipótesis!")
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(c) > 0:
            # sabemos que f(a)<0 y f(c)>0
            return biseccion(f, a, c, n + 1, tol)
        else:
            # sabemos que f(b)>0 y f(c) <0
            return biseccion(f, c, b, n + 1, tol)


if __name__ == "__main__":

    from math import sqrt, exp, log, sin, cos, pi

    # Ejemplo 1: calculemos la raíz cuadrada de 2 
    # encontrando una raíz de un polinomio


    def mi_funcion(x):
        return x * x - 2

    raiz_hallada = biseccion(mi_funcion, 0, 2,tol=1e-3)
    print("raiz_hallada=", raiz_hallada)
    print("valor exacto=", sqrt(2))

    # Otro ejemplo: calculemos el logaritmo de 2 como la inversa de la
    # exponencial


    def mi_funcion2(x):
        return exp(x) - 2

    raiz_hallada = biseccion(mi_funcion2, 0, 2, tol=1e-11)
    print("raiz_hallada=", raiz_hallada)
    print("valor exacto=", log(2))

    # ejemplo 3: calculemos pi/4 resolviendo la ecuación
    # sin(x)=cos(x)


    def mi_funcion3(x):
        return sin(x) - cos(x)

    raiz_hallada = biseccion(mi_funcion3, 0, pi / 2, tol=1e-12)
    print("raiz_hallada=", raiz_hallada)
    print("valor exacto=", pi / 4)
