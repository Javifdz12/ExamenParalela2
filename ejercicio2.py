import threading
import random

saldo_banca = 50000  # Saldo inicial de la banca

class jugador(threading.Thread):
    def __init__(self,saldo,apuesta):
        threading.Thread.__init__(self)
        self.saldo = saldo
        self.apuesta = apuesta
    # Función para simular el juego a un número concreto
    def jugar_numero(self,numero):
        while True:
            if self.saldo >= self.apuesta:
                # Se resta la apuesta del saldo
                self.saldo -= self.apuesta
                # Se simula el giro de la ruleta
                resultado = random.randint(1, 36)
                if resultado == numero:
                    # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                    self.saldo += 360
                else:
                    # Si no coincide, se pierde la apuesta
                    pass
            else:
                # Si no hay suficiente saldo para apostar, se sale del bucle
                break

    # Función para simular el juego a par/impar
    def jugar_par_impar(self):
        while True:
            apuesta = 10  # Apuesta de 10 euros
            if self.saldo >= apuesta:
                # Se resta la apuesta del saldo
                self.saldo -= apuesta
                # Se simula el giro de la ruleta
                resultado = random.randint(1, 36)
                if resultado % 2 == 0:
                    # Si el resultado es par y se apostó a par, se incrementa el saldo en 20 euros
                    self.saldo += 20
                else:
                    # Si el resultado es impar y se apostó a impar, se incrementa el saldo en 20 euros
                    self.saldo += 20
            else:
                # Si no hay suficiente saldo para apostar, se sale del bucle
                break

    # Función para simular el juego a la "martingala"
    def jugar_martingala(self,numero):
        while True:
            if self.saldo >= self.apuesta:
                # Se resta la apuesta del saldo
                self.saldo -= self.apuesta
                # Se simula el giro de la ruleta
                resultado = random.randint(1, 36)
                if resultado == numero:
                    # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                    self.saldo += 360
                    self.apuesta = 10  # Se vuelve a la apuesta inicial después de ganar
                else:
                    # Si no coincide, se duplica la apuesta para el próximo turno
                    self.apuesta *= 2
            else:
                # Si no hay suficiente saldo para apostar, se sale del bucle
                break
    def run(self):
        self.jugar_numero(numero = random.randint(1, 36))

jugador1=jugador(1000,10)
jugador2=jugador(1000,10)
jugador3=jugador(1000,10)
jugador4=jugador(1000,10)
jugadores=[jugador1,jugador2,jugador3,jugador4]

# Creación de hilos para simular los diferentes juegos
for i in range(4):
    jugadores[i].start()

# El hilo principal espera a que todos los hilos terminen antes de imprimir los saldos finales.
for i in range(4):
    jugadores[i].join()

# Se imprime el saldo final de cada jugador y el saldo final de la banca
for i in range(4):
    print("Saldo final del jugador {}: {} euros".format(i+1, jugadores[i].saldo))
print("Saldo final de la banca: {} euros".format(saldo_banca))

