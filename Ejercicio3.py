# Ejercicio 3 if
"""
nombre1=input("nombre 1: ")
nombre2=input("nombre 2: ")
if nombre1==nombre2:
    print("Son Similares")
    print("Sigue asi bb tu puedes mi amor")
elif nombre1!=nombre2:
    print("Son pendejos xd")
    print("Como eres pendejo ni escribir nombre sabes")
"""
nombre1=input("Nombre 1: ")
nombre2=input("Nombre 2: ")
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia")
