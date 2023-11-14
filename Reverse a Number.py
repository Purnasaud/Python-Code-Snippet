def reversing_Number(number):
      if len(str (number))==0:
           print('Number of Digits are ', 0)
      else:
          print('Number of digits are', len(number))
          reverse= number[::-1]
          return int(reverse)
value = input('Enter a Number: ')
print(reversing_Number(value))