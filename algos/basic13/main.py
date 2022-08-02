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

def return_odds_array_1_to_255():
    odds = []
    for i in range(1,256):
        if i % 2 == 1:
            odds.append[i]
        return(odds)

print(return_odds_array_1_to_255())
odds = return_odds_array_1_to_255()

def return_array_count_greater_thanY(arr, y):
    count = 0
    for i in arr:
        if i > y:
            count =+ 1
    print(count)

return_array_count_greater_thanY(return_odds_array_1_to_255, 163)