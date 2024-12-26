# Write a Python program using filter() to find all strings that contain the letter "a" in the list ['dog', 'cat', 'bat', 'fish']
words = ["dog", "cat", "bat", "fish"]
def letter(word):
  if("a" in word):
    print(f"{word} word contain letter a")
  else:
    print(f"{word} word not have letter a")
final = filter(letter,words)
print(list(final))