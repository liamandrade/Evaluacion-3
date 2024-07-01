def menu():
    print('Seleccione una opción: ')
    print('1. Registrar puntajes de torneo')
    print('2. Listar los puntajes')
    print('3. Imprimir por tipo')
    print('4. Salir del programa')
    op=int(input('-->: '))
    
def listarPuntajes():
    idJugadores=[]
    nombreJugadores=[]
    idJugador=input('Ingrese su id de jugador: ')
    idJugadores.append(idJugador)
    nombre=input('Ingrese su nombre y apellido: ')
    nombreJugadores.append(nombre)    
    listaJuegos=[]
    print('Seleccione los juegos en los que compite:')
    print('1. Valorant')
    print('2. Fortnite')
    print('3. Fifa')
    print('4. Dejar de escojer')
    flag=True
    while flag:
        try:
            selec=int(input('Escoja: '))
            if selec==1:
                print('Valorant seleccionado')
                listaJuegos.append('Valorant')
            elif selec==2:
                print('Fortnite seleccionado')
                listaJuegos.append('Fortnite')
            elif selec==3:
                print('Fifa seleccionado ')
                listaJuegos.append('Fifa')
            elif selec==4:
                print('Juegos escogidos')
                flag=False
            else:
                print('Seleccione una opcion valida')
            return listaJuegos
        except:
            print('La opcion debe ser un numero')
    for i in listaJuegos:
        puntaje=int(input('Ingrese su puntaje obtenido en el juego seleccionado: '))
    print('Seleccione su nivel de jugador: ')
    print('1. Principiante')
    print('2. Avanzado')
    print('3. Experto')
    nivelJugador=int(input('-->: '))
    nivel=[]
    flag2=True
    while flag2:
        try:
            if nivelJugador==1:
                print('Principiante seleccionado')
                nivel.append('Principiante')
                flag2=False
            elif nivelJugador==2:
                print('Avanzado seleccionado')
                nivel.append('Avanzado')
                flag2=False
            elif nivelJugador==3:
                print('Experto seleccionado')
                nivel.append('Experto')
                flag2=False
            else:
                print('Opcion invalida')
        except:
            print('La opcion debe ser un numero')        
    print('Id jugador| Nombre | Valorant | Fortnite | Fifa | Tipo ')
    print(idJugadores, nombreJugadores, i, nivel)
    



