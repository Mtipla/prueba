import numpy
import os
import time 
import msvcrt

lst_guarderia=numpy.zeros((2,5),int)
lst_rut_dueno=[]
lst_nombre_dueno=[]
lst_nombre_mascota=[]
lst_dias=[]
lst_fila=[]
lst_columna=[]

def menu_p():
    os.system("cls")
    print('''MENU PRINCIPAL
    1.Guardar datos mascota y dueño
    2.Buscar mascota
    3.Retirar mascota y pagar 
    4.Salir''')

def validar_numero(p_min,p_max,contex,contex2):
    while True:
        try:
            opc=int(input(f"ingrese {contex} : "))
            if opc >= p_min and opc<=p_max:
                return opc
            else:
                print(f"ERROR! {contex2}")
        except:
            print("ERROR! INGRESE UN NUMERO ENTERO!")

def vallidar_rut():
    while True:
        try: 
            rut=int(input("ingrese su rut: "))
            if rut >=1000000 and rut <=99999999:
                return rut
            else:
                print("ERRRO! RUT NO VALIDO!")
        except:
            print("ERROR! INGRESE UN NUMEROS ENTEROS!")

def vallidar_nombre(p_nm):
    while True:
        if p_nm == 1:
            nmbr=input("ingrese su nombre:")
            if len(nmbr.strip()) >=3 and nmbr.isalpha :
                return nmbr
            else:
                print("ERROR! EL NOMBRE DEBE SER DE 3 O MAS LETRAS!")
        elif p_nm==2:
            nmbr=input("ingrese el nombre de su mascota: ")
            if len(nmbr.strip()) >=3 and nmbr.isalpha :
                return nmbr
            else:
                print("ERROR! EL NOMBRE DEBE SER DE 3 O MAS LETRAS!")

def valid_fila():
    while True:
        try:
            fl=int(input("ingrese el piso de la habitacion: "))
            if fl in (1,2):
                return fl
            else:
                print("ERROR! PISO INVALIDO")
        except:
            print("ERROR! INGRSE UN NUMERO ENTERO!")

def valid_columna():
    while True:
        try:
            cl=int(input("ingrese columna de la habitacion: "))
            if cl in (1,2,3,4,5):
                return cl
            else:
                print("ERROR! COLUMNA INVALIDO")
        except:
            print("ERROR! INGRSE UN NUMERO ENTERO!")

def grabar():
    os.system("cls")
    print("INGRESAR MASCOTA")
    if 0 not in lst_guarderia:
        print("GUARDERIA LLENA! VUELVA MAS TARDE")
        time.sleep(3)
        return
    rut_d=vallidar_rut()
    nombre_d=vallidar_nombre(1)
    nombre_m=vallidar_nombre(2)
    dias=validar_numero(1,9999999,"numero de dias","NUMERO DE DIAS NO PUEDE SER MENOR A 0")  
    print("HABITACIONES DISPONIBLES")
    ver_habitaciones()
    while True:
        fila=valid_fila()
        columna=valid_columna()
        if lst_guarderia[fila-1][columna-1]==0:
            lst_rut_dueno.append(rut_d)
            lst_nombre_dueno.append(nombre_d)
            lst_nombre_mascota.append(nombre_m)
            lst_dias.append(dias)
            lst_guarderia[fila-1][columna-1]=1
            lst_fila.append(fila-1)
            lst_columna.append(columna-1)
            print("Habitacion registrada con exito")
            time.sleep(3)
            break
        else:
            print("Esta habitacion ya esta ocupad, elija otra por favor ")
            time.sleep(3)

def ver_habitaciones():
    print("        1 2 3 4 5 ")
    for x in range(2):
        print(f"Piso {x+1}:",end=" ")
        for y in range(5):
            print(lst_guarderia[x][y],end=" ")
        print()
    print("pulse una tecla para continuar...")
    msvcrt.getch()

def buscar_m():
    print("Buscar mascota por el rut")
    rut=vallidar_rut()
    if rut in lst_rut_dueno:
        posicion=lst_rut_dueno.index(rut)
        fila=lst_fila.index(posicion)
        columna=lst_columna.index(posicion)
        ver_habitaciones()
        print(f"Su mascota se encuentra en el piso {fila+1} y la columna {columna+1}")
        time.sleep(3)
    else:
        print("SU RUT NO ESTA REGISTRADO EN NUESTROS ARCHIVOS")

#me falto popear bien
def retirasre():
    print("RETIRAR MASCOTA Y PAGAR")
    rut=vallidar_rut()
    if rut in lst_rut_dueno():
        posicion=lst_rut_dueno.index(rut)
        dias=lst_dias(posicion)
        print(f"SU TOTAL A PAGAR ES: {dias*15000}")
        lst_nombre_dueno.pop(posicion)
        lst_nombre_mascota.pop(posicion)
        lst_rut_dueno.pop(posicion)
        print("Preione un boton para continuar...")
        msvcrt.getch()
    else:
        print("No tiene ninguna mascota registrada a este rut ")
        time.sleep(3)