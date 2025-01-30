# Pattern A: Leaning to the left
print("A pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern B: Leaning to the right
print("\nB pattern:")
i = 1
while i <= 7:
    if i % 2 != 0 or i == 6:
        spaces = 7 - i  # Calculate leading spaces to shift pattern right
        print(" " * spaces + str(i) * i)
    i += 1