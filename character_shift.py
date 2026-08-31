text = input("Enter a text: ")
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():
        if char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        result += char

print("Original :", text)
print("Modified :", result)
