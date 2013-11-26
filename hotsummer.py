import sys

rl = lambda : sys.stdin.readline()
n = int(rl())

for j in range(n):
    sum =  int(rl())
    list = rl().split(" ")
    print "YES" if sum >= reduce(lambda x,y:x+y, [int(s) for s in list]) else "NO"
