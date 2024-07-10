import random
import statistics
import math
import csv


trabajadores = ["Juan rollroyce", "María Gastañeda", "Carlos lore", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
   ]

sueldos = []

#" ASIGANAR SUELDOS ALEATORIOS A LOS TRABAJADORES"
def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]

    print("Sueldos asignados correctamente.")
    
# FUNCION PARA CLASIFICAR SUELDOS
def clasificar_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return

    menores_800k = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo < 800000]
    entre_800k_2m = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if 800000 <= sueldo <= 2000000]
    mayores_2m = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo > 2000000]

    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(menores_800k)}")
    for trabajador, sueldo in menores_800k:
        print(f"{trabajador}: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800k_2m)}")
    for trabajador, sueldo in entre_800k_2m:
        print(f"{trabajador}: ${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(mayores_2m)}")
    for trabajador, sueldo in mayores_2m:
        print(f"{trabajador}: ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

#" FUNCION PARA VER ESTADISTICAS DE TRABAJADORES"
def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return

    maximo = max(sueldos)
    minimo = min(sueldos)
    promedio = statistics.mean(sueldos)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    
    print(f"Sueldo más alto: ${maximo}")
    print(f"Sueldo más bajo: ${minimo}")
    print(f"Promedio de sueldos: ${promedio}")
    print(f"Media geométrica: ${media_geometrica:.2f}")

#" CREAR FUNCION PARA REPORTE DE SUELDOS"
def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return

    descuentos_salud = [sueldo * 0.07 for sueldo in sueldos]
    descuentos_afp = [sueldo * 0.12 for sueldo in sueldos]
    sueldos_liquidos = [sueldo - descuento_salud - descuento_afp for sueldo, descuento_salud, descuento_afp in zip(sueldos, descuentos_salud, descuentos_afp)]

    print("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido in zip(trabajadores, sueldos, descuentos_salud, descuentos_afp, sueldos_liquidos):
            writer.writerow({'Nombre empleado': trabajador, 'Sueldo Base': sueldo, 'Descuento Salud': descuento_salud, 'Descuento AFP': descuento_afp, 'Sueldo Líquido': sueldo_liquido})
            print(f"{trabajador}, ${sueldo}, ${descuento_salud}, ${descuento_afp}, ${sueldo_liquido}")

    print("\nReporte generado correctamente y guardado en 'reporte_sueldos.csv'.")


#"CREAR MENU PARA INICIAR PROGRAMA"
def menu():
    while True:
        print("Menú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("Finalizando programa…")
            print("Desarrollado por Italo Ortega")
            print("RUT 20.888.802.1")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
