""" Un biólogo veterinario es el encargado de cuidar a los animales de un 
zoológico el posee su registro donde va el dato de cada animal por sus 
características y el área del zoológico donde se encuentran, cada cierto 
tiempo hace sus reportes donde enlista todos los animales del 
zoológico. 
Al ser veterinario se encarga también de la salud de los animales, 
por lo cual enlista aquellos que están en tratamiento, que dosis y 
cada cuanto tiempo se debe medicar a un animal """

class Animal:
    def __init__(self, nombre, especie, edad, sexo, ubicación):
        # Validaciones básicas de los atributos
        if not nombre or not especie or not sexo or not ubicación:
            raise ValueError("Todos los campos de nombre, especie, sexo y ubicación deben estar completos.")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")

        # Inicialización de atributos
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.sexo = sexo
        self.ubicación = ubicación
        self.tratamientos = []

    def agregar_tratamiento(self, tratamiento, dosis, frecuencia):
        # Agrega un tratamiento al animal
        if not tratamiento or not dosis or not frecuencia:
            raise ValueError("Los detalles del tratamiento, dosis y frecuencia no pueden estar vacíos.")
        self.tratamientos.append({"tratamiento": tratamiento, "dosis": dosis, "frecuencia": frecuencia})

    def __str__(self):
        # Representación del animal en formato de cadena
        return f"{self.nombre} ({self.especie}) - {self.edad} años, {self.sexo}, ubicado en {self.ubicación}"


class Zoológico:
    def __init__(self):
        self.animales = []  # Inicializa la lista de animales

    def agregar_animal(self, animal):
        # Verifica que solo se agreguen instancias de Animal
        if not isinstance(animal, Animal):
            raise TypeError("Solo se pueden agregar objetos de tipo Animal.")
        self.animales.append(animal)

    def obtener_animal(self, nombre):
        # Busca un animal por nombre
        for animal in self.animales:
            if animal.nombre.lower() == nombre.lower():
                return animal
        raise ValueError(f"No se encontró el animal '{nombre}'")

    def listar_animales(self):
        # Muestra todos los animales en el zoológico
        if not self.animales:
            print("No hay animales en el zoológico.")
        else:
            print("Listado de todos los animales en el zoológico:")
            for animal in self.animales:
                print(animal)

    def generar_informe(self):
        # Genera un informe de los animales en tratamiento
        informe = "Animales en tratamiento:\n"
        if not self.animales:
            informe += "No hay animales en el zoológico.\n"
        else:
            for animal in self.animales:
                if animal.tratamientos:
                    informe += f"- {animal.nombre} ({animal.especie}):\n"
                    for tratamiento in animal.tratamientos:
                        informe += f"  - {tratamiento['tratamiento']} ({tratamiento['dosis']} cada {tratamiento['frecuencia']})\n"
        return informe

    def alertas_tratamientos(self):
        # Genera alertas para tratamientos frecuentes
        for animal in self.animales:
            for tratamiento in animal.tratamientos:
                if tratamiento["frecuencia"] == "diaria":
                    print(f"Alerta: {animal.nombre} necesita {tratamiento['tratamiento']} hoy")
                elif tratamiento["frecuencia"] == "semanal":
                    print(f"Alerta: {animal.nombre} necesita {tratamiento['tratamiento']} esta semana")


def main():
    zoológico = Zoológico()  # Crea una instancia del zoológico

    while True:
        # Muestra el menú de opciones
        print("\nSeleccione una opción:")
        print("1. Agregar animal")
        print("2. Listar todos los animales")
        print("3. Agregar tratamiento a un animal")
        print("4. Ver informe de animales en tratamiento")
        print("5. Ver alertas de tratamientos")
        print("6. Salir")

        opción = input("Opción: ")

        try:
            if opción == "1":
                # Agrega un nuevo animal al zoológico
                nombre = input("Nombre del animal: ")
                especie = input("Especie del animal: ")
                edad = int(input("Edad del animal: "))
                sexo = input("Sexo del animal: ")
                ubicación = input("Ubicación del animal: ")

                animal = Animal(nombre, especie, edad, sexo, ubicación)
                zoológico.agregar_animal(animal)
                print("Animal agregado con éxito!")

            elif opción == "2":
                # Lista todos los animales
                zoológico.listar_animales()

            elif opción == "3":
                # Agrega tratamiento a un animal existente
                nombre = input("Nombre del animal a tratar: ")
                try:
                    animal = zoológico.obtener_animal(nombre)
                    tratamiento = input("Nombre del tratamiento: ")
                    dosis = input("Dosis del tratamiento: ")
                    frecuencia = input("Frecuencia del tratamiento (diaria/semanal): ")
                    animal.agregar_tratamiento(tratamiento, dosis, frecuencia)
                    print("Tratamiento agregado con éxito!")
                except ValueError as e:
                    print(e)

            elif opción == "4":
                # Muestra el informe de tratamientos
                print(zoológico.generar_informe())

            elif opción == "5":
                # Muestra las alertas de tratamientos
                zoológico.alertas_tratamientos()

            elif opción == "6":
               
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as e:
            print(f"Error de entrada: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
