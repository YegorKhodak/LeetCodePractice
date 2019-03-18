def palindrome_check(n):
    digits = [int(x) for x in str(n)]
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[-i - 1]:
            return False
    return True
    pass


def prime_check(n):
    import numpy as np
    for i in range(2, int(np.sqrt(n))):
        if n % i == 0:
            return False
    return True


def generate_palindrome(n):
    """
    Dandeg
    :param n:
    :return:
    """
    digits = [int(x) for x in str(n)]
    deg = len(digits)

    if deg % 2 == 0 :
        pass
    else:

    while True:
        yield str(a) + "!!"


for a in generate_palindrome(1001):
    print(a)


# for i in range(0, 100000):
#     if palindrome_check(i):
#         if prime_check(i):
#             print(i)
