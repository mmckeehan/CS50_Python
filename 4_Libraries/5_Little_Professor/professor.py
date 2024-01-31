# Prompts user to INPUT for LEVEL. 1 through 3. VALUE_ERROR if not given correctly
# LOOPS 10 times generating 10 RANDOM addition problems
# PROMPTS user to INPUT SOLUTION
# IF SOLUTION != COR_ANS, PRINT EEE and Try again, LOOP 3 times, if needed. PRINT COR_ANS if correct guess is not given
# PRINT SCORE


import random


def main():
    level = get_level()
    i = 0
    x = int()
    y = int()
    ans = 0
    total_correct = 0

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        cor_ans = x + y
        while ans < 3:
            try:
                print(f"{x} + {y} = ", end="")
                solution = int(input())
                if solution == cor_ans:
                    total_correct += 1
                    break
                else:
                    ans += 1
                    print("EEE")
                    if ans == 3:
                        print(f"{x} + {y} = {cor_ans}")
            except ValueError:
                None

        ans = 0
        i += 1
    print(f"Score: {total_correct}")


def get_level():
    while True:
        try:
            gl = int(input("Level: "))
            if 1 <= gl <= 3:
                return gl
            else:
                raise ValueError
        except ValueError:
            None
    return gl


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
