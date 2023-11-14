memo1 = {}
def fact1(x):
    if x < 2: return 1
    if x not in memo1:
        memo1[x] = x * fact1(x-1)
    return memo1[x]

range_upto =int (input("Enter range up to you want to print factorial: "))
for i in range(1, range_upto):
  print(fact1(i))
print(memo1)
