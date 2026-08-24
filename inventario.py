print("================================")
print("     SISTEMA DE INVENTARIO")
print("================================")

inventario = []

cantidad_productos = int(input("¿Cuántos productos desea ingresar? "))

for i in range(cantidad_productos):
    print(f"\n--- PRODUCTO {i + 1} ---")

    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    total = cantidad * precio

    inventario.append({
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "total": total
    })

print("\n================================")
print("       INVENTARIO COMPLETO")
print("================================")

for producto in inventario:
    print("\nProducto:", producto["producto"])
    print("Cantidad:", producto["cantidad"])
    print("Precio: $", producto["precio"])
    print("Valor total: $", producto["total"])