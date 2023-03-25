# Question: 3
def isPalindrome(n): # function to check if a number is palindrome or not
    number=[]
    digit= None
    while n>=1:
        digit = n %10
        n = n//10
        number.append(digit)
    end = -1
    for i in range(len(number)//2):
        if number[i]!= number[end]:
            return False
        else:
            end = end -1
    return True
   
def Palindrome():
    palindrome_value= 0
    for i in range(100,1000): # range for 3 digit numbers only, we can change this range
        for j in range(i,1000):
            result = i * j 
            #print(result)
            if (isPalindrome(result)): 
                if result > palindrome_value:
                    palindrome_value = result
    return palindrome_value
print(Palindrome())
    
    
    
    
