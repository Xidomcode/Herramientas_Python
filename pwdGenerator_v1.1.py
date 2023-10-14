
from colorama import Fore, Style

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
purple = Fore.MAGENTA
reset = Style.RESET_ALL

colors = {'red': red, 'green': green, 'blue': blue, 'yellow': yellow, 'purple': purple, 'reset': reset}

# Función para Cerrar el script cuando pulsas Ctrl + C

import signal, sys

print(colors['yellow'] + "\n[+] Pulsa Ctrl + C en cualquier momento para cerrar el script.\n" + colors['reset'])

def fin_programa(signal, frame):
    print(colors['red'] + "\n\n[+] Cerrando programa...\n" + colors['reset'])
    sys.exit(0) 

signal.signal(signal.SIGINT, fin_programa)



import string
import random

# Función para obtener todos los parámetros que introducirá el usuario y detección de errores

def getInformation():

    print(colors['blue'] + "\n[+] GENERADOR DE CONTRASEÑAS [+]\n" + colors['reset'])

    while True:
        try:
            longitud = int(input("\nIndica la longitud de la contraseña: "))
            break
        except ValueError:
            print("\nError, introduce solo números.")
        
    minusculas = input("\n¿Quieres introducir minúsculas? (s/n): ")
    
    if minusculas == 's' or minusculas == 'S':
        letras_minusculas = string.ascii_lowercase
    else:
        print("\nNo tendrás minúsculas en la contraseña.\n")
        letras_minusculas = ''
    
    mayusculas = input("\n¿Quieres introducir mayúsculas? (s/n): ")

    if mayusculas == 's' or mayusculas == 'S':
        letras_mayusculas = string.ascii_uppercase
    else:
        print("\nNo tendrás mayúsculas en la contraseña.\n")
        letras_mayusculas = ''

    caracteres_especiales = input("\n¿Quieres introducir carácteres especiales? (s/n): ")

    if caracteres_especiales == 's' or caracteres_especiales == 'S':
        caracteres_especiales = string.punctuation
    else:
        print("\nNo tendrás carácteres especiales en la contraseña.\n")
        caracteres_especiales = ''
    
    numeros = input("\n¿Quieres introducir números? (s/n): ")

    if numeros == 's' or numeros == 'S':
        numeros = string.digits
    else:
        print("\nNo tendrás números en la contraseña.\n")
        numeros = ''


    return longitud, letras_minusculas, letras_mayusculas, caracteres_especiales, numeros


# Función para generar la contraseña

def generar_contraseña(longitud, letras_minusculas, letras_mayusculas, caracteres_especiales, numeros):

    lista_contraseña = []

    generando_contraseña = letras_minusculas + letras_mayusculas + caracteres_especiales + numeros

    if generando_contraseña == '':
        print(colors['red'] + "\nNo has introducido nada, saliendo del programa...\n" + colors['reset'])
        exit

    else:

        for i in range(longitud):

            contraseña = random.choice(generando_contraseña)
            lista_contraseña.append(contraseña)

        passwd = ''.join(lista_contraseña)
        
    return passwd


# Función main

def main():

    var_getInformation = getInformation()
    var_generar_contraseña = generar_contraseña(*var_getInformation)


    print(colors['green'] + "\n\n[+] Generando contraseña...\n" + colors['reset'])
    print("\tContraseña: ", colors['red'] + var_generar_contraseña + colors['reset'] + "\n")


if __name__ == "__main__":
    main()
