#Ejercicio 4 "Simulación de un cajero"

saldo=2000
print("1. Ingresar Dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. salir")

seleccion = int(input("¿Que operación deseas realizar?: "))

if seleccion==1:
    ingreso = float(input("Ingresar dinero: "))
    saldo+=ingreso
    print(f"Saldo nuevo: {saldo}")
elif seleccion==2:
    salida = float(input("Retirar dinero: "))
    if salida>saldo:
        print("Saldo insuficiente: ")
    else:
        saldo-=salida
        print(f"Nuevo saldo disponible: {saldo}")
elif seleccion==3:
    print(f"Saldo disponible: {saldo}")
elif seleccion==4: 
    print("Usted ha deseado salir")
else:
    print("Error de operacion")