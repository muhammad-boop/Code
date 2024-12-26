# ! list_comprehension
myList = [1,2,4,5,6,8,9]
# sqauredList = []

# for item in myList:
#   sqauredList.append(item*item)
# print(sqauredList)
# ~ By using List Comprehensions
squaredList = [i*i for i in myList ]
print(squaredList)