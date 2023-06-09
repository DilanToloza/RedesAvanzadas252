import os
import time
import ipaddress

def menu():
    os.system("clear")
    print("¡Bienvenido al sistema de gestión de redes!")
    print("--------------MENU-------------------")
    print("1. Mostrar .txt de la carpeta.")
    print("2. Agregar nuevo Sector.")
    print("3. Leer Archivo.")
    print("4. Agregar al Archivo.")
    print("5. Reemplazar Texto en Archivo")
    print("6. Salir.")
    print("\n\n---------------------------------")


def ficheros():
    directory = os.getcwd()
    txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    print(txt_files)
    while True:
        print("Desea Salir? \nSi.\tNo.")
        sesion = input()
        if sesion.lower() == "no":
            os.system("clear")
            print(txt_files)
            time.sleep(10)
        elif sesion.lower() == "si":
            opc = 9
            break
    

def Nuevo_documento():
    print("Atencion: Se va a agregar un nuevo documento a la carpeta de archivos.\nFavor de no introducir el mismo nombre de alguno de los archivos.")
    ficheros()
    archivo = input("Ingrese nombre del archivo: ")
    archivo = archivo + ".txt"  # Corrección en la construcción de la ruta del archivo
    if os.path.exists(archivo):
        print("Ya existe un archivo creado con ese nombre.")
        print("Regresando...")
        time.sleep(3)
    else:
        with open(archivo, "w") as file:
            file.write("-------------------------------------------\n\t\t"+archivo+"\n-------------------------------------------\n")
            print("Archivo creado con exito.\nPara agregar nuevo contenido a este Archivo, ingresar a la opcion correspondiente.\nRegresando...")
            time.sleep(4)

def validador_IP(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def agregar():
    ficheros()
    archivo = input("Ingrese nombre del archivo: ")
    os.system("clear")
    print("Para agregar un nuevo dispositivo de red al documento, debe de hacerlo de la siguiente manera.\n")
    print("(NOMBRE)\n(DIRECCION IP)\n(VLAN)\n(SERVICIO)\n(CAPA DE RED)\n(SECTOR)\n")
    for x in range(6):
        if x == 0:#NOMBRE DEL DISPOSITIVO
            text = input("Ingrese el nombre del dispositivo: ")
            with open(archivo, 'a') as file:
                file.write("Nombre: " + text + "\n")
        elif x == 1:#DIRECCION IP
            while True:
                ip_address = input("Ingrese la direccion ip del dispositivo: ")
                if validador_IP(ip_address):
                    with open(archivo, 'a') as file:
                        file.write("Direccion IP: " + ip_address + "\n")
                    break
                else:
                    print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
        elif x == 2:#VLAN DEL DISPOSITIVO
            text = input("Ingrese VLAN perteneciente al dispositivo: ")
            with open(archivo, 'a') as file:
                file.write("VLAN: " + text + "\n")
        elif x == 3:#CAPA JERARQUICA DEL DISPOSITIVO
            text = input("Ingrese Capa jerarquica de dispositivo: ")
            with open(archivo, 'a') as file:
                file.write("Capa jerarquica: " + text + "\n")
        elif x == 4:#CAMPUS DEL DISPOSITIVO
            text = input("Ingrese Sector donde se ubica el dispositivo: ")
            with open(archivo, 'a') as file:
                file.write("Campus: " + text + "\n")
        elif x == 5:#SERVICIO DE RED DEL DISPOSITIVO
            text = input("Ingrese servicio de red que opere el dispositivo: ")
            with open(archivo, 'a') as file:
                file.write("Servicio de Red: " + text + "\n")
    separador = "---------------------------------------"
    with open(archivo, 'a') as file:#AGREGA SEPARADOR
        file.write(separador + "\n")
    print("Texto agregado con exito al Archivo.")

def leer():
    ficheros()
    archivo = input("Ingrese nombre del archivo: ")
    try:
        with open(archivo, 'r') as file:
            contents = file.read()
            print(contents)
            time.sleep(10)
            while True:
                print("Desea prolongar su sesión de lectura? \nSi.\tNo.")
                sesion = input()
                if sesion.lower() == "si":
                    os.system("clear")
                    print(contents)
                    time.sleep(10)
                elif sesion.lower() == "no":
                    opc = 9
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.\nRegresando...")
        time.sleep(3)


def reemplazar():
    archivo = input("Ingrese nombre del archivo: ")
    with open(archivo, 'r') as file:
        contents = file.read()
        print(contents)
    antiguo = input("Ingrese el Texto que desea Reemplazar: ")
    nuevo = input("Ingrese el nuevo Texto para Reemplazar: ")
    with open(archivo, 'r+') as file:
        contents = file.read()
        contents = contents.replace(antiguo, nuevo)
        file.seek(0)
        file.write(contents)
        file.truncate()
    print("Texto reemplazado en el Archivo " + archivo)


def Admin(username, password):
    with open("credenciales.txt", "r") as f:
        for line in f:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False


os.system("clear")
username = input("Introduzca nombre de Administrador: ")
password = input("Introduzca Contraseña: ")
os.system("clear")

if Admin(username, password):
    print("--------Acceso Habilitado--------\n\n")
    while True:
        menu()
        opc = input("Que desea realizar?: ")
        os.system("clear")
        if opc == '1':
            os.system("clear")
            ficheros()
        elif opc == '2':
            os.system("clear")
            Nuevo_documento()
        elif opc == '3':
            os.system("clear")
            leer()
        elif opc == '4':
            os.system("clear")
            agregar()
        elif opc == '5':
            os.system("clear")
            reemplazar()
        elif opc == '6':
            os.system("clear")
            print("Saliendo del Programa.")
            time.sleep(3)
            os.system("clear")
            break
        else:
            print("Opcion Invalida.")
else:
    print("Credenciales incorrectas. Acceso denegado.")
