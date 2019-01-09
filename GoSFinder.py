import urllib2
from colorama import *
import argparse
__author__ = 'Katz'
__version__ = '1.0'

#Por favor, recuerde que copiando codigo no te hace un programador
#toma algun tiempo para aprender a programar tu propios tools
#La communidad te nesecita! No seas un $crIpT kIddI3.

#Darle credito al desarrollador: Katz
#Contacto: Twitter: 0Katz
#Facebook: Metasploit En Espanol 

"""
=======================
 WEB CRAWL
=======================
 """

parser = argparse.ArgumentParser()
parser.add_argument("-n","--nombre", help="USAGE: python2 ghostofshell.py -a GoS")
args = parser.parse_args()
print "Buena suerte con tu escaneo.",Style.BRIGHT,args.nombre, Style.NORMAL, Style.RESET_ALL

from colorama import init, Fore, Back, Style
init(autoreset=True)
 
print Fore.RED +"                   _.-,"
print Fore.BLUE + Fore.YELLOW +"              _ .-'  / .._"
print Fore.YELLOW +"           .-:'/ - - \:::::-."
print Fore.CYAN + "         .::: '  e e  ' '-::::."
print Fore.GREEN + "        ::::'(    ^    )_.::::::"
print Fore.MAGENTA +"       ::::.' '.  o   '.::::'.'/_"
print Fore.YELLOW + "   .  :::.'       -  .::::'_   _.:"
print Fore.YELLOW + Fore.BLUE +" .-''---' .'|      .::::'   '''::::"
print Fore.RED +"'. ..-:::'  |    .::::'        ::::"
print Fore.MAGENTA +" '.' ::::    \ .::::'          ::::"
print Fore.CYAN + "      ::::   .::::'           ::::"
print Fore.GREEN + Fore.RED +"       ::::.::::'._          ::::"
print Fore.YELLOW +"        ::::::' /  '-      .::::"
print Fore.WHITE +"         '::::-/__    __.-::::'"
print Fore.RED +"           '-::::::::::::::-'"
print Fore.CYAN + "               '''::::'''"
try:    
    website = raw_input(Fore.MAGENTA +"> SITIO PARA SCANEAR: " + Style.RESET_ALL)
    if "http://" not in website:
        website ="http://"+ website
    with open("gosadmin.txt", "r") as ins:
        cont= ins.read() 
        arr = eval(cont)
        array=arr   
        
        length = max(map(len, array)) + len(website)
    for i in array:
        try:
            panel = urllib2.urlopen(website+i)
            checkurl = panel.code
            length_url = len(website+i)
            if checkurl == 200:
                print Fore.GREEN + website+i, " " * (length - length_url) + "[+]FOUND[+]" + Style.RESET_ALL
                continue
        except urllib2.URLError, checkurl:
            length_url = len(website+ i)
            if checkurl == 400:
                print  website+i," " * (length - length_url) + Fore.RED + "[+]NOT FOUND[+]" 
            else:
                print Fore.RED + website+i, " " * (length - length_url) + Fore.RED + "[-]ERROR[-]" 
                
except KeyboardInterrupt:
    print Back.RED + "Nos Vemos, Chao! :.Team GoS.:" + Style.RESET_ALL
    