'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    start = 4
    num1 = 1
    num2 = 2
    num3 = 4
    if n > 3:
        for i in range(start, n + 1):
            result = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = result
            start += start
    else:
        if n <= 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            result = 4
    return result


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
