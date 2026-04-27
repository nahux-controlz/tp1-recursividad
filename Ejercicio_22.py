def usar_la_fuerza(mochila, objetos_sacados=0):
    # si la mochila esta vacia, cortamos (caso base)
    if len(mochila) == 0:
        return False, objetos_sacados
    
    # sacamos el primer elemento para mirarlo
    item = mochila[0]
    
    # si es el sable, joya, devolvemos true y sumamos 1 al contador
    if item == "sable de luz":
        return True, objetos_sacados + 1
        
    # si no es, la funcion se llama a si misma pero le pasa 
    # la mochila sin el objeto que acabamos de sacar (con mochila[1:])
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)


# armamos el vector (lista) para el punto C
mochila_jedi = ["raciones", "binoculares", "transmisor", "sable de luz", "capa"]
mochila_falsa = ["piedra", "cantimplora"]

# probamos a ver si funciono
encontrado, cant = usar_la_fuerza(mochila_jedi)

print("Buscando en la mochila de Luke...")
if encontrado:
    print(f"Sable encontrado. Se sacaron {cant} objetos.")
else:
    print(f"No hay sable. Se vacio la mochila sacando {cant} objetos.")