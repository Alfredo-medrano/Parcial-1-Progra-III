class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.productos = []
        self.ventas = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_compra(self, producto, cantidad):
        try:
            if producto in self.productos:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    self.ventas.append((producto, cantidad))
                    return True
                else:
                    raise ValueError("No hay suficiente cantidad del producto")
            else:
                raise ValueError("El producto no existe en la tienda")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    Ctotal = lambda self: sum(map(lambda x: x[0].precio * x[1], self.ventas))

    def dar_vuelto(self, pago):
        try:
            total = self.Ctotal()
            if pago < total:
                raise ValueError("No hay suficiente dinero para pagar")
            return pago - total
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def atender_proveedor(self, producto, cantidad, precio):
        try:
            if producto in self.productos:
                producto.cantidad += cantidad
                producto.precio = precio
            else:
                self.productos.append(Producto(producto, precio, cantidad))
        except Exception as e:
            print(f"Error: {e}")

def menu():
    print("Tienda de productos")
    print("1. Agregar producto")
    print("2. Realizar compra")
    print("3. Dar vuelto")
    print("4. Atender proveedor")
    print("5. Salir")

def main():
    tienda = Tienda()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            tienda.agregar_producto(Producto(nombre, precio, cantidad))
            print("Producto agregado con éxito")

        elif opcion == "2":
            print("Productos disponibles:")
            for i, producto in enumerate(tienda.productos):
                print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
            producto_seleccionado = int(input("Seleccione el producto que desea comprar: ")) - 1
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            tienda.realizar_compra(tienda.productos[producto_seleccionado], cantidad)
            print("Compra realizada con éxito")

        elif opcion == "3":
            pago = float(input("Ingrese el pago: "))
            print("Vuelto:", tienda.dar_vuelto(pago))

        elif opcion == "4":
            print("Productos disponibles:")
            for i, producto in enumerate(tienda.productos):
                print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
            producto_seleccionado = int(input("Seleccione el producto que desea atender: ")) - 1
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            tienda.atender_proveedor(tienda.productos[producto_seleccionado].nombre, cantidad, precio)
            print("Proveedor atendido con éxito")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()