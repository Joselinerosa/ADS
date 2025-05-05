import sys

class CarnetPuntos:  # O(1)
    def __init__(self):
        self.conductores = {}  # Dictionary to store drivers and their points
        self.puntos_count = {i: 0 for i in range(16)}  # O(1) initialization

    def nuevo(self, dni):  # O(1)
        if dni in self.conductores:
            raise ValueError("Conductor duplicado")
        self.conductores[dni] = 15
        self.puntos_count[15] += 1

    def quitar(self, dni, puntos):  # O(1)
        if dni not in self.conductores:
            raise ValueError("Conductor inexistente")
        puntos_actuales = self.conductores[dni]
        self.puntos_count[puntos_actuales] -= 1
        nuevos_puntos = max(0, puntos_actuales - puntos)
        self.conductores[dni] = nuevos_puntos
        self.puntos_count[nuevos_puntos] += 1

    def consultar(self, dni):  # O(1)
        if dni not in self.conductores:
            raise ValueError("Conductor inexistente")
        return self.conductores[dni]

    def cuantos_con_puntos(self, puntos):  # O(1)
        if puntos < 0 or puntos > 15:
            raise ValueError("Puntos no validos")
        return self.puntos_count[puntos]

def main():
    if len(sys.argv) != 2:
        print("Usage: python Drivers.py <input_file>")
        return

    input_file = sys.argv[1]
    carnet = CarnetPuntos()

    try:
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line == "FIN":
                    # Print the final ---
                    print("---")
                    carnet = CarnetPuntos()  # Reset carnet for the next session
                    continue

                parts = line.split()
                op = parts[0]

                try:
                    if op == "nuevo":
                        carnet.nuevo(parts[1])
                    elif op == "quitar":
                        carnet.quitar(parts[1], int(parts[2]))
                    elif op == "consultar":
                        print(f"Puntos de {parts[1]}: {carnet.consultar(parts[1])}")
                    elif op == "cuantos_con_puntos":
                        print(f"Con {parts[1]} puntos hay {carnet.cuantos_con_puntos(int(parts[1]))}")
                    else:
                        raise ValueError("Operación no válida")
                except ValueError as e:
                    print(f"ERROR: {e}")

    except FileNotFoundError:
        print(f"ERROR: No se pudo abrir el archivo '{input_file}'")

if __name__ == "__main__":
    main()

