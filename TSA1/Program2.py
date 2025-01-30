digits = input("Enter a string with digits/numerical characters: ")
total = 0
for char in digits:
    if char.isdigit():
        total += int(char)
print(f"Total of digits: {total}")