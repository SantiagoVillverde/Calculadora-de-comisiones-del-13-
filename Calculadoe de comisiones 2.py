
nombre = input("Dime cual es tu nombre: ")
ventas = int(input("Dime cuanto has vendido: "))
comision = int(input("Dime cual es el monto de tu comision:"))
comisionfinal = round(ventas * comision / 100,2)

print(f"Hola {nombre}, tus comisiones de este mes son: ${comisionfinal}")


