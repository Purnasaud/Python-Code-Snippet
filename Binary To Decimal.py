def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n%8, end=' ')

number = int(input('Enter a Number: '))
print(convertToBinary(number))