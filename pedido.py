from te import Te

Te.limpiar_pantalla()

sabor = int(input("""
Selecciona el sabor del té:
1 : Té Negro
2 : Té Verde
3 : Agua de hierbas

>>> """))

Te.limpiar_pantalla()

formato = int(input("Elige el formato: 300 ó 500 gramos:\n\n>>> "))

nombre, tiempo, recomendacion = Te.receta(sabor)

precio = Te.obtener_precio(formato)

Te.limpiar_pantalla()

print(f"""
Tu elección es la siguiente      
    
a. Sabor del tipo de té: {nombre}
b. Formato: {formato} gramos
c. Precio:  {precio} pesos
d. Tiempo:  {tiempo} minutos
e. Recomendación: {recomendacion}
f. Caduca en: {Te.caducidad} días

""")