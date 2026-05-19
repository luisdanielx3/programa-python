#Matriz del Inventario
inventario = [
    ["01", "Cuadernos", 5, 15],
    ["02", "Lapices", 15, 15],
    ["03", "Borradores", 13, 15],
    ["04", "Marcadores", 12, 15],
    ["05", "Reglas", 2, 15],
    ["06", "Colores", 7, 15],
    ["07", "Tijeras", 4, 15],
    ["08", "Pegamento", 1, 15]
]
#Funcion para calcular cuanto se debe pedir de cada producto
print("Lista de Productos:")
for producto in inventario:
    nombre = producto[1]
    stock_actual = producto[2]
    stock_maximo = producto[3]
    cantidad_a_pedir = stock_maximo - stock_actual
    print(f"{nombre}: {cantidad_a_pedir} unidades a pedir")

