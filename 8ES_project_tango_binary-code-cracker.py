import random
#Binary Code Cracker
#Idea del juego Project Tango. Tienes que adivinar el código de cuatro cifras de 0's y 1's. 
# El programa te dará una pista sobre cuantos errores has cometido una vez introduzcas tu deducción y tendrás 5 intentos.

def code_cracker():
    codigo_secreto = [random.randint(0, 1) for _ in range(4)]
    print("-La pantalla muestra un espacio de cuatro dígitos con solo botones '0' y '1' debajo-")
    
    intentos = 5
    while intentos > 0:
        user = input("Ingresa el código secreto: ")
        
        if len(user) != 4 or not user.isdigit():
            print("Por favor, ingresa un código de 4 dígitos válidos (0 o 1).")
            continue

        user_code = [int(digit) for digit in user]
        
        # Contar 0 y 1 en común
        aciertos = sum(a == b for a, b in zip(user_code, codigo_secreto)) # Utilizando zip para comparar cada dígito del input del usuario (user_code) con el código secreto (codigo_secreto). # La función zip crea parejas de elementos, tomando un elemento de user_code y otro de codigo_secreto al mismo tiempo, y compara si son iguales
        aciertos_0 = sum(a == 0 for a in user_code) # Contando cuántos (0) hay en user_code
        aciertos_1 = sum(a == 1 for a in user_code) # Contando cuántos (1) hay en user_code
        
        if aciertos == 4:
            print("¡Has descifrado el código! ¡Felicidades!")
            break
        else:
            print(f"Has adivinado {aciertos} dígitos en la posición correcta.")
            print(f"Tienes {aciertos_0} '0' en común y {aciertos_1} '1' en común.")
            print(f"Te quedan {intentos - 1} intentos.\n")
            intentos -= 1
    
    if intentos == 0:
        print("Te has quedado sin intentos. La operación ha fallado.")
        print(f"El código secreto era: {codigo_secreto}")

code_cracker()
