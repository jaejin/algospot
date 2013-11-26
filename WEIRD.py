import sys

def sumList(l):
    return reduce(lambda x,y : x+y , l)

def semiperfectnum(n,l):
    l = reversed(l)
    for i in l :
        if n >= i :
            n = n - i
            
        elif n <= 0 :
            break

    return True if n == 0 else False
    

def sumOfDivisorList(n):
    return  filter(lambda i : n % i == 0, range(1,n))
    
def isWeird(n):
    divisorList = sumOfDivisorList(n)
    sum = sumList(divisorList)
    if sum > n :
        return "not weird" if semiperfectnum(n, divisorList) else "weird"
    else :
        return "not weird"
    
rl = lambda : sys.stdin.readline()
n = int(rl())

for j in range(n) :
    print isWeird(int(rl()))
    

