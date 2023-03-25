# Question : 7
import csv
with open('names.csv') as csv_file: # Reading the csv file of names
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    names = []
    for name in csv_reader:
        names.append(name[0])
names = list( dict.fromkeys(names) ) # To remove duplicate

def quicksort(names): # sorting the names using quicksort algorithm. Its time complexity is n*log(n) which is good as compared to some other
    if not names:
        return []
    return (quicksort([x for x in names[1:] if x <  names[0]])
            + [names[0]] +
            quicksort([x for x in names[1:] if x >= names[0]]))
    
names = quicksort(names) # calling the sorting algorithm

# Below initializing a list of turkish letters. 
turkish_letters = ['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z']

def score():      # function to calculate the score
    total_sum = 0
    name_sum  = 0
    row= 1
    for name in names:
        name_sum=0
        for i in range(len(name)):
            if name[i]==' ':
                continue
            index_value = turkish_letters.index(name[i]) # I am extracting the index number of alphabet from Turkish_letters list
            name_sum += index_value + 1 # Adding 1 because index start from 0 but here we need it to be started from 1.
        name_sum = row * name_sum
        row+=1
        total_sum += name_sum
    return total_sum
print(score())
