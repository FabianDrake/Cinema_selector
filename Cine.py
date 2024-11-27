print("Bienvenido a tu cine favorito!!")

def mostrar_asientos(asientos):
    for fila in asientos:
        print(" ".join(fila))

def elegir_asiento(asientos, fila, columna):
    if asientos[fila][columna] == "O":
        asientos[fila][columna] = "X"
        return True
    else:
        return False

def main():
    filas = 5
    columnas = 5
    asientos = [["O" for _ in range(columnas)] for _ in range(filas)]
    
    while True:
        mostrar_asientos(asientos)
        fila = int(input("Elige una fila (0-4): "))
        columna = int(input("Elige una columna (0-4): "))
        
        if elegir_asiento(asientos, fila, columna):
            print("Asiento reservado con éxito.")
        else:
            print("Asiento ya está ocupado. Elige otro asiento.")
        
        continuar = input("¿Quieres reservar otro asiento? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
