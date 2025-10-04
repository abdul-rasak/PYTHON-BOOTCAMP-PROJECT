# For loop in Python
name = "Abdulrasak"
for letters in name:
    print(letters)

#Applying for loop to list
items = ["Vegitable Oil", "Onion", "Pepper","Salt"]
for item in items:
    print(item)

nums = [1,2,3,4,5,6,7,8,9,10] 
for num in nums:
    if num % 2 == 0:
        print(f'Even Number {num}')
    elif num % 2 != 0:
        print(f'Odd Number {num}')    