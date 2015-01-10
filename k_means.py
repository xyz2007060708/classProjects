import random
from math import sqrt 

def euDis(x, y):
    if x == y:
        return 0.0
    res = sqrt(sum( (x[i] - y[i])**2 for i in xrange(len(x)) ))
    return res

def assignPnt(ctr, L):
    cluster = [[] for c in ctr]
    for i in xrange(len(L)):
        d = euDis(L[i], ctr[0])
        belong_to = 0
        for j in xrange(len(ctr)):
            if d > euDis(L[i], ctr[j]):
                d = euDis(L[i], ctr[j])
                belong_to = j
        cluster[belong_to].append(i) 
    return cluster

def calcNewCtr(cluster, L):
    ctr = []
    for c in cluster:
        coordinate = [0.0 for x in L[0]]
        for i in c:
            for j in xrange(len(L[i])):
                coordinate[j] += L[i][j]
        ctr.append(tuple(x/len(c) for x in coordinate))
    return ctr
   
def kmeans(k, L):
    if len(L) == 0 or k == 0 or k > len(L):
        return None
    ctr = random.sample(L,k)
    prectr = []
    while set(ctr) != set(prectr):
        prectr = ctr[:]
        cluster = assignPnt(ctr, L)
        ctr = calcNewCtr(cluster, L)
    #form result
    res = []
    for i in xrange(k):
        res.append((ctr[i],[L[j] for j in cluster[i]]))
    return res
    
    
if __name__ == '__main__':
    import pickle
    datafile = open("cdata.txt","r")
    vals = pickle.load(datafile)
    datafile.close()
    se = [[] for k in xrange(1,9)]
    for k in xrange(1,9):
        for i in xrange(5):
            res = kmeans(k, vals)
            s = 0.0
            for j in xrange(k):
                n = len(res[k-1][1])
                s += sum(euDis(res[k-1][0], res[k-1][1][t])**2 for t in xrange(n))
            se[k-1].append(s/len(vals))
    for x in se:
        for y in x:
            print y,'\t',
        print 
        
        
        
        
