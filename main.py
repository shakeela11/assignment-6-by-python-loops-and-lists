#Question no 3
#*Write a program* that uses a while loop to print the first 25 integers.
count:int=1
while count <= 25:
    print(count)
    count += 1

#Question no 4
#*Write a program* that uses a while loop to print the first 10 even numbers.
count:int=1
num:int=2
while count<=10:
    print(num)
    num+=2
    count+=1

# Question no 3
#  *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
nums:list[int]=[1,-2,-3,4,-5,6]
for num in nums[1:6]:
    if num <= 0:
        nums.remove(num)
print(nums)

# Question no 5
# *create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number
def num(Number)->int:
     count = 1
     result=1
     while (count <= Number):
          result = result * count
          count = count + 1
     return result
print(num(2)) 

#Question no 9
# *create a program* to remove all the odd numbers from an array.
numbers:list[int]=[1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num % 2 != 0:
        numbers.remove(num)
print(numbers)

#Question no 1
# *create a function* that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array
def insert_value(arr, index, num):
    arr.insert(index, num)
    return arr

print(insert_value([1, 2, 3, 4, 5], 0, 5))

#Question no 7
#  *create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array
def nums(array):
 count=0
 total=0   
 while count<len(array):
   count+=1
   total+=array[count-1]
 return total
print(nums([1,2,3,4,5]))


#Question no 8
# Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
celsius_temperatures = []
while True:
  temp = input("Enter temperature in Celsius (or 'done' to finish): ")
  if temp == 'done':
    break
  celsius_temperatures.append(float(temp))

fahrenheit_temperatures = []
i = 0
while i < len(celsius_temperatures):
  celsius = celsius_temperatures[i]
  fahrenheit = (celsius * 9/5) + 32
  fahrenheit_temperatures.append(fahrenheit)
  i += 1

print("Temperatures in Fahrenheit:", fahrenheit_temperatures)

# Question no 2
# Implement a simple shopping cart program using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation
cart = []
def add_item(item):
  cart.append(item)
  print(cart)
def remove_item(item):
  cart.remove(item)
  print(cart)
def update_quantity(item, quantity):
  cart[cart.index(item)] = (item, quantity)
  print(cart)
add_item('apple')
add_item('banana')
remove_item('banana')
update_quantity('apple', 2)
