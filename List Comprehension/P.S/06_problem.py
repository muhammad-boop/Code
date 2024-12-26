'''
print only even numbers from the list [1,2,3,4,5,6,7,8,9,10]
'''
list = [1,2,3,4,5,6,7,8,9,10]
even = [i for i in list if i%2==0]
print(even)