# #1
# def print_1_to_255():
#     for i in range(256):
#         print(i)
# print_1_to_255()
# #2
# def print_ints_and_sum_0_to_255():
#     sum = 0
#     for i in range(256):
#         sum = sum + i
#         print("number: ", i, "running total: ", sum)
# print_ints_and_sum_0_to_255()

#3
# def print_max_of_array(arr):
#     largest = arr[0]
#     for i in arr:
#         if i > largest:
#             largest = i
#     print(largest)

# print_max_of_array([4,5,34,23,56,42])

# def return_odds_array_1_to_255():
#     odds = []
#     for i in range(1,256):
#         if i % 2 == 1:
#             odds.append[i]
#         return(odds)

# print(return_odds_array_1_to_255())
# odds = return_odds_array_1_to_255()

# def return_array_count_greater_thanY(arr, y):
#     count = 0
#     for i in arr:
#         if i > y:
#             count =+ 1
#     print(count)

# return_array_count_greater_thanY(return_odds_array_1_to_255, 163)

def printMaxMin_average_array_val(arr):
    max = arr[0]
    min = arr[0]
    sum = 0

    for i in arr:
        if max < i:
            max = i
        if min > i:
            min = i
        sum += i
    print(max, min, sum)
    avg = sum / len(arr)
    print(avg)
    
printMaxMin_average_array_val([1, 2, 3, 4, 5, 6])

def swapStringFor_array_negative_vals(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    return arr

print(swapStringFor_array_negative_vals([1, -2, 3, -4, 5, -6]))

def swapStringFor_array_negative_vals2(arr):
    emptyArr = []
    for i in arr:
        if i < 0:
            emptyArr.append('Dojo')
        else:
            emptyArr.append(i)
    return arr

def print_avg_of_array(arr):
    sum  = 0
    for num in arr:
        sum += num
    print(sum / len(arr))
print_avg_of_array([1,2,3,4,5])

def square_arr_vals(arr):
    for i in range(len(arr)):
        arr[i]= arr[i] * arr[i]
    print(arr)
square_arr_vals([1,2,3,4,5])

def zero_out_arry_negatives_vals(arr):
    for i in range (len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr

print(zero_out_arry_negatives_vals([1,-5,8,-9]))

def shift_array_vals_left(arr):
    for i in range (len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = 0
    return arr

print(shift_array_vals_left([1,2,3,4,5]))