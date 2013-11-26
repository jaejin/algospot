import sys


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

def bigendian(n):
    bit = bin(n)[2:]
    l = [str(0) for i in range(32)]
    l = l[len(bit):]
    return "%s%s" % (''.join(l),bit)

def littleendian(bitn):
    return int(''.join([i for i in reversed([j for j in  chunks(bitn,8)])]),2)
    
rl = lambda : sys.stdin.readline()
n = int(rl())
inputl = []
for i in range(n):
    inputl.append(int(rl()))

for o in inputl :                 
    print "%s" %  littleendian(bigendian(o))