# Una biblioteca ofrece prestamos a usuarios mediante una tarjeta de prestamo, el sitema debe tomar los
# datos, se debe registrar la fecha de retiro y devolución del libro y el nombre del libro.


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

class Tarjeta:
    def __init__(self, nombre_persona):
        self.nombre_persona = nombre_persona
        self.libros_prestados = {}

    def prestar_libro(self, libro, dias_prestamo):
        if not libro.prestado:
            fecha_prestamo = self.obtener_fecha()
            fecha_devolucion = fecha_prestamo + dias_prestamo
            self.libros_prestados[libro.titulo] = (fecha_prestamo, fecha_devolucion)
            libro.prestado = True
            print(f"Libro '{libro.titulo}' prestado. Fecha de devolución: {fecha_devolucion}")
        else:
            print(f"El libro '{libro.titulo}' ya está prestado.")

    def devolver_libro(self, libro):
        if libro.titulo in self.libros_prestados:
            fecha_prestamo, fecha_devolucion = self.libros_prestados[libro.titulo]
            fecha_actual = self.obtener_fecha()

            if fecha_actual > fecha_devolucion:
                dias_retraso = fecha_actual - fecha_devolucion
                print(f"Devolución tardía. Sanción aplicada por {dias_retraso} días de retraso. Por cada día de retraso se cobrará $1.00")
            else:
                print(f"Libro '{libro.titulo}' devuelto a tiempo.")

            libro.prestado = False
            del self.libros_prestados[libro.titulo]
        else:
            print(f"El libro '{libro.titulo}' no estaba prestado por esta tarjeta.")

    def obtener_fecha(self):
       
        return int(input("Introduce el número de días (1, 2, 3, ...): "))

libro1 = Libro("El Quijote")
tarjeta = Tarjeta("Juan Pérez")

tarjeta.prestar_libro(libro1, 7)  # Préstamo por 7 días
tarjeta.devolver_libro(libro1)    # Devolución del libro


#En este codigo usamos un contador para representar las fechas, por ejemplo el dia 1 
# representa el primer dia, el dia 3, son los 3 dias, etc, implementamos la sección de devolución así
# aplicará su sanción, agregamos un enunciado adicional que por cada día de retraso se aplicara un 
# cobro de $1.00. 