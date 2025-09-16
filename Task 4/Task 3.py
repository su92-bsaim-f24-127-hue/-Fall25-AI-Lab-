s = input("Enter a sentence: ")
words = s.split()
n = len(words)
for i in range(n):
    for j in range(n - i - 1):
        if words[j] > words[j + 1]: 
            words[j], words[j + 1] = words[j + 1], words[j]

print(" ".join(words))
