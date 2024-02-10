# Subdomains-scanner
Una herramienta creada en python para la enumeracion de subdominios.

<h1> Recomendaciones </h1>

El script puede modificarse a gusto propio y es importante cambiar la ruta del archivo 
la cual lee el diccionario de subdominios

<h2> Uso del script </h2>

el script crea peticiones a http / https el cual solo tiene un argumento el cual es 
-t o --target y la direccion del dominio el cual eticamente se esta haciendo fuzzing a
los subdominios

ejemplo:

python3 Sdomains.py -t google.com
python3 Somains.py --target facebook.com
