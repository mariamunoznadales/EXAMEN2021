#EJERCICIO 1

num1 = int(input("Escriba un numero positivo menor que 1000:  "))
num2 = int(input("Escriba otro numero positivo menor que 1000:  "))

def obtener_cifras():
    if num1 > 1000:
        print("No es menor de 1000")
    elif num1 < 0:
        print("No es positivo")
    else:
        num2
        if num2 > 1000:
            print("No es menor de 1000")
        elif num2 < 0 :
            print("No es positivo")

obtener_cifras()

def mismas_cifras():
    if sorted(str(num1)) == sorted(str(num2)):
        print("Tienen las mismas cifras")
    else:
        print("Tienen diferentes cifras")

    
    cifras_num1 = sorted(str(num1))
    cifras_num2 = sorted(str(num2))
    
    print(f"Las cifras del primer número son: {cifras_num1}")
    print(f"Las cifras del segundo número son: {cifras_num2}")

mismas_cifras() 


#EJERCICIO 2

import random

def juego():
    print("JUEGO DE DADOS")

    valores= [
    int(input("Elija un valor del 1 al 6: ")),
    int(input("Elija otro valor del 1 al 6: ")),
    int(input("Elija otro valor del 1 al 6: "))]

    cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
    if cantidad_dados == 0:
        print("Imposible!")

    dados_lanzados = [random.randint(1, 6) for i in range(cantidad_dados)]
    print("Tirada de dados:", dados_lanzados)
     
    total_valores = sum(dado in valores for dado in dados_lanzados)
    if total_valores > cantidad_dados/2:
        print("Has ganado.")
    else:
        print("Has perdido")



juego()

#EJERCICIO 3

import random

def jugar_juego_dados():
    print("¡Bienvenidos a la competencia de dados!")

    puntuacion_marcus = obtener_puntuacion()
    puntuacion_julius = obtener_puntuacion()

    print(f"Marcus Cubitus obtuvo una puntuación de {puntuacion_marcus}")
    print(f"Julius Humerus obtuvo una puntuación de {puntuacion_julius}")

    determinar_ganador(puntuacion_marcus, puntuacion_julius)

def obtener_puntuacion():
    dado_anterior = None #No tiene ningún valor asignado al principio (False, 0, None)
    while True:
        dado = random.randint(1, 6)
        print(f"Tirando el dado... Resultado: {dado}")

        if dado == dado_anterior:
            print(f"¡Doble {dado}! Puntuación obtenida.")
            return dado
        else:
            dado_anterior = dado

def determinar_ganador(puntuacion_marcus, puntuacion_julius):
    if puntuacion_marcus == puntuacion_julius:
        print("¡Empate!")
    else:
        ganador = "Marcus Cubitus" if puntuacion_marcus > puntuacion_julius else "Julius Humerus"
        print(f"¡{ganador} es el ganador!")

if __name__ == "__main__":
    jugar_juego_dados()


def numeros_multiplos():
    print(" DIRECTOR DE MÚLTIPLOS")
    print("Escriba 3 números crecientes, le indicaré si alguno es múltiplo de otro")
    
    num1 = int(input("Primer número : "))
    num2 = int(input("Segundo número: "))
    num3 = int(input("Tercer número: "))
    
    if num1 == num2 or num2 == num3:
        print("Por favor, escriba números crecientes")
    elif num2 < num1 or num3 < num2:
        print("Por favor, escriba números crecientes.")
    else:
        if num2%num1 and num1%num2 and num3%num1 and num1%num3 and num2%num3 and num3%num2 != 0:
            print("Ningún número es múltiplo de otro")
        elif num1%num2 == 0:
            print(f"{num1} es múltiplo de {num2}")
        elif num2%num1 == 0:
            print(f"{num2} es múltiplo de {num1}")
        elif num3%num1 == 0:
            print(f"{num3} es múltiplo de {num1}")
        elif num1%num3 == 0:
            print(f"{num1} es múltiplo de {num3}")
        elif num2%num3 == 0:
            print(f"{num2} es múltiplo de {num3}")
        elif num3%num2 == 0:
            print(f"{num3} es múltiplo de {num2}")

numeros_multiplos() 



#EJERCICIO 4

import random

def juego ():
    
    puntos_julius = 0
    puntos_marcus = 0
    
    intentos = int(input("Cuantas veces se van a tirar los dados?: "))
    tiradas = [random.randint(1, 6) for i in range(intentos)]
    dado1 = tiradas
    dado2 = tiradas
    

    print("Tirada de dados:" + str(dado1) + str(dado2) )

   
    if dado1 == dado2:
        puntos_julius += 6
    elif dado1 != dado2:
        puntos_marcus += 1

    

    if puntos_julius > puntos_marcus:
        print(f" Ha ganado Julius {puntos_julius} a {puntos_marcus}")
    elif puntos_marcus > puntos_julius:
        print(f" Ha ganado Marcus {puntos_marcus} a {puntos_julius}")
    else:
        print(f"Empate a {puntos_julius} ")
juego()

