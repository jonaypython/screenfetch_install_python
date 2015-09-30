#!/usr/bin/python3

import os
import urllib.request
import getpass


#Modo de uso : sudo python3 + script

print("""
                              _____    _       _     
 ___  ___ _ __ ___  ___ _ __ |  ___|__| |_ ___| |__  
/ __|/ __| '__/ _ \/ _ \ '_ \| |_ / _ \ __/ __| '_ \ 
\__ \ (__| | |  __/  __/ | | |  _|  __/ || (__| | | |
|___/\___|_|  \___|\___|_| |_|_|  \___|\__\___|_| |_|
                                                     
By : Jonay ,Administrador de  : https://www.facebook.com/InSeguridadInformaticaSt
Nassima , Administradora de www.sanvendida.com , de Inseguridadinformática y editora de cyberpunk, facebook.com/Cyberpunks.Hackers.2015
diego , Administrador de Inseguridadinformática y estudiante de marketing""")



if getpass.getuser() == "root":
    directorio = os.chdir("/usr/bin/")  
    descarga = urllib.request.urlretrieve("https://raw.github.com/KittyKatt/screenFetch/master/screenfetch-dev " , "screenfetch")
    permisos = ("sudo chmod +x screenfetch")
    print ("Ahora que se a instalado correctamente,para que se ejecute siempre desde la terminal,lea el archivo terminal.txt")
else:
    print("Debes de ejecutar el script con sudo : sudo python3 screenfetch_install.py ")


