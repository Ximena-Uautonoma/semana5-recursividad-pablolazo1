"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    total=0
    for i in range(1,n+1):
        total= total+i
    return total

def suma_recursiva(n):
    if n==1:
        return 1
    else:
        return n+suma_recursiva(n-1)
    
