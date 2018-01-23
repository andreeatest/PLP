from collections import Counter

file_name = input("Enter file name: ")

num_words = 0

with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        num_lines = sum(1 for line in open('text.txt'))

    print("Number of words:")
    print(num_words)
    print(num_lines)
    print(Counter(words))