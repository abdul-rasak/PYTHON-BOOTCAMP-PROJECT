# For loop in Python
name = "Abdulrasak"
for letters in name:
    print(letters)

#Applying for loop to list
items = ["Vegitable Oil", "Onion", "Pepper","Salt"]
for item in items:
    print(item)

# Applying controlflow to for-loop

nums = [1,2,3,4,5,6,7,8,9,10] 
for num in nums:
    if num % 2 == 0:
        print(f'Even Number {num}')
    elif num % 2 != 0:
        print(f'Odd Number {num}')  

#Tuples in for-loop   
stocks = [(1,2),(3,4),(5,6),(7,8)]       
for stock in stocks:
    print(stock)
#Tuples Unpacking 
for a,b in stocks:
    print(a)
    print(b)
# Dictionary in for-loop    
py_dict = {'a' :10, 'b':20,'c':30}
for key,value in py_dict.items():
    print(key)
    print(value)