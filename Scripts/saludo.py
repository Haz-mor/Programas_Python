import argparse
import random


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--saludo", type=str, default="")
args = parser.parse_args()
saludo = args.saludo
if saludo == "Hola":
    num = random.randint(0, 100)
    if num <= 50:
        print("Hola, cómo estas")
    elif num <= 75:
        print('Hola, me llamo Computina')
    else:
        print("Háblale a la mano")
else:
    print("Primero, saluda!!")
