num = int(input("How many numbers you want to input : "))
lst = []

for n in range (num):
    numbers =int(input("Enter a number : " ))
    lst.append(numbers)


print("Sum of them : ", sum(lst))
