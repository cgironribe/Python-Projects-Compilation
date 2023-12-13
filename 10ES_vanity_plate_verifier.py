# Programa que permite validar si la personalización de una matrícula es apta o no para proceder siguiendo varios tests.

plate = input("Introduce your vanity plate: ")

# Inicializamos variables booleanas para cada condición
starts_with_two_letters = not (plate[0].isdigit() or plate[1].isdigit())
valid_length = 2 <= len(plate) <= 6
numbers_at_end = False
first_digit_not_zero = False
no_special_characters = plate.isalnum()

# Verificamos si hay números al final de la matrícula
if len(plate) == 6:
    numbers_at_end = plate[-1].isdigit() and plate[-2].isdigit() and plate[-3].isdigit()
elif len(plate) == 5:
    numbers_at_end = plate[-1].isdigit() and plate[-2].isdigit()

# Verificamos si el primer dígito no es cero
if len(plate) == 6:
    first_digit_not_zero = plate[-3] != '0'
elif len(plate) == 5:
    first_digit_not_zero = plate[-2] != '0'

# Comprobamos si todas las condiciones son verdaderas
if starts_with_two_letters and valid_length and numbers_at_end and first_digit_not_zero and no_special_characters:
    print("Valid")
else:
    print("Invalid")



