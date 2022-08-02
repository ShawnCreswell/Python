#1. Countdown 
count = 0
t = input("Enter Number")
t = int(t)
while t >= count:
    print((t))
    t -= 1

#2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([3,77]))

#3. Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    return len(list) + (list[0])
print(first_plus_length([1,2,3,4,5]))

#4.Values Greater than Second
# def values_greater_than_second(list):
#         if len(list) < 
# print(values_greater_than_second(5,2,3,2,1,4))
def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    # greaterThan = list[1]
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5. This Length, That Value

def length_and_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))
print(length_and_value(6,2))