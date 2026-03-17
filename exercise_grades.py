def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    nota4 = (nota1+nota2+nota3)
    promedio = (nota4/3)
    print(promedio)
    maximo = max(nota1,nota2,nota3)
    print(maximo)
    minimo = min(nota1,nota2,nota3)
    print(minimo)
    faltantes = 10 - promedio
    print(faltantes)
