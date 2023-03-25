# Question: 1
def Question1():
    sum1=0
    for i in range(1,1000000): 
        if i%2==0 or i%3==0 or i%5==0: 
            sum1+= i
    print("The sum of natural numbers less than 1 million whose prime factors are only 2, 3, or 5 is : ",sum1)
Question1()
