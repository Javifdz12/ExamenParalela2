import threading
import random

saldo_jugadores = [1000, 1000, 1000, 1000]  # Saldo inicial de los jugadores
saldo_banca = 50000  # Saldo inicial de la banca

# Función para simular el juego a un número concreto
def jugar_numero(saldo, numero):
    while True:
        apuesta = 10  # Apuesta de 10 euros
        if saldo >= apuesta:
            # Se resta la apuesta del saldo
            saldo -= apuesta
            # Se simula el giro de la ruleta
            resultado = random.randint(1, 36)
            if resultado == numero:
                # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                saldo += 360
            else:
                # Si no coincide, se pierde la apuesta
                pass
        else:
            # Si no hay suficiente saldo para apostar, se sale del bucle
            break

# Función para simular el juego a par/impar
def jugar_par_impar(saldo):
    while True:
        apuesta = 10  # Apuesta de 10 euros
        if saldo >= apuesta:
            # Se resta la apuesta del saldo
            saldo -= apuesta
            # Se simula el giro de la ruleta
            resultado = random.randint(1, 36)
            if resultado % 2 == 0:
                # Si el resultado es par y se apostó a par, se incrementa el saldo en 20 euros
                saldo += 20
            else:
                # Si el resultado es impar y se apostó a impar, se incrementa el saldo en 20 euros
                saldo += 20
        else:
            # Si no hay suficiente saldo para apostar, se sale del bucle
            break

# Función para simular el juego a la "martingala"
def jugar_martingala(saldo):
    apuesta = 10  # Apuesta inicial de 10 euros
    while True:
        if saldo >= apuesta:
            # Se resta la apuesta del saldo
            saldo -= apuesta
            # Se simula el giro de la ruleta
            resultado = random.randint(1, 36)
            if resultado == numero:
                # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                saldo += 360
                apuesta = 10  # Se vuelve a la apuesta inicial después de ganar
            else:
                # Si no coincide, se duplica la apuesta para el próximo turno
                apuesta *= 2
        else:
            # Si no hay suficiente saldo para apostar, se sale del bucle
            break

# Creación de hilos para simular los diferentes juegos
for i in range(4):
    numero = random.randint(1, 36)  # Número aleatorio para el juego a número concreto
    t1 = threading.Thread(target=jugar_numero, args=(saldo_jugadores[i], numero))
    t1.start()

# El hilo principal espera a que todos los hilos terminen antes de imprimir los saldos finales.
t1.join()

# Se imprime el saldo final de cada jugador y el saldo final de la banca
for i in range(4):
    print("Saldo final del jugador {}: {} euros".format(i+1, saldo_jugadores[i]))
print("Saldo final de la banca: {} euros".format(saldo_banca))

