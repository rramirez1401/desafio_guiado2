from te import Te

Te.limpiar_pantalla()  ## Limpiar pantalla


## solicito el saor del té con un input
sabor = int(input("""
Selecciona el sabor del té:
1 : Té Negro
2 : Té Verde
3 : Agua de hierbas

>>> """))

Te.limpiar_pantalla()  ## Limpiar pantalla


## solicito el formato del té
formato = int(input("Elige el formato: 300 ó 500 gramos:\n\n>>> "))


## LLamamos al método estático "receta" de la clase "Te" para obtener el nombre, el tiempo y la recomendación del té
nombre, tiempo, recomendacion = Te.receta(sabor)

## LLamamos al método estático "obtener_precio" de la clase "Te" para obtener el precio según el formato
precio = Te.obtener_precio(formato)

Te.limpiar_pantalla()  ## Limpiar pantalla


## Imprimo en pantalla el resultado del pedido
print(f"""
Tu elección es la siguiente      
    
a. Sabor del tipo de té: {nombre}
b. Formato: {formato} gramos
c. Precio:  {precio} pesos
d. Tiempo:  {tiempo} minutos
e. Recomendación: {recomendacion}
f. Caduca en: {Te.caducidad} días

""")