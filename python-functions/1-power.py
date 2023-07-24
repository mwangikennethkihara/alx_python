def pow(a, b):
    # Base case: anything raised to the power of 0 is 1
    if b == 0:
        return 1

    # Calculate the absolute values of a and b
    abs_a, abs_b = abs(a), abs(b)

    # Initialize the result to 1
    result = 1

    # Multiply abs_a to the result abs_b times
    for _ in range(abs_b):
        result *= abs_a

    # Consider the signs of a and b to get the final result
    if b < 0:
        result = 1 / result

    if a < 0 and b % 2 != 0:
        result = -result

    return result

