# ! Using ForLoop
list2 = [2,88,90,12,22]
CubeList= []
for i in list2:
  CubeList.append(i**3)
print(CubeList)
# ! Using List Comprehension
list = [1,2,4,6,5,90,77]
squareList = [i**2 for i in list]
print(squareList)
# ! Number printing by using for Loop
n = [m for m in range(1,101)]
print(n)