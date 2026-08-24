print("================================")
print("     SISTEMA DE INVENTARIO")
print("================================")

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio: "))

print("\n--- INFORMACIÓN DEL PRODUCTO ---")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio: $", precio)

total = cantidad * precio

print("Valor total:", total)