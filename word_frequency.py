sentence = input("Enter a sentence: ")

words = sentence.lower().split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    frequency[word] = frequency.get(word, 0) + 1

result = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nWord Frequency:")
for word, count in result:
    print(f"{word} : {count}")
