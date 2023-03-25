# Question 5
list1 = [3, None, 2, None, None, 1, False, None, 10]
previous = list1[0]
list2=[]
for i in range(len(list1)):
    if list1[i]== None:
        list2.append(previous)
        previous = list1[i-1]
    else:
        list2.append(list1[i])
        previous = list1[i]

print(list2)
