#Ceasar de-cypher:

  #input the key in the first line(any natural number other than the multiples of 26)
  #input a word or a sentence to decrypt on the next line

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

beta = ''

print('Enter a key\n')
key = int(input())
print('Enter a word or a sentence\n')
word = input()

word = word.upper()
word = word.split(' ')
for s in range(0, len(word)):
    if word[s].isdigit():
        word[s] = int(word[s])
        word[s] -= key
    elif isfloat(word[s]):
        word[s] = float(word[s])
        word[s] -= key
        
word = ' '.join(str(x) for x in word)

for j in range(0, len(word)):
    if word[j] not in alpha:
        beta += word[j]
    else:
        beta += alpha[(alpha.index(word[j]) - key) % 26]

print("Decryption\n")
print(beta)

## check caesar cypher first
