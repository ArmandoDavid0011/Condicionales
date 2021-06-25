# Ejercicio 1 Condicionales if

n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo Valor:"))

if n1%2==0 and n2%2==0:
    print("Ambos valores son pares")
elif n1%2==0 and n2%2!=-0:
    print(f"{n1} es un valor pares")

elif n1%2==0 and n2%2==-0:
    print(f"{2} Es un valor par")
else:
    print("Ambos valores son impares")