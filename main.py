from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas

def listar_citas(citas: list):
    print("\n--- LISTADO DE CITAS MÉDICAS ---")
    if not citas:
        print("No hay citas registradas actualmente.")
        return
    
    for c in citas:
        tipo = "Urgencia" if c["es_urgencia"] else "Programada"
        print(f"ID: {c['id_cita']} | Paciente: {c['paciente']} | Especialidad: {c['especialidad']} "
              f"| Fecha: {c['fecha']} | Tipo: {tipo} | Costo Final: ${c.get('costo_final', c['costo_consulta']):,.2f}")

def registrar_cita(citas: list):
    print("\n--- REGISTRAR NUEVA CITA ---")
    id_cita = input("Ingrese el ID de la cita: ").strip()
    
    # Validación de ID único
    if any(cita["id_cita"] == id_cita for cita in citas):
        print("\n[Error] Ya existe una cita registrada con ese ID.")
        return

    paciente = input("Nombre del paciente: ").strip()
    especialidad = input("Especialidad médica: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    
    try:
        costo_consulta = float(input("Costo base de la consulta: "))
    except ValueError:
        print("\n[Error] El costo debe ser un valor numérico.")
        return

    urgencia_input = input("¿Es una cita de urgencia? (s/n): ").strip().lower()
    es_urgencia = urgencia_input == "s"

    nueva_cita = CitaMedica(id_cita, paciente, especialidad, fecha, costo_consulta, es_urgencia)
    citas.append(nueva_cita.a_diccionario())
    
    if guardar_citas(citas):
        print("\n¡Cita registrada y guardada exitosamente!")

def consultar_total_ingresos(citas: list):
    print("\n--- TOTAL DE INGRESOS PROYECTADOS ---")
    if not citas:
        print("No hay citas registradas para calcular ingresos.")
        return
    
    total = sum(c.get("costo_final", c["costo_consulta"]) for c in citas)
    print(f"El ingreso total proyectado es: ${total:,.2f}")

def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN MEDISENA ===")
        print("1. Listar citas")
        print("2. Registrar nueva cita")
        print("3. Consultar total de ingresos proyectados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        citas = cargar_citas()

        if opcion == "1":
            listar_citas(citas)
        elif opcion == "2":
            registrar_cita(citas)
        elif opcion == "3":
            consultar_total_ingresos(citas)
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()