import random
import os

def read_data():
    with open("./data.txt", "r", encoding="utf-8") as f:
        datos = [line.strip("\n") for line in f]

    dict_datos = {key:value for key, value in enumerate(datos)}
    return dict_datos

def normalize(s): # It removes the accents of a string
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),)

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def run():
    try:
        dict_datos = read_data()
        palabra_adivinar = normalize(dict_datos.get(random.randint(1,len(dict_datos)+1)))
        palabra_adivinando = len(palabra_adivinar)*"_"
        print("""¡Bienvenido al juego del ahorcado! \nAdivina la siguiente palabra:""")

        while palabra_adivinar != palabra_adivinando:
            print(palabra_adivinando)
            letra = normalize(input("ingresa una lera: "))
            if letra in palabra_adivinar:
                palabra_adivinando = list(palabra_adivinando)
                for i, x in enumerate(palabra_adivinar):
                    if x == letra:
                        palabra_adivinando[i] = x
                palabra_adivinando = "".join(palabra_adivinando)
            os.system("cls")
        print(f"¡Ganaste! tu palabra era {palabra_adivinando}")

        volver_jugar = int(input("¿Quieres jugar nuevamente?: \n1. Si\n2. No\n"))
        if volver_jugar == 1:
            run()
        else:
            print("Adiós :)")

    except ValueError:
        print("Solos debes ingresar letras")

if __name__ == "__main__":
    run()