import math as ma
import argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("weight", type=float)
parser.add_argument("height", type=float)
args = parser.parse_args()
user_weight = args.weight
user_height = (args.height)/100

print("Aplicacion que calcula su Indice de Masa Corporal IMC.\nLos datos entregados se mantendran de forma confidencial ")

imc = user_weight/(user_height**2)
user_clasification = "Bajo Peso"
if(imc < 18.5):
    user_clasification = "Bajo Peso"

elif(imc < 25):
    user_clasification = "Adecuado"
elif(imc < 30):
    user_clasification = "Sobrepeso"
    
elif(imc < 35):
    user_clasification = "Obesidad Grado I"

elif(imc < 40):
    user_clasification = "Obesidad Grado II"
else:
    user_clasification = "Obesidad Grado III"


print(f"---------------------------------------------\nPara un peso de {user_weight}[kg] y una altura de {user_height}[m], su IMC es : {imc:.2f}[kg/m2]")
print(f"---------------------------------------------\nSegun la OMS la clasificacion para su IMC es : {user_clasification}")
