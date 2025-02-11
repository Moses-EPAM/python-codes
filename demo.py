from typing import Union

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    # Perform the calculation
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))

    result = round(result, 2)

    return result


print(some_expression_with_rounding(4,5))