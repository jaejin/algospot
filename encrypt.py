import sys

    
rl = lambda : sys.stdin.readline()
n = int(rl())
output = []
for j in range(n):
    s = rl()
    s = s.replace('\n','')
    odd = ""
    even = ""
    for i in range(len(s)) :
        if i % 2 == 0 :
            even += s[i]
        else :
            odd += s[i]
    print "%s%s" % (even,odd)

