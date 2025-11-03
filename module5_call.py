from module5_mod import NumberCollection

def main():
    N = int(input("Enter a positive integer N: "))
    collection = NumberCollection()

    print(f"Enter {N} numbers:")
    for i in range(N):
        num = int(input(f"Number #{i + 1}: "))
        collection.add_number(num)

    x = int(input("Enter a number you want to find (X): "))

    position = collection.find_index(x)
    if position != -1:
        print(f"{x} is at index {position}.")
    else:
        print("-1")

if __name__ == "__main__":
    main()