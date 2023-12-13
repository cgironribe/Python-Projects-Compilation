#Programa que genera aleatoriamente X num. de dígitos en un rango deseado y comprueba cuántas vueltas le toma aparecer al valor introducido por el usuario.

from random import randint 

def loteria():
    boletos = randint(1, 30)
    return boletos

def split_nums(boleto): 
    boleto_split = boleto.split(" ") 
    n1, n2, n3, n4 = boleto_split 
    int_n1 = int(n1)
    int_n2 = int(n2)
    int_n3 = int(n3)
    int_n4 = int(n4)
    tu_boleto = [int_n1, int_n2, int_n3, int_n4]
    return tu_boleto


cliente_boleto = input("Pon los numeros de tu boleto separados por espacios:\t")
cliente_boleto = split_nums(cliente_boleto)

veces_jugado = 0
Active = True

while Active == True:
    num1 = loteria()
    num2 = loteria()
    num3 = loteria()
    num4 = loteria()
    result = [num1, num2, num3, num4]
    print(f"El boleto ganador es {result}")
    if result != cliente_boleto:
        veces_jugado += 1
    else:
        Active = False
print(f"Tu boleto {cliente_boleto} ES GANADOR!")
print(f"Veces jugadas: {veces_jugado}")
 