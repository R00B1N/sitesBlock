#!/usr/bin/python3

import time
from datetime import datetime as tiempito
from colorama import Fore, init
from shutil import copyfile, rmtree
from os import mkdir
import signal

init()

# Adding the banner.
mybanner = """
,d88~~\ ,e,   d8                          888~~\  888                  888   _   
8888     "  _d88__  e88~~8e   d88~\       888   | 888  e88~-_   e88~~\ 888 e~ ~  
`Y88b   888  888   d888  88b C888         888 _/  888 d888   i d888    888d8b    
 `Y88b, 888  888   8888__888  Y88b        888  \  888 8888   | 8888    888Y88b   
   8888 888  888   Y888    ,   888D       888   | 888 Y888   ' Y888    888 Y88b  
\__88P' 888  "88_/  "88___/  \_88P        888__/  888  "88_-~   "88__/ 888  Y88b 
                                                                                 
       
       +++ by R00B1N +++ 
                            Github: https://github.com/R00B1N                                                                             
"""

# Adding some utils variables.
ruta_host = r"C:\Windows\System32\drivers\etc\hosts"
global lista_sitios
lista_sitios = []


def main():
    # Backup for restoring the file.
    rmtree(r"C:\Windows\System32\drivers\etc\hostsBackup")
    mkdir(r"C:\Windows\System32\drivers\etc\hostsBackup")
    copyfile(r"C:\Windows\System32\drivers\etc\hosts", r"C:\Windows\System32\drivers\etc\hostsBackup\hosts")
    # os.system('cls')
    print(Fore.LIGHTGREEN_EX)
    print(mybanner)
    menu = """\n\t############### Opciones ###############\n\n1-Iniciar Script.\n2-Mostrar Lista de Sitios Bloqueados\n\n3-Salir."""
    print(menu)
    ask = int(input("\n[*]Escoge una opcion: "))
    if ask == 1:
        main1()
    elif ask == 2:
        with open(ruta_host, "r+") as myfile:
            content = myfile.readlines()
            print(Fore.RED)
            print("\nLista de Sitios Bloqueados!\n")
            for line in content:
                if line.startswith('127.0.0.1 '):
                    print(Fore.YELLOW)
                    print(line.replace("127.0.0.1", ""))
            print(Fore.CYAN)
            input("\nPresione Enter para continuar!")
            main()
    elif ask == 3:
        print("Saliendo del Programa!...")
        exit(0)
    elif ask == " ":
        print(Fore.RED)
        print("\nOpcion no Valida!")
        main()
    else:
        print("Introduce una opcion Valida!")
        main()


def handler(signum, frame):
    print(Fore.RED)
    res = input("Desea detener el programa? (y/n): ")
    if res == 'y':
        ask = input("[*]Desea Borrar todos los sitios de la lista? (y/n): ")
        if ask == 'y':
            with open(ruta_host, "r+") as myfile:
                content = myfile.readlines()
                for line in content:
                    if line.startswith('127.0.0.1 '):
                        print(Fore.RED)
                        print(line)
                copyfile(r"C:\Windows\System32\drivers\etc\hostsBackup\hosts", r"C:\Windows\System32\drivers\etc\hosts")
                print("\nSitios Borrados Exitosamente")
                input("\nPresiona Enter para Continuar!")
                main()
        else:
            main()
    else:
        pass


def main1():
    # Main List.
    busqueda = "127.0.0.1"
    lista_sitios = [
        "www.facebook.com",
        "www.instagram.com",
        "www.twitter.com",
    ]
    # Adding some sites manually.
    asking = str(input("[*]Deseas agregar mas sitios manualmente (y/n): "))
    if asking == 'y':
        while True:
            print(Fore.CYAN)
            mysites = input("[*]!Introduce un sitio para bloquearlo: ")
            lista_sitios.append(mysites)
            print(Fore.LIGHTGREEN_EX)
            asking_for = str(input("[]Desea continuar agregando sitios? (y/n) : "))
            if asking_for == "y":
                continue
            else:
                break

    else:
        pass
    ruta_host = r"C:\Windows\System32\drivers\etc\hosts"
    dir_host = ruta_host
    print(Fore.LIGHTYELLOW_EX)
    desde_hr = int(input("[*]Hora de inicio: "))
    hasta_hr = int(input("[*]Hora de apagado: "))

    signal.signal(signal.SIGINT, handler)

    while True:
        print(lista_sitios)
        time.sleep(5)
        if tiempito(tiempito.now().year, tiempito.now().month, tiempito.now().day, desde_hr) < tiempito.now() < \
                tiempito(tiempito.now().year, tiempito.now().month, tiempito.now().day, hasta_hr):
            print(Fore.GREEN)
            print("\nBloqueando...")
            print(Fore.GREEN)
            print("Bloqueador de Sitios Activado!")
            with open(dir_host, 'r+') as myfile:
                content = myfile.read()
                for sites in lista_sitios:
                    if sites in content:
                        pass
                    else:
                        myfile.write("\n" + busqueda + " " + sites + "\n")
            with open(ruta_host, "r+") as myfile:
                content = myfile.readlines()
                for line in content:
                    if line.startswith('127.0.0.1 '):
                        print(Fore.YELLOW)
                        print(line.replace("127.0.0.1", ""))

        else:
            print(Fore.LIGHTRED_EX)
            print("Bloqueador de Sitios Desactivado!")
            with open(dir_host, 'r+') as myfile:
                myfile.readlines()
                myfile.seek(0)
            time.sleep(7)


if __name__ == "__main__":
    main()
