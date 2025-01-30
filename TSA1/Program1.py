text = input("Enter a string: ")

vowels = consonants = spaces = others = 0
for char in text.lower():
    if char in "aeiouAEIOU":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1
        
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Others: {others}")