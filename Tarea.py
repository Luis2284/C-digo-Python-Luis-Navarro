#Nombre: Luis Navarro Masson
#Grupo 81
#Programa Ingeniería Industrial 
#Codigo fuente: Autoria propia

# Diccionario con los precios de cada sector
precios = {
    'A': 15000,  # Norte alta
    'B': 13000,  # Norte baja
    'C': 10000,  # Oriental alta
    'D': 11000,  # Occidental alta
    'E': 20000   # Exclusivo
}

# Función para obtener un sector válido con depuración extra
def obtener_sector():
    while True:
        sector = input("Ingrese el sector (A, B, C, D, E): ")
        print(f"DEBUG: Sector ingresado antes de limpieza -> '{sector}'")  # Mostrar la entrada original

        # Limpiar la entrada de espacios y convertir a mayúsculas
        sector = sector.strip().upper()
        print(f"DEBUG: Sector después de limpieza -> '{sector}'")  # Mostrar después de limpiar

        if sector in precios:
            return sector
        else:
            print("❌ Error: Sector inválido. Intente de nuevo.")

# Función para obtener una cantidad válida de entradas
def obtener_cantidad():
    while True:
        try:
            cantidad = input("Ingrese la cantidad de entradas: ").strip()
            print(f"DEBUG: Cantidad ingresada -> '{cantidad}'")  # Depuración
            cantidad = int(cantidad)
            if cantidad > 0:
                return cantidad
            else:
                print("❌ Error: La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")

# Obtener datos del usuario
sector = obtener_sector()
cantidad = obtener_cantidad()

# Calcular total a pagar
precio_unitario = precios[sector]
total_pagar = precio_unitario * cantidad

# Mostrar resultados
print("\n🔹 **Resumen de Compra** 🔹")
print(f"📍 Sector elegido: {sector}")
print(f"💲 Precio unitario: ${precio_unitario:,.0f}")
print(f"🎟️ Cantidad de entradas: {cantidad}")
print(f"💰 Total a pagar: ${total_pagar:,.0f}")
