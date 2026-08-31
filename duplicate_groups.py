numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

groups = {}

for index, number in enumerate(numbers):
    if number not in groups:
        groups[number] = []

    groups[number].append(index)

print("\nDuplicate Groups:")

found = False

for number, positions in groups.items():
    if len(positions) > 1:
        found = True
        print(f"{number} → positions {positions}")

if not found:
    print("No duplicate numbers found.")
