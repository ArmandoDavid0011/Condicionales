# Ejericio 2

n1=int(input("Ingrese el primer valor: "))
n2=int(input("Ingrese el segundo valor: "))
n3=int(input("ingrese el tercer valor: "))

if n1>=2 and n1>=3:
    print(f"El primer valor es mayor: {n1}")
elif n2>=n1 and n2>=3:
    print(f"El segundo valor es mayor: {n2}")
elif n3>=n1 and n3>=n2:
    print(f"El tercer valor es mayor: {n3}")