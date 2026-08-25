import json

ARCHIVO = "inventario.json"


def cargar_inventario():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_inventario(inventario):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


print("================================")
print("     SISTEMA DE INVENTARIO")
print("================================")

inventario = cargar_inventario()

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

guardar_inventario(inventario)

print("\n================================")
print("       INVENTARIO COMPLETO")
print("================================")

for producto in inventario:
    print("\nProducto:", producto["producto"])
    print("Cantidad:", producto["cantidad"])
    print("Precio: $", producto["precio"])
    print("Valor total: $", producto["total"])

print("\nInventario guardado correctamente.")
