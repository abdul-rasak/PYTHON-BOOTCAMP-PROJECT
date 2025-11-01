mylist = [1,2,3,4,5,6,7,8,9]
print(help(mylist.insert))
#range Function
for num in range(10):
    print(num) 

for num in range(1,10):
    print(num)

print(list(range(1,10)))       

#Enumerate function
index_count = 0
animal = 'monkey'
for letter in animal :
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1
for item in enumerate(animal):
    print(item)

#Zip  function
list1 = [1,2,3]
list2 = ['a','b','c']   
for item in zip(list1,list2):
    print(item)

#Input
name = input('What is your name ?')    

print(name)
