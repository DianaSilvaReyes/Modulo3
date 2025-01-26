# Clase para representar un conductor
class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  

# Clase para representar un bus
class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None 
        self.horarios = []  
        self.conductor = None  

# Clase administrativa para manejar buses y conductores
class Admin:
    def __init__(self):
        self.buses = []  
        self.conductores = [] 

    def agregar_bus(self, id_bus):
        bus = Bus(id_bus)
        self.buses.append(bus)
        print(f"Bus con ID {id_bus} agregado correctamente.")

    def agregar_ruta_a_bus(self, id_bus, ruta):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                bus.ruta = ruta
                print(f"Ruta '{ruta}' asignada al bus {id_bus}.")
                return
        print(f"No se encontró el bus con ID {id_bus}.")

    def registrar_horario_a_bus(self, id_bus, horario):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                if horario not in bus.horarios:
                    bus.horarios.append(horario)
                    print(f"Horario {horario} registrado al bus {id_bus}.")
                else:
                    print(f"El bus {id_bus} ya tiene el horario {horario} asignado.")
                return
        print(f"No se encontró el bus con ID {id_bus}.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado correctamente.")

    def agregar_horario_a_conductor(self, nombre, horario):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                if horario not in conductor.horarios:
                    conductor.horarios.append(horario)
                    print(f"Horario {horario} asignado al conductor {nombre}.")
                else:
                    print(f"El conductor {nombre} ya tiene el horario {horario} asignado.")
                return
        print(f"No se encontró el conductor {nombre}.")

    def asignar_bus_a_conductor(self, id_bus, nombre_conductor, horario):
        # Buscar el bus
        bus = next((b for b in self.buses if b.id_bus == id_bus), None)
        if not bus:
            print(f"No se encontró el bus con ID {id_bus}.")
            return

        # Buscar el conductor
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)
        if not conductor:
            print(f"No se encontró el conductor {nombre_conductor}.")
            return

        # Validar si el conductor ya tiene ese horario ocupado
        if horario in conductor.horarios:
            print(f"El conductor {nombre_conductor} ya tiene el horario {horario} ocupado.")
            return

        # Validar si el bus ya tiene ese horario ocupado
        if horario in bus.horarios:
            print(f"El bus {id_bus} ya tiene el horario {horario} ocupado.")
            return

        # Asignar bus al conductor y horario
        bus.conductor = conductor
        bus.horarios.append(horario)
        conductor.horarios.append(horario)
        print(f"Bus {id_bus} asignado al conductor {nombre_conductor} en el horario {horario}.")

# Función principal para el menú
admin = Admin()

def menu():
    while True:
        print("\n....Menú de Gestión de Buses.....")
        print("1. Agregar Bus")
        print("2. Agregar Ruta a Bus")
        print("3. Registrar Horario a Bus")
        print("4. Agregar Conductor")
        print("5. Agregar Horario a Conductor")
        print("6. Asignar Bus a Conductor")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_bus = input("Ingresa el ID del bus: ")
            admin.agregar_bus(id_bus)
        elif opcion == "2":
            id_bus = input("Ingresa el ID del bus: ")
            ruta = input("Ingresa la ruta: ")
            admin.agregar_ruta_a_bus(id_bus, ruta)
        elif opcion == "3":
            id_bus = input("Ingresa el ID del bus: ")
            horario = input("Ingresa el horario (ejemplo: 8:00): ")
            admin.registrar_horario_a_bus(id_bus, horario)
        elif opcion == "4":
            nombre = input("Ingresa el nombre del conductor: ")
            admin.agregar_conductor(nombre)
        elif opcion == "5":
            nombre = input("Ingresa el nombre del conductor: ")
            horario = input("Ingresa el horario (ejemplo: 8:00): ")
            admin.agregar_horario_a_conductor(nombre, horario)
        elif opcion == "6":
            id_bus = input("Ingresa el ID del bus: ")
            nombre_conductor = input("Ingresa el nombre del conductor: ")
            horario = input("Ingresa el horario (ejemplo: 8:00): ")
            admin.asignar_bus_a_conductor(id_bus, nombre_conductor, horario)
        elif opcion == "7":
            print("Que tengas buen día. ADIÓS :)")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
