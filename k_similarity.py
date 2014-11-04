#Dynamic programming for computing k-similarity
#Two input spectra are given as lists of integers
#Suppose s1 and s2 have the same length

def BaseCase(s1, s2):
    n = len(s1)
    res = 0
    D = [[0 for i in xrange(n)] for j in xrange(n)] #construct the real result table
    M = [[0 for i in xrange(n)] for j in xrange(n)] #construct the max num table
    #initialize the table when k = 0, i.e. main diagonal 
    for i in xrange(1,n):
        for j in xrange(1,n):
            (pi, pj) = diag(s1,s2,i,j)
            if s1[i] == s2[j]:
                D[i][j] = D[pi][pj] + 1
            M[i][j] = max(D[i][j], M[i-1][j], M[i][j-1])
    return D, M

def nextKSim(s1, s2, D, M):
    for i in xrange(1,len(s1)):
        for j in xrange(1,len(s1)):
            (pi, pj) = diag(s1,s2,i,j)
            D[i][j] = max(D[pi][pj] + 1, M[i-1][j-1]+1)
    #Now update the max number table M(k-1) to M(k)
    for i in xrange(1,len(s1)):
        for j in xrange(1,len(s1)):
            M[i][j] = max(D[i][j], M[i-1][j], M[i][j-1])
    
    
def diag(s1, s2, ind1, ind2):  #find the position of the previous '1' on the same diagonal
    i = ind1 - 1
    j = ind2 - 1
    while i >= 0 and j >= 0:
        if s1[ind1] - s1[i] < s2[ind2] - s2[j]:
            i -= 1
        elif s1[ind1] - s1[i] > s2[ind2] - s2[j]:
            j -= 1
        else:
            return (i,j)
    return (0,0)
    
if __name__ == '__main__':
    s1 = [0, 115, 133, 262, 264, 377, 383, 496, 498, 627, 645, 760] #0 added at front for initial conditions
    s2 = [0, 115, 133, 264, 280, 383, 395, 498, 514, 645, 663, 778]
    s3 = [0, 115, 133, 280, 337, 395, 456, 514, 571, 718, 736, 851]
    a = [0, 10, 15, 30, 35, 50, 55, 70, 75, 90, 95]
    b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    a = [0,7,11,15,18,21,24,30,38,43]
    b = [0,7,11,13,19,22,25,31,33,38]
    #a = [0, 98, 133,  246,  254,  355,  375 , 476,  484,  597,  632]
    #b = [0, 98, 133,  284,  296,  385,  425 , 514,  526,  677,  712]
    a = s1
    b = s3
    x, y = BaseCase(a, b)
    for i in x:
        print i
    print '------------------'
    for i in y:
        print i
    print '------------------'
    
    print '0-similarity' 
    print max(max(p) for p in x)
    
    for i in xrange(5):
        nextKSim(a,b,x,y)
        print '%s-similarity' %(i+1)
        print max(max(p) for p in x)
        
            
            
    
