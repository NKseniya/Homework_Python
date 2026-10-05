import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        return math.ceil(area)
    return area


test_side = 4.2
result = square(test_side)
print(result)

# Примеры использования:


print(square(5))      # 25 (целое число)
print(square(4.2))    # 18 (4.2 * 4.2 = 17.64, округляем вверх до 18)
print(square(3.1))    # 10 (3.1 * 3.1 = 9.61, округляем вверх до 10)
