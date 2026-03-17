def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    maximo = max(15, 8, 23, 12)
    minimo = min(15, 8, 23, 12)
    diferencia = maximo - minimo
    print("diferencia es", diferencia)
    print("maximo", maximo)
    print("minimo", minimo)
