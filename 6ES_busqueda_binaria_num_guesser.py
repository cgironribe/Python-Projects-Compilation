# Prueba hacer una función que pida al usuario pensar en un numero en el rango 1-50, el programa encontrará el numero elegido a través de preguntas.

def guess_num(start, end):
    while start <= end:
        mid = (start + end) //2
        question = input(f"Is your number greater than {mid}? y/n:  ").lower()
        if question == 'y':
            start = mid +1 
        elif question == 'n':
            end = mid -1
        else:
            print("Please provide 'y' if your answer is positive or a 'n' if negative")
    print(f"Your number is {start}!")

if __name__ == "__main__":
    print("Think about one number from 1 to 50 and I will guess it!")
    guess_num(1, 50)