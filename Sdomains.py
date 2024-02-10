import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='Indica el dominio de la victima') # argumento para la url
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('Subdominios.txt'): # Comprobacion que existe un archivo en la ruta especificada 
            wordlist = open('Subdominios.txt','r')
            wordlist = wordlist.read().split('\n')
            
            for subdominio in wordlist: # enumeracion de subdominios en http
                url = "http://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio encontrado.. " + url)
                    
            for subdominio in wordlist: # Enumeracion de subdominios en https
                url = "https://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio encontrado.. " + url)
                    
    else: # comprobacion del dominio
        print("(!) Ingresa un dominio")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: # El programa finaliza haciendo ctrl + c
        sys.exit()
