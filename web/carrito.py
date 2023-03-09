# Clase carrito
class Cart:
    # se le pasara el request a esta clase
    def __init__(self, request):
        self.request = request
        # obtener la session del navegador
        self.session = request.session
        # tienes una variable session llamada cart, para obtener el valor de dicha variable => session.get("cart")
        cart = self.session.get("cart")
        montoTotal = self.session.get("cartMontoTotal")
        # si no existe la variable session llamado cart
        if not cart:
            # crear una variable session llamado cart => elf.session['cart']
            cart = self.session['cart'] = {}
            montoTotal = self.session["cartMontoTotal"] = "0"

        self.cart = cart
        self.montoTotal = float(montoTotal)

    # adicionar
    def add(self, producto, cantidad):
        if str(producto.id) not in self.cart.keys():
            # Si el id del producto no se encuentra dentro de las claves
            # clave del diccionario es el id del producto.
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": cantidad,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "categoria": producto.categoria.nombre,
                "subtotal": str(cantidad * producto.precio)
            }
        else:
            # si encuentra el producto
            # actualizamos el producto en el carrito
            for key, value in self.cart.items():
                # si encuentra el producto id
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + cantidad)
                    value["subtotal"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break

        self.save()

    # eliminar
    def delete(self, producto):
        producto_id = str(producto.id)
        # consulta si existe
        if producto_id in self.cart:
            del self.cart[producto_id]
            # para que se actualice el carrito
            self.save()

    # limpias el carrito
    def clear(self):
        self.session["cart"] = {}
        self.session["cartMontoTotal"] = "0"

    # para grabar lo que haces(cambios) en el carrito de compra
    def save(self):
        montoTotal = 0

        for key, value in self.cart.items():
            # sumando todos los subtotales
            montoTotal += float(value["subtotal"])
        # asigna el nuevo monto total de la session
        self.session["cartMontoTotal"] = montoTotal
        # actualizar el carrito de compras
        self.session["cart"] = self.cart
        # variable session modificable
        self.session.modified = True




