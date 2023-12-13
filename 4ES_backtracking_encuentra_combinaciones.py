"""
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)"""

def find_combinations(nums, target):
    result = []  

    def backtrack(start, target, current_combination):
        if target == 0:
            # Si el objetivo se ha alcanzado (es igual a cero),
            # hemos encontrado una combinación válida. La añadimos a 'result'.
            result.append(current_combination[:])  # [:] copia la combinación actual.
            return

        if target < 0 or start == len(nums):
            # Si el objetivo es negativo o hemos llegado al final de la lista de números,
            # no podemos continuar esta búsqueda en particular, así que detenemos la búsqueda.
            return

        for i in range(start, len(nums)):
            # Iteramos a través de los números en la lista, empezando desde 'start'.

            if i > start and nums[i] == nums[i - 1]:
                # Evitamos usar el mismo número en la misma posición más de una vez.
                # Si es un número duplicado en la misma posición, saltamos al siguiente.
                continue

            current_combination.append(nums[i])  # Agregamos el número actual a la combinación actual.

            # Llamamos recursivamente a 'backtrack' para seguir buscando.
            backtrack(i + 1, target - nums[i], current_combination)

            current_combination.pop()  # Quitamos el último número para probar otras combinaciones.

    nums.sort()  # Ordenamos la lista de números para manejar duplicados correctamente.

    # Llamamos a 'backtrack' para iniciar la búsqueda con los valores iniciales.
    backtrack(0, target, [])

    # Retornamos la lista de combinaciones válidas.
    return result

# Ejemplo de uso:
lista = [1, 5, 3, 2]
objetivo = 6
combinaciones = find_combinations(lista, objetivo)
print(combinaciones)
