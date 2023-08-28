my_list = [1,2,3,4,5]

numbers_to_append = [10,11,12]

for num in numbers_to_append:
    my_list.append(num)

print(my_list)

my_list.append(6)
print(my_list)

my_list.pop() #remove last element
print(my_list)

my_list.insert(1,100) #enter 100 to 2nd location 1st index
print(my_list)

print(my_list[1:3]) #slicing and take only 1 and 2nd indexes

num1 = [1,3,5,7,9]
num2 = [2,4,6,8,10]
for n1, n2 in zip(num1, num2): #zipping
    print(n1, n2)

from array import array
my_array = array('i', [1,2,3,4,5])
print(my_array)