num = int(input("Ingrese un numero: "))


def verifyNum():
    if num > 0:
        print("El numero es positivo")
    elif num == 0:
        print("El numero es cero")
    else:
        print("El numero es negativo")
    
    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
verifyNum()