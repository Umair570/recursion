def sum_natural(n):
    if n==0:
        return 0
    return n + sum_natural(n-1)
print(sum_natural(100))

def elem_list(lst,idx):
    if idx==len(lst):
        return 
    print(lst[idx])
    elem_list(lst,idx+1)

lst=[1,3,5,6,8,9]
elem_list(lst,0)


def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fac(n-1)
    
print(fac(5))

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(5))    

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
print(gcd(9888,6060))

def sum(list):
    if list==[]:
        return 0
    else:
        return list[0]+sum(list[1:])
    
print(sum([1,2,3,4])) 

def reverseString(string):
    if string=='':
        return string
    else:
        return string[-1]+reverseString(string[:-1])
    
print(reverseString("hello"))    

def element(s,ele):
    if not s:
        return 0
    
    elif s[0]==ele:
        return 1+element(s[1:],ele)
    
    else:
        return element(s[1:],ele)
    
print(element("Umairirer","r"))    
        

def elements(list,ele):
    if not list:
        return 0
    elif list[0]==ele:
        return 1+elements(list[1:],ele)
    else:
        return elements(list[1:],ele)
    
print(elements([1,2,3,4,2,5,6,2,2,2,2],2))    

def tri(n):
    if n==1:
        print("[]")
        return
    else:
        print("[]"*n)
        tri(n-1)

tri(6)

def findMin(lst):
    if len(lst)==1:
        return lst[0]
    else:
        min=findMin(lst[1:])
        if lst[0]<min:
            return lst[0]
        else:
            return min

print(findMin([3,4,5,1,6,7,2]))

def findMax(lst):
    if len(lst)==1:
        return lst[0]
    else:
        max=findMax(lst[1:])
        if lst[0]>max:
            return lst[0]
        else:
            return max
        
print(findMax([3,1,4,1,5]))

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
    
print(GCD(48,18))

def isSorted(lst):
    if len(lst)==1:
        return True
    else:
        if lst[0]<=lst[1]:
            isSorted(lst[1:])
            return True
        else:
            isSorted(lst[1:])
            return False
        
print(isSorted([4,3,2,1]))     


def findElement(lst,element):
    if lst==[]:
        return False
    elif lst[0]==element:
        return True
    else:
        return findElement(lst[1:],element)
    
print(findElement([1,2,3,4],3))    





#Practice Again
#1
def sumElements(lst):
    if lst==[]:
        return 0
    else:
        return lst[0]+sumElements(lst[1:])

print(sumElements([10,12,3,4]))        

#2
def reverseString(string):
    if len(string)==0:
        return string
    else:
        return string[-1]+reverseString(string[:-1])

print(reverseString("umair"))

#3
def calculatePower(a,b):
    if b==0:
        return 1
    else:
        return a*calculatePower(a,b-1)
    
print(calculatePower(2,3))

#4
def findMin(lst):
    if len(lst)==1:
        return lst[0]
    else:
        min=findMin(lst[1:])
        if lst[0]<min:
            return lst[0]
        else:
            return min

print(findMin([6,2,4,5,1,9]))

#5
def occurrence(lst,element):
    if lst==[]:
        return 0
    elif lst[0]==element:
        return 1+occurrence(lst[1:],element)
    else:
        return occurrence(lst[1:],element)
    
print(occurrence([1,2,3,4,5,2,3,2,3,2],2))    
        
        