def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:          # делится и на 3, и на 5
            print("FizzBuzz")
        elif i % 3 == 0:         # делится только на 3
            print("Fizz")
        elif i % 5 == 0:         # делится только на 5
            print("Buzz")
        else:                    # не делится ни на 3, ни на 5
            print(i)


# Пример использования:
fizz_buzz(19)
