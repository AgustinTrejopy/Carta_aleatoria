import random
cartas = ["si", "no", "probablemente", "probablemente no", "no se"]
numero_carta = random.randint(0, 4)
pregunta = input("Hace tu pregunta: ")
print(cartas[numero_carta])