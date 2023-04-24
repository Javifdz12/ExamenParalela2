import threading
import random

saldo_banca = 50000  # Saldo inicial de la banca

class jugador(threading.Thread):
    def __init__(self,nombre,saldo,apuesta):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.saldo = saldo
        self.apuesta = apuesta
    # Función para simular el juego a un número concreto
    def jugar_numero(self):
        while True:
            numero=random.randint(1,36)
            print(f'{self.nombre}: {self.saldo}')
            if self.saldo >= self.apuesta:
                print(f'{self.nombre} tiene pasta')
                # Se resta la apuesta del saldo
                self.saldo -= self.apuesta
                # Se simula el giro de la ruleta
                resultado = random.randint(1, 36)
                if resultado == numero:
                    print(f'{self.nombre} ha ganado')
                    # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                    self.saldo += 360
                else:
                    print(f'{self.nombre} ha perdido')
                    # Si no coincide, se pierde la apuesta
            else:
                # Si no hay suficiente saldo para apostar, se sale del bucle
                print(f'{self.nombre} no tiene suficiente pasta para apostar')
                break

    # Función para simular el juego a par/impar
    def jugar_par_impar(self):
        list=['par','impar']
        while True:
            if self.saldo >= self.apuesta:
                # Se resta la apuesta del saldo
                self.saldo -= self.apuesta
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
    def jugar_martingala(self):
        while True:
            numero=random.randint(1,36)
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
        self.jugar_numero()

jugador1=jugador('Javi',1000,10)
jugador2=jugador('Felipe',1000,10)
jugador3=jugador('Andres',1000,10)
jugador4=jugador('Juan',1000,10)
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

