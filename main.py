# Tu implementacion va aqui
from random import randint
def tirar_dados():
    tiradas=0
    fin_turno=False
    dados=[0,0,0,0,0]
    dados_listos=[False,False,False,False,False]
    while tiradas<3 and fin_turno==False:
        if tiradas==0:
            for i in range(len(dados)):
                dados[i]=randint(1,6)
                print(f'Dado',i+1,'=',dados[i])
        if tiradas>=1:
            print('¿Desea volver a tirar?')
            rta=validar_rta()
            if rta=='SI':
                for i in range(len(dados)):
                    if dados_listos[i]==False:
                        print('¿Desea volver a tirar el dado',i+1,'?')
                        rta=validar_rta()
                        if rta=='SI':
                            dados[i]=randint(1,6)
                        else:
                            dados_listos[i]=True
                for i in range(len(dados)):
                    print(f'Dado',i+1,'=',dados[i])
            else:
                fin_turno=True
        if fin_turno==False:
            tiradas+=1
    return dados,tiradas



def validar_rta():
    rta_valida=False
    while rta_valida==False:
        rta=input('SI/NO:')
        if rta=='SI' or rta=='NO':
            rta_valida=True
        else:
            print('Su respuesta fue invalida, responda SI/NO')
    return rta

import csv

def guardar_o_modificar(categoria, jugador, puntos):
    archivo = "jugadas.csv"

    try:
        # Intento leer el archivo (si existe)
        planilla = {}

        with open(archivo, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)  # salteo encabezado

            for fila in lector:
                planilla[fila[0]] = [int(fila[1]), int(fila[2])]

    except FileNotFoundError:
        # Si no existe, creo planilla inicial en 0

        planilla = [["E", 0, 0], ["F", 0, 0], ["P", 0, 0], ["G", 0,
0], ["1", 0, 0], ["2", 0, 0], ["3", 0, 0], ["4", 0, 0], ["5", 0, 0],
["6", 0, 0]]






    #  Modifico el puntaje
    for fila in planilla:
        if fila[0] == categoria:
            if jugador == 1:
                if fila[1]==0:
                    fila[1] = puntos
            else:
                if fila[2]==0:
                    fila[2] = puntos

    # Reescribo el archivo completo
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Categoria", "Jugador 1", "Jugador 2"])

        for fila in planilla:
            escritor.writerow(fila)


def categorias(l1, l2):
        jugador = int(input('Que jugador quiere anotar: '))
        cat_elegida = input("Elija una categoria para anotar: ")
        valor = 0
        tirada = 0
        # if tirada == 1:
        #     OpcionesPrimeraTirada()


        if cat_elegida == "E":
            valor += 20
        elif cat_elegida == "F":
            valor += 30
        elif cat_elegida == "P":
            valor += 40
        elif cat_elegida == "G":
            valor += 50
        elif cat_elegida == "1":
            valor = input("Ingrese el valor: ")
        elif cat_elegida == "2":
            valor = input("Ingrese el valor: ")
        elif cat_elegida == "3":
            valor = input("Ingrese el valor: ")
        elif cat_elegida == "4":
            valor = input("Ingrese el valor: ")
        elif cat_elegida == "5":
            valor = input("Ingrese el valor: ")
        elif cat_elegida == "6":
            valor = input("Ingrese el valor: ")

        if jugador == 1 :
            l1[0].append(cat_elegida)
            l1[1] = int(valor)
        if jugador == 2 :
            l2[0].append(cat_elegida)
            l2[1] = int(valor)


        return(cat_elegida, jugador, valor)

def main():
    jugador1 = [[], []]
    jugador2 = [[], []]
    dados,nro_tirada=tirar_dados()
    cat, jugador, valor = categorias(jugador1, jugador2)
    guardar_o_modificar(cat, jugador, valor)
main()

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
    "hola"



