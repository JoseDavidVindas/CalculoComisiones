nombre = input("Cúal es su nombre: ")
ventas = int(input("Digite el numero de ventas totales en el mes: "))
comision = round(ventas * 13 / 100,2)
print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
