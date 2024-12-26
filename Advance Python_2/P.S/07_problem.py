numbers = [10, 15, 20, 25, 30]
result = filter(lambda x: x % 10 == 0, numbers)
print(list(result))
# ! Ans: [10, 20, 30]
