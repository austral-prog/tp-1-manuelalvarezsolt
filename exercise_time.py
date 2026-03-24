def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    minutos = 3665 // 60
    horas = minutos // 60
    minutoscom = minutos - horas * 60
    segundoscom = total_segundos - (horas * 60) * 60 - minutoscom * 60
    print(horas)
    print(minutoscom)
    print(segundoscom)
