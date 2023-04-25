from ejercicio1 import unittest
from ejercicio2 import jugador,ruleta
def lanzar_ej1():
    print('\n-- EJERCICIO 1 --\n')
    unittest.main()
def lanzar_ej2():
    ruleta1=ruleta(50000)
    jugador1=jugador('Javi',1000,10,ruleta1)
    jugador2=jugador('Felipe',1000,10,ruleta1)
    jugador3=jugador('Andres',1000,10,ruleta1)
    jugador4=jugador('Juan',1000,10,ruleta1)
    jugadores=[jugador1,jugador2,jugador3,jugador4]

    # Creación de hilos para simular los diferentes juegos
    for i in range(4):
        jugadores[i].start()
    ruleta1.start()

    # El hilo principal espera a que todos los hilos terminen antes de imprimir los saldos finales.
    ruleta1.join()
    for i in range(4):
        jugadores[i].join()

    print('\n-- EJERCICIO 2 --\n')
    # Se imprime el saldo final de cada jugador y el saldo final de la banca
    for i in range(4):
        print("Saldo final del jugador {}: {} euros".format(i+1, jugadores[i].saldo))
    print("Saldo final de la banca: {} euros".format(ruleta1.banca))