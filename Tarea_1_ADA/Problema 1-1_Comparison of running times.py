
tiempos = [10**6, 60 * 10**6, 36 * 10**8, 864 * 10**8, 26298 * 10**8, 315576 * 10**8, 315576 * 10**10]

duraciones = ["1 segundo", "1 minuto", "1 hora", "1 dia", "1 mes", "1 año", "1 siglo"]

duracion = 0
for i in tiempos:
    n = 1
    factorial = 1
    while factorial < i:
        factorial += factorial * n
        n += 1
    print(duraciones[duracion], n - 1)
    duracion += 1
