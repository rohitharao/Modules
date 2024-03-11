import fun
#+ve or -ve or 0
print(fun.np(-6))
print()
#reverse of string using slicing
print(fun.revs("bag"))
print()
#find biggest of 3 nos
print(fun.big3(9,12,3))
print()
#pattern sum
fun.pat()
print()
#leap year or  not
y = int(input("Enter a year: "))
if fun.leap(y):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")
print()
#print sum of digits of number    
nu=input("enter a 2 or 3 digit number:")
print(fun.digit(nu))
print()
#print sum of n nos
n=int(input("give nth no:"))
print(fun.sumn(n))
print()

#armstrong no
num = int(input("Enter a number(arm): "))
print("Armstrong" if fun.armstrong(num) else "Not Armstrong")
print()
#palindrome
u = int(input("Enter a number)pal: "))
if fun.palindrome(u):
    print(u, "is a palindrome number.")
else:
    print(u, "is not a palindrome number.")
print()
#Swap Two Elements in a List
print(fun.swap([26,5,9,96],1,3))
