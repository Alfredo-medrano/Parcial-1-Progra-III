# El consultorio necesita registrar las consultas de los pacientes, la secretaria debe asignarle
# a cada paciente que sea registrado su nombre, motivo de su consulta y su fecha para su cita,
# Si el paciente ya tiene una consulta previa, el programa debe dirigirlo a la sala de espera.

class Paciente:
    def __init__(self, doctor, nombre, consulta, fecha):
        self.doctor = doctor
        self.nombre = nombre
        self.consulta = consulta
        self.fecha = fecha

    def __str__(self):
        return (f"Nombre del Paciente: {self.nombre}\n"
                f"Motivo de la consulta: {self.consulta}\n"
                f"Fecha de la consulta: {self.fecha}\n"
                f"Doctor programado: {self.doctor}\n")
class Fecha:
    def __init__(self, doctor):
        self.doctor = doctor
        self.fechas = []

    def agregar(self, paciente):
        # Aquí verificamos si el paciente ya tiene una consulta ya programada.
        for registro in self.fechas:
            if registro.nombre == paciente.nombre:
                print(f"El paciente {paciente.nombre} ya tiene una consulta previa.")
                print("Se le pasará a sala de espera.")
                return
        self.fechas.append(paciente)
        print(f"Consulta registrada para {paciente.nombre}.")

    def mostrar(self):
        print("***Registro De Consultas***")
        for paciente in self.fechas:
            print(paciente)


doctorl = input("Bienvenido, ingrese el nombre del doctor programado: ")
fechl = Fecha(doctorl)

while True:
    npaciente = input("Ingrese el nombre del paciente: ")
    cpaciente = input("Ingrese el motivo de la consulta: ")
    fpaciente = input("Ingrese la fecha de la consulta: ")
    paciente = Paciente(doctorl, npaciente, cpaciente, fpaciente)

    fechl.agregar(paciente)

    op = input("¿Desea ingresar nuevo paciente? (s/n): ")
    if op.lower() == 'n':
        fechl.mostrar()
        break

# En este codigo lo diseñamos para gestionar los datos con el objetivo de suplir las necesidades del 
# consultorio registrando cada paciente.
# Para evitar duplicar datos de paciente con la misma fecha de consulta implementamos una funcion
# que detecta si el paciente ya tiene una fecha previa y asi mandarlo directo a sala de espera.
