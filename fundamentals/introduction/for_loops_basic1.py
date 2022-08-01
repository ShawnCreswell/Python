# 1.Basic- Print all integers from 0 to 150
for nums in range(0, 151):
    print(nums)
# 2. Multiples o five -Print all the mulitples of 5 from 5 to 1,000
for mulitples in range(5, 1005, 5):
    print(mulitples)
# 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for count in range(1, 101):
    if count % 10 == 0:  
        print("Coding Dojo")
    elif count % 5 == 0: 
        print('Coding')
    else:
        print(count)
# 4. Add odd integers from 0 to 500,000 and print the final sum.
sum = 0
for odd in range(0, 500001):
    if odd % 2 == 1:
        sum = odd + sum
print(sum)
# 5. Print positive numbers starting at 2018, counting down by fours.
for pos in range(2018, 0, -4):
    print(pos)
# 6. Flexiable counter
lowNum = 2
highNum = 9
mult = 3

for count in range(lowNum, highNum+1):
    if count % mult == 0:
        print(count)