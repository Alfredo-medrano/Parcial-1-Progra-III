""" Una tienda local vende diversos productos, cada vez que un cliente 
hace una compra niña mary se encarga de anotarlo en una libreta. A su 
vez, con una calculadora le da el total a cada cliente y les da su 
respectivo vuelto en caso de necesitarlo. 
 Niña mary también se encarga de atender a los proveedores que 
le dan cierta cantidad de producto y un precio sugerido de venta, 
propón una solución dentro de tu programa para ayudarle. """

class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Constructor para inicializar los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        # Inicializa las listas de productos y ventas
        self.productos = []
        self.ventas = []

    def agregar_producto(self, producto):
        # Agrega un nuevo producto a la tienda
        self.productos.append(producto)

    def realizar_compra(self, producto, cantidad):
        try:
            # Verifica si el producto existe en la tienda
            if producto in self.productos:
                # Verifica si hay suficiente cantidad del producto
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad  # Reduce la cantidad del producto
                    self.ventas.append((producto, cantidad))  # Registra la venta
                    return True
                else:
                    # Lanza una excepción si no hay suficiente cantidad
                    raise ValueError("No hay suficiente cantidad del producto")
            else:
                # Lanza una excepción si el producto no existe
                raise ValueError("El producto no existe en la tienda")
        except ValueError as e:
            # Muestra un mensaje de error en caso de excepción
            print(f"Error: {e}")
            return False

    # Calcula el total de ventas utilizando una función lambda
    Ctotal = lambda self: sum(map(lambda x: x[0].precio * x[1], self.ventas))

    def dar_vuelto(self, pago):
        try:
            total = self.Ctotal()  # Obtiene el total de ventas
            if pago < total:
                # Lanza una excepción si el pago es insuficiente
                raise ValueError("No hay suficiente dinero para pagar")
            return pago - total  # Calcula el vuelto
        except ValueError as e:
            # Muestra un mensaje de error en caso de excepción
            print(f"Error: {e}")
            return None

    def atender_proveedor(self, producto, cantidad, precio):
        try:
            # Verifica si el producto ya existe en la tienda
            if producto in self.productos:
                producto.cantidad += cantidad  # Actualiza la cantidad del producto
                producto.precio = precio  # Actualiza el precio del producto
            else:
                # Agrega un nuevo producto si no existe
                self.productos.append(Producto(producto, precio, cantidad))
        except Exception as e:
            # Muestra un mensaje de error en caso de excepción
            print(f"Error: {e}")

def menu():
    
    print("Tienda de productos")
    print("1. Agregar producto")
    print("2. Realizar compra")
    print("3. Dar vuelto")
    print("4. Atender proveedor")
    print("5. Salir")

def main():
    tienda = Tienda()  # Crea una instancia de Tienda

    while True:
        menu()  # Muestra el menú al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Permite agregar un nuevo producto a la tienda
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            tienda.agregar_producto(Producto(nombre, precio, cantidad))
            print("Producto agregado con éxito")

        elif opcion == "2":
            # Permite realizar una compra
            print("Productos disponibles:")
            for i, producto in enumerate(tienda.productos):
                print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
            producto_seleccionado = int(input("Seleccione el producto que desea comprar: ")) - 1
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            tienda.realizar_compra(tienda.productos[producto_seleccionado], cantidad)
            print("Compra realizada con éxito")

        elif opcion == "3":
            # Calcula y muestra el vuelto al cliente
            pago = float(input("Ingrese el pago: "))
            print("Vuelto:", tienda.dar_vuelto(pago))

        elif opcion == "4":
            # Permite atender al proveedor y actualizar o agregar productos
            print("Productos disponibles:")
            for i, producto in enumerate(tienda.productos):
                print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
            producto_seleccionado = int(input("Seleccione el producto que desea atender: ")) - 1
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            tienda.atender_proveedor(tienda.productos[producto_seleccionado].nombre, cantidad, precio)
            print("Proveedor atendido con éxito")

        elif opcion == "5":
            # Finaliza el programa
            print("Saliendo...")
            break

        else:
            # Muestra un mensaje en caso de opción inválida
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main() 
    
    
