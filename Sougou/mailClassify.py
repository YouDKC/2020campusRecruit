import math
train,Test,dim = [int(i) for i in input().strip().split('\t')]
t = [0]*dim
f = [0]*dim
test = []
while train>0:
    w = [int(i) for i in input().strip().split('\t')]
    if w[0]==1:
        for i in range(dim):
            t[i] += w[i+1]
    else:
        for i in range(dim):
            f[i] += w[i+1]
    train-=1
while Test>0:
    w = [int(i) for i in input().strip().split('\t')[1:]]
    Test-=1
    test.append(w)

for t3 in test:
    a,b = 0,0
    for t1 in t:
        a+=math.sqrt(sum([(t1[d]-t3[d])**2 for d in range(dim)]))
    for t2 in f:
        b+=math.sqrt(sum([(t2[d]-t3[d])**2 for d in range(dim)]))
    print(0+(a<b))