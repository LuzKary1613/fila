import os
import csv

def calcular_estadisticas(clientes):
    total_clientes = len(clientes)
    tiempo_espera_promedio = sum(cliente['Tiempo Espera'] for cliente in clientes) / total_clientes
    probabilidad_espera = sum(1 for cliente in clientes if cliente['Tiempo Espera'] > 0) / total_clientes
    tiempo_cajero_inactivo = sum(cliente['Tiempo Espera'] for cliente in clientes if cliente['Tiempo Espera'] > 0)
    porcentaje_cajero_inactivo = (tiempo_cajero_inactivo / sum(cliente['Tiempo Tramite'] for cliente in clientes)) * 100
    tiempo_servicio_promedio = sum(cliente['Tiempo Tramite'] for cliente in clientes) / total_clientes
    return tiempo_espera_promedio, probabilidad_espera, porcentaje_cajero_inactivo, tiempo_servicio_promedio

def main():
    escritorio = os.path.expanduser("~/Desktop")

    archivo_csv = os.path.join(escritorio, "resultados.csv")

    clientes = []

    with open(archivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cliente = {
                'Cliente': int(row['cliente']),
                'Hora Llegada': float(row['hora de llegada']),
                'Hora Inicio Trámite': float(row['inicia servicio']),
                'Hora Finalización': float(row['termina servicio ']),
                'Tiempo Espera': float(row['tiempo espera']),
                'Tiempo Tramite': float(row['tiempo inactividad del ATM ']),
            }
            clientes.append(cliente)

    tiempo_espera_promedio, probabilidad_espera, porcentaje_cajero_inactivo, tiempo_servicio_promedio = calcular_estadisticas(clientes)

    print(f"Tiempo de espera promedio por cliente: {tiempo_espera_promedio}")
    print(f"Probabilidad de que un cliente espera en la fila: {probabilidad_espera}")
    print(f"Porcentaje de tiempo en que el ATM estuvo inactivo: {porcentaje_cajero_inactivo}%")
    print(f"Tiempo promedio de servicio: {tiempo_servicio_promedio}")

if __name__ == "__main__":
    main()
