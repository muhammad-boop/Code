'''
Given the list words = ["apple", "banana", "cherry", "date"], use filter() to extract words that have more than 5 letters.
'''

words = ["apple", "banana", "cherry", "date"]
def more_than_5(word):
  if(len(word)>5):
    print(f"{word} has more than 5 letters")
  else:
    print(f"{word} has less than 5 letters")
final = filter(more_than_5, words)
print(list(final))  