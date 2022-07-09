
nombre = input("Dime cual es tu nombre: ")
ventas = int(input("Dime cuanto has vendido: "))
comision = ventas * 13 / 100
comision = round(comision,2)
print(f"Hola {nombre}, tus comisiones de este mes son: ${comision}")


