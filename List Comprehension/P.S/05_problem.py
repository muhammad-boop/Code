'''
Filter Positive Numbers
From the list [-3, -1, 0, 2, 5, 7, -9], create a new list that contains only the positive numbers.
'''
list = [-3, -1, 0, 2, 5, 7, -9]
positive = [i for i in list if i>0]
print(positive)