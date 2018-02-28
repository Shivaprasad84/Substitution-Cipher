a = 0

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
beta = ''
word = ''
print("Enter a keyword\n")
key = input()
key = key.upper()
print("Enter a sentence\n")
sentence = input()
sentence = sentence.upper()

sentence  = sentence.split(' ')

for j in range(0, len(sentence)):
    if sentence[j].isdigit():
        sentence[j] = int(sentence[j])
        sentence[j] += len(key)
    elif isfloat(sentence[j]):
        sentence[j] = float(sentence[j])
        sentence[j] += len(key)
        
sentence = ' '.join(str(x) for x in sentence)

for i in range(0, len(sentence)):
    if sentence[i] not in alpha:
        word += sentence[i]
    else:
        word += key[a % len(key)]
        a = a + 1
# print(word)
for s in range(0, len(sentence)):
    if sentence[s] not in alpha:
        beta += sentence[s]
    else:
        beta += alpha[(alpha.index(sentence[s]) + alpha.index(word[s])) % 26]
print(beta)