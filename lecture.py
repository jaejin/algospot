import sys

def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

rl = lambda : sys.stdin.readline()
n = int(rl())

for i in range(n):
    print ''.join(sorted([s for s in chunks(rl(),2)]))
