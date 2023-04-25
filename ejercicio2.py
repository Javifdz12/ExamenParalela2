import threading
import random
import time

class jugador(threading.Thread):
    def __init__(self,nombre,saldo,apuesta,ruleta):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.saldo = saldo
        self.apuesta = apuesta
        self.ruleta=ruleta
    # Función para simular el juego a un número concreto
    def jugar_numero(self):
        while True:
            numero=random.randint(1,36)
            print(f'{self.nombre}: {self.saldo}')
            if self.saldo >= self.apuesta :
                if self.ruleta.lock.locked()==False:
                    print(f'{self.nombre} tiene pasta y va a apostar')
                    # Se resta la apuesta del saldo
                    self.saldo -= self.apuesta
                    self.ruleta.banca += self.apuesta
                    # Se simula el giro de la ruleta
                    if self.ruleta.resultado == numero :
                        if self.ruleta.banca>=360:
                            print(f'{self.nombre} ha ganado')
                            # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                            self.saldo += 360
                            self.ruleta.banca -= 360
                        else:
                            self.saldo += self.ruleta.banca
                            self.ruleta.banca=0
                    elif self.ruleta.resultado == 0:
                        print('Ha salido el cero')
                        self.ruleta.banca+=self.saldo
                        self.saldo=0
                    else:
                        print(f'{self.nombre} ha perdido')
                        # Si no coincide, se pierde la apuesta
                else:
                    print(f'la ruleta esta funcionando espera al siguiente turno')
                    pass
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
                if self.ruleta.resultado % 2 == 0:
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
                if self.ruleta.resultado == numero:
                    # Si el número apostado coincide con el resultado, se incrementa el saldo en 360 euros
                    self.saldo += 360
                    self.ruleta.banca -= 360
                    self.apuesta = 10  # Se vuelve a la apuesta inicial después de ganar
                elif self.ruleta.resultado == 0:
                    self.ruleta.banca+=self.saldo
                    self.saldo=0
                else:
                    # Si no coincide, se duplica la apuesta para el próximo turno
                    self.apuesta *= 2
            else:
                # Si no hay suficiente saldo para apostar, se sale del bucle
                break
    def run(self):
        while True:
            if self.saldo>0 and self.ruleta.banca>0:
                self.jugar_numero()
            else:
                break

class ruleta(threading.Thread):
    def __init__(self,banca):
        threading.Thread.__init__(self)
        self.banca = banca
        self.resultado=None
        self.lock=threading.Lock()
    def lanzar_bola(self):
        self.resultado = random.randint(0,36)
        time.sleep(0.5)
        self.lock.acquire()
        time.sleep(3)
        self.lock.release()
    def run(self):
        while True:
            if self.banca>0 and self.resultado!=0 and self.banca<54000:
                self.lanzar_bola()
            else:
                break




