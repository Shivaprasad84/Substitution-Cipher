a = 0
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
beta = ''
word = ''
print("Enter a keyword\n")
key = input()
key = key.upper()
key = list(key)
print("Enter a sentence\n")
sentence = input()
sentence = sentence.upper()
for i in range(0, len(sentence)):
    if sentence[i] == " ":
        word += " "
    else:
        word += key[a % len(key)]
        a = a + 1
# print(word)
for s in range(0, len(sentence)):
    if sentence[s] not in alpha:
        beta += " "
    else:
        beta += alpha[(alpha.index(sentence[s]) + alpha.index(word[s])) % 26]
print(beta)
