from random import randint
import csv

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

def numeros(dados,cat):
    valor=0
    for i in range(len(dados)):
        if int(cat)==dados[i]:
            valor+=int(dados[i])
    return valor

def nueva_categoria(dados,tiradas):
    cat_elegida = input("Elija una categoria para anotar: ")
    print("Desea tachar la categoria?") 
    tachar=validar_rta()
    if tiradas==1:
        valor=5
    else:
        valor=0
    if cat_elegida == "E" and tachar == "NO":
        valor += 20
    elif cat_elegida == "F" and tachar == "NO":
        valor += 30
    elif cat_elegida == "P" and tachar == "NO":
        valor += 40
    elif cat_elegida == "G" and tachar == "NO":
        valor += 50
    if cat_elegida!='E' and cat_elegida!='F' and cat_elegida!='P' and cat_elegida!='G':
        valor=numeros(dados,cat_elegida)
    return valor,cat_elegida,tachar

def categorias(l1, l2, tiradas,dados): 
        jugador = int(input('Que jugador quiere anotar: '))
        valor, cat_elegida, tachar = nueva_categoria(dados,tiradas)
        if jugador == 1 :
            l1[0].append(cat_elegida)
            l1[1] = int(valor)
        if jugador == 2 :
            l2[0].append(cat_elegida)
            l2[1] = int(valor)


        return(cat_elegida, jugador, valor, tachar)   


def guardar_o_modificar(categoria, jugador, puntos, tachar, dados,tiradas):
    archivo = "jugadas.csv"

    try:
        # Intento leer el archivo (si existe)
        planilla = []
        with open(archivo, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)  # salteo encabezado

            for fila in lector:
                
                if fila[1] == "":
                    j1 = ''
                else:
                    j1 = fila[1]

                if fila[2] == "":
                    j2 = ''
                else:
                    j2 = fila[2]
                    
                planilla.append([fila[0], j1, j2])


    except FileNotFoundError:
        # Si no existe, creo planilla inicial 

        planilla = [["E", '', ''], ["F", '', ''], ["P", '', ''], ["G", '', ''], ["1", '', ''], ["2", '', ''], ["3", '', ''], ["4", '', ''], ["5", '', ''], ["6", '', ''],['Total:',0,0]]
    #  Modifico el puntaje
    anotado=False
    while anotado==False:
        for fila in planilla:
            if fila[0] == categoria:
                if jugador == 1:
                    if fila[1]=='' and tachar == "NO":
                        fila[1] = puntos
                        anotado=True
                    elif fila[1]=='' and tachar == "SI":
                        fila[1] = 0
                        anotado=True
                    else:
                        anotado=False
                                                                            
                else:
                    if fila[2]=='' and tachar=='NO':
                        fila[2] = puntos
                        anotado=True
                    elif fila[2] == '' and tachar == "SI":
                        fila[2] = 0
                        anotado=True
                    else:
                        anotado=False
                    
       
        if anotado==False:                
            print('Esta categoria ya fue utilizada. Elija otra.')
            puntos,categoria,tachar=nueva_categoria(dados,tiradas)
    total=0   
    for pos in range(1,len(planilla)-1):
        if jugador==1 and planilla[pos][1]!='':
            total+=int(planilla[pos][1])
        elif jugador==2 and planilla[pos][2]!='':
            total+=int(planilla[pos][2])
    if jugador==1:
        planilla[len(planilla)-1][1]=total
    else:
        planilla[len(planilla)-1][2]=total
    

                  
                    

    # Reescribo el archivo completo
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Categoria", "Jugador 1", "Jugador 2"])

        for fila in planilla:
            escritor.writerow(fila)
            

def main():
    turnos=0
    while turnos<20:
        jugador1 = [[], []]
        jugador2 = [[], []]
        dados,nro_tirada=tirar_dados()
        cat, jugador, valor, tachar = categorias(jugador1, jugador2, nro_tirada,dados)
        guardar_o_modificar(cat, jugador, valor, tachar,dados,nro_tirada)
        turnos+=1



# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
