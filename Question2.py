#Question # 2
def fibonacci(n):
    num1 = 0
    num2 = 1
    next_num = 0
    sum2 = 0
    for i in range(n-1):
        if num2 % 3 == 0: # to check if divisible by 3
            sum2 += num2
        next_num = num1 + num2  # adding the last two digits to generate the next number
        num1 = num2
        num2 = next_num
    return sum2
print(fibonacci(5000000))
