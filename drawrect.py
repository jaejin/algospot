import sys

def increase(dict,x) :
    if dict.get(x) :
        dict[x] = dict[x] +1
    else :
        dict[x] = 1
    return dict

def find(dict):
    return reduce(lambda x,y :  y if dict.get(x) > dict.get(y)  else  x, dict)
    
rl = lambda : sys.stdin.readline()
n = int(rl())
output = []
for j in range(n):
    xdict = {}
    ydict = {}
    for i in range(3) :
        x, y = rl().split(' ')
        xdict, ydict = increase(xdict,x),increase(ydict,y)
        
    output.append( "%s %s" % ( find(xdict),find(ydict)))

for o in output :
    print o
