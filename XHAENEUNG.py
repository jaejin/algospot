import sys


numbers= {"zero":0,0:"zero", 1:"one","one":1,2:"two","two":2,3:"three", "three":3,4:"four", "four":4,5:"five", "five":5, 6:"six","six":6,7:"seven", "seven":7,8:"eight", "eight":8,9:"nine", "nine":9,10:"ten","ten":10}


rl = lambda : sys.stdin.readline()
n = int(rl())

def operator(op,a,b,c):
    try :
        if op == "+" :
            return "Yes" if  sorted(c) == sorted(numbers[numbers[a] + numbers[b]]) else "No"
        elif op == "-" :
            return "Yes" if  sorted(c) == sorted(numbers[numbers[a] - numbers[b]]) else "No"
        elif op == "*" :
            return "Yes" if  sorted(c) == sorted(numbers[numbers[a] * numbers[b]]) else "No"
    except Exception :
        return "No"

for j in range(n):
    l = rl().replace("\n","")
    a,op,b,_,c=l.split(" ")
    print operator(op,a,b,c)

