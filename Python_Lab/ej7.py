name = input("Ingresar su nombre ")
age = int(input("Ingresar su edad "))
city = input("Ingresar ciudad de residencia ")

def User():
    birth = str((2025 - age))
    print("Vivis en: " + city)
    print("Hola, " + name, "Tu año de nacimiento es: " + birth)
    if age >= 18 and age%5==0:
        print("Hola, " + name, "Tienes mas de 18 años y tu edad es multiplo de 5")
    elif age >= 18 and age%5!=0:
        print("Hola, " + name, "Tienes mas de 18 años y tu edad NO es multiplo de 5")
    else:
        print("Hola, " + name, "No Tienes mas de 18 años y tu edad NO es multiplo de 5")
User()