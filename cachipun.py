import argparse
import random


cachipun = ["piedra","papel","tijeras"]
computer = random.choice(cachipun)
parser = argparse.ArgumentParser()
parser.add_argument("player_selection", help="Argumento inválido: Debe ser piedra, papel o tijera.", type=str)
player = (parser.parse_args().player_selection).lower()
if(player == "tijeras" or player == "papel" or player == "piedra"):
    print(f"Tu jugaste {player}")
    print(f"Computador jugó {computer}")
    if(player == computer):
        print("Es un empate")
    elif(player == "tijera" and computer == "piedra"):
        print("Perdiste")
    elif(player == "tijera" and computer == "papel"):
        print("Ganaste!!")
    elif(player == "piedra" and computer == "papel"):
        print("Perdiste")
    elif(player == "piedra" and computer == "tijeras"):
        print("Ganaste!!")
    elif(player == "papel" and computer == "tijeras"):
        print("Perdiste")
    elif(player == "papel" and computer == "piedra"):
        print("Ganaste!!")

else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")

