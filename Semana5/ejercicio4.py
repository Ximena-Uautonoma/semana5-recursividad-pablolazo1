"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contador=0
    num=n
    while num>0:
        if num%2==0:
            contador=contador+1
        num=num-1
        


def contar_pares_recursivo(n):
        if n>0:
            if n%2==0:
                return 1+contar_pares_recursivo(n-1)
            else:
                return 0+contar_pares_recursivo(n-1)
        else:
            return 0
