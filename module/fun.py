#1.print negative or positive no
def np(a):
    if a<0:
        return "negative"
    elif a>0:
        return "positive"    
    else:
        return 'zero'

#2.reverse of string using slicing
def revs(a):
    return a[::-1]
#3.find biggest of 3 nos
def big3(a,b,c):
    if(a>b) and (a>c):
        return a
    elif (b>c) and (b>a):
        return b
    else:
        return c
#4.pattern 
def pat():
    for i in range(1,6):
        for c in range(i):
            print(i, end=" ")
            i=i+1
        print()
 #5.leap year or  not   
def leap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False
#6.print sum of digits of number
def digit(nu):
    num=str(nu)
    s = 0
    for i in num:
        s += int(i)
    return s
#7.print sum of n nos
def sumn(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
#8.armstrong no
def armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))
    a=len(str(num))
    for digit in str(num):
        s=int(digit)        
    return num==a+s    
#9.palindrome
def palindrome(u):
    s = str(u)
    return s == s[::-1]
#10.Swap Two Elements in a List
def swap(l, p1, p2):
	l[p1],l[p2]=l[p2],l[p1]
	return l