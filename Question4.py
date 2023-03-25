# Question: 4
def isPrime(n):  # Function to check if a number is prime or not
    if n <= 1:
        return False
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True
def Prime(limit):
    count = 0
    i=2
    prime = None 
    while count!=limit:
        if isPrime(i):
            prime = i
            count+=1
        i+=1
    return prime

limit = 10101
Prime(limit)
