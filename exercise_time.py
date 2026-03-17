def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    minutos = 3665 / 60
    horas = minutos // 60
    minutos_restantes = total_segundos // 60
    segundos_restantes = total_segundos % 60
    print(horas)
    print(minutos)
    print(segundos_restantes)
