
def range_of_list(list):
    return max(list) - min(list)

def median(list):
    return sorted(list)[len(list)//2]
 
def length(list):
    return len(list)

def mean(list):
    return sum(list)/len(list)

numbers = [1, 2, 3, 4, 5]

print("The list is: ", numbers)
print("The median of the list is :",median(numbers))
print("The length of the list is :",length(numbers)) 
print("The mean of the list is :",mean(numbers)) 
print("The range of list is :",range_of_list(numbers)) 