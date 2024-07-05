
while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Introduzca los puntos de valoración y los comentarios ')
    print('2: Comprueba los resultados obtenidos hasta ahora')
    print('3: Terminación.' )
    num = input()
    
    if num.isdecimal():
        num=int(num)
        
        if num == 1:
            while True:
                print('Por Favor, introduzca una puntuación en una escala de 1 a 5')
                punto = input()
                if punto.isdecimal():
                 punto = int(punto)
                if punto <= 1 or  punto > 5:
                    print('Indique una escala de 1 a 5: ')
                    punto = input()
                else:
                    print('Introduzca sus comentarios: ')
                    comentario = input()
                    post = f'punto: {punto} comentario: {comentario}'
                    with open("data.txt", 'a') as file_pc:
                        file_pc.write(f'{post} \n')
                    file_pc.close()
                    break
                
                #si se introduce un valor no numerico(int)
            else:
                print('Introduzca un numero')
        elif num == 2:
            print('Resultado hasta la fecha') 
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        elif num == 3:
            print('Terminación')
            break
        else:
            print('Por favor, Introduzca de 1 a 3')
    else:
        print('Por favor, introduzca un número válido')