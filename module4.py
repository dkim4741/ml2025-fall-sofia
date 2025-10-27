
N = int(input("Enter a positive integer N: "))
numbers = []
print(f"Enter {N} number: ")
for i in range(N):
    num = int(input(f"Number #{i + 1}: "))
    numbers.append(num)

x = int(input("Enter a number you want to find (X): "))

if x in numbers:
    position = numbers.index(x) + 1
    print(f"{x} is at index {position}.")
else:
    print("-1")