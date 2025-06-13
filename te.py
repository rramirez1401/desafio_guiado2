import os

class Te :
    caducidad = 365

    sabores = {
        1 : {"nombre"        : "Té negro",
             "tiempo"        : 3,
             "recomendacion" : "Desayuno"},
        2 : {"nombre"        : "Té verde",
             "tiempo"        : 5,
             "recomendacion" : "Mediodia"},
        3 : {"nombre"        : "Agua de hierbas",
             "tiempo"        : 6,
             "recomendacion" : "Once"}
    }

    precios = {
        300 : 3000,
        500 : 5000 
    }

    @staticmethod
    def receta(sabor:int):
        ## Retorna el tiempo de preparacion en min y recomendacion de uso

        pedido = Te.sabores[sabor]
        return pedido["nombre"], pedido["tiempo"], pedido["recomendacion"]

    @staticmethod
    def obtener_precio(formato:int):
        ## Retorna el precio segun el formato indicado

        return Te.precios[formato]
    
    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

