
file = open('AlphaNumericCharacter.txt', 'r')
newCharacter = ' '
data = file.read()
readingData = data.split()
print('original List of data', readingData)
for i in readingData:
    for j in i:
        if j.isdigit():
            newCharacter = newCharacter + str(j)
    print(newCharacter)
    newCharacter=''



