def greedyChange(M, d):
    r = M  #record the residual amount
    res = []  #result
    for x in d:
        res.append(r // x)
        r %= x
    return res

def xsChange(M, d):
    methods = []    #record all correct solutions
    leaf = [0 for i in d]
    if M == 0:
        return [leaf]
    leaf[0] = 1
    min_coin = 99
    limit = searchSpace(M, d)
    while True:
        if sum(leaf) == 0:
            break
        #calculate sum
        coin_sum = 0
        for i in xrange(len(d)):
            coin_sum += leaf[i] * d[i]
        if coin_sum == M:
            methods.append([x for x in leaf])
            if sum(leaf) < min_coin:
                min_coin = sum(leaf)
        #iterate
        for i in xrange(len(d)):
            if leaf[i] + 1 > limit[i]:
                leaf[i] = 0
            else:
                leaf[i] += 1
                break
    #choose optimal solutions
    res = []
    for x in methods:
        if sum(x) == min_coin:
            res.append(x)
    return res

def searchSpace(M, d):
    res = [M // d[0]] # first element
    for i in xrange(1, len(d)):
        for x in xrange(d[i-1] // d[i], M // d[i] + 1):
            if (x * d[i]) % d[i-1] == 0:
                res.append(x - 1)
                break
        else:
            res.append(M // d[i])
    return res

def isGreedyOK(d):
    return all(greedyChange(x,d) in xsChange(x, d) for x in xrange(100))

def avgCoinsChange(d):
    res = map(lambda x: xsChange(x, d)[0], range(100))
    return sum(map(sum, res))/100.0

if __name__ == '__main__':
    isGreedyOK([25,10,5,1]) #US coin
    isGreedyOK([50,20,10,5,2,1]) #Euro
    avgCoinsChange([25,10,5,1]) #US
    avgCoinsChange([50,20,10,5,2,1]) #Euro
    
    
