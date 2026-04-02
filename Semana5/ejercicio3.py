"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado=1
    while n>1:
        resultado=resultado*n
        n=n-1
    return resultado

def factorial_recursivo(n):
    if n==o or n==1:
        return 1
    else:
        return n*factorial_recursivo(n-1)
    
