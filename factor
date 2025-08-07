# Check if one number is a factor of another

num = int(input("Enter the main number: "))
factor = int(input("Enter the potential factor: "))

if num % factor == 0:
    print(f"{factor} is a factor of {num}.")
else:
    print(f"{factor} is not a factor of {num}.")
