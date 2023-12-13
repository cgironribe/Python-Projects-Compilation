"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"] """

def obtener_valores(enlace):
    cut_link = enlace.split("?")
    url, params = cut_link
    dict = {}

    for par in params.split("&"):
        split_params = par.split("=")
        key, value = split_params
        dict[key] = value
    return dict

check = obtener_valores("https://retosdeprogramacion.com?year=2023&challenge=0")
print(check)