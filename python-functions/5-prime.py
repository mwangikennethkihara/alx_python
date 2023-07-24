def is_prime(number):
    # 0 and 1 are not prime numbers
    if number < 2:
        return False

    # Check if the number is divisible by any number from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

