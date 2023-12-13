"""Implemented a program that:
- Prompts the user for a level. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the users score: the number of correct answers out of 10.
- Structure your program as follows: def main(): /// def get_level(): /// def generate_integer(level): /// if __name__ == "__main__":       main()"""
import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            else:
                level = int(input("Level: "))
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def main():
    level = get_level()
    total_problems = 10
    correct_answers = 0

    for _ in range(total_problems):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        attempts = 0

        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == result:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                user_answer = int(input(f"{x} + {y} = "))

        if attempts == 3:
            print(f"{x} + {y} = {result}")

    print(f"Score: {correct_answers}")

if __name__ == "__main__":
    main()
