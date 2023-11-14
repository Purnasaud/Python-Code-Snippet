# Python programming to learn a Fibonnaci Series
nums = {}
def fib(n):
    if n<=1:
       nums[n] =n
       return n
    if n in nums:
        return nums[n]
    else:
        num = fib(n-1) + fib(n-2)
        nums[n] = num
        return num

# Printing fibonnaci Series Upto Nth terms
#print(fib(1000))

number =  int (input("Enter range of your fibonnaci series: "))

for i in range(0, number+1):
    print(fib(i))

print(nums)

