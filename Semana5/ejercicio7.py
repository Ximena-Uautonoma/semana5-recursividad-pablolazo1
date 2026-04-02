"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    total=0
    for monto in ahorros:
        total=total+monto
    return total 


def ahorro_total_recursivo(ahorros):
   if not ahorros:
       return 0
    return ahorros[0]+ahorro_total_recursivo(ahorros[1:])
