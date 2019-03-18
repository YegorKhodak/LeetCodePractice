"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


class Solution:

    @staticmethod
    def self_dividing_numbers(left, right):
        sdn = []
        for i in range(left, right + 1):
            try:
                digits = [Solution.change(x) for x in str(i)]
            except ValueError:
                continue

            flag = True
            for j in digits:
                if i % j != 0:
                    flag = False
                    break
            if flag:
                sdn.append(i)
        return sdn

    @staticmethod
    def change(param):
        int_param = int(param)
        if int_param == 0:
            raise ValueError
        return int_param


if __name__ == '__main__':
    print(Solution.self_dividing_numbers(1, 200))
