"""
Construct a python program that, given a directed graph, yields a Eulerian path or None, if no such 
path exists.  The directed graph is given as an unordered sequence of graph edges.  Each edge is a 
triple of the form (v,w,l) denoting a directed edge from vertex v to vertex w with edge label.  A 
Eulerian path is the triple (v,s,w) where v is the start vertex of the path, s is the sequence of labels 
of edges traversed in the path and w is the final vertex of the path. 
Example input:      [('a','b',1), ('b','c',2), ('c','a',3)] 
Output (one of several possible):  ('a', [1,2,3], 'a')
"""
"""
Idea: 
First find a path by extending the first edge from the input 
If the path found was not the entire path, there must be additional paths connected with the one found if there actually exists a Eulerian path
We can just keep extending the first path to get the entire path
"""
def euler(g):
    if len(g) == 0:
        return None
    path = FirstPath(g)
    if len(g) == 0: #the one found is the entire eulerian path
        return path
    while len(g) != 0:
        x = FindMorePath(path,g)
        if x == None:
            return None
        else:
            (pExt, status, pos) = x
        if path[0] == path[-1]:
            path = ExtendCirclePath(path, pExt, status, pos) #you can always add an additional path to a circular path
        else:
            path = ExtendNonCirclePath(path, pExt, status, pos)
        if path == 0:
            return None
    return (path[0], path[1::2] ,path[-1])
    
    
def FirstPath(g):
    (start,end,num) = g.pop(0)
    path = [start,num,end]
    while len(g) != 0:
        for i in xrange(len(g)):
            (s,e,n) = g[i]
            if s == path[-1]:
                path += [n,e]
                g.pop(i)
                break
            if e == path[0]:
                path = [s,n] + path
                g.pop(i)
                break
        else:
            break
    return path
            
def ExtendCirclePath(p, pExt, status, i):
    if pExt[0] == pExt[-1]:
        p = p[:i] + pExt[:-1] + p[i:]
    else:
        if status == 1:
            p = p[i:-1] + p[0:i] + pExt
        else:
            p = pExt + p[i+1:-1] + p[0:i+1] 
    return p
    
def ExtendNonCirclePath(p, pExt, status, i):
    if pExt[0] == pExt[-1]:
        p = p[:i] + pExt[:-1] + p[i:]
        return p
    if status == 1: #the to-be-added path starts from one vertex in p
        if pExt[-1] != p[0]: #the last element of pExt has to be the same with the first of p, otherwise there is no eulerian path
            return 0
        else:
            p = pExt + p[1:]
    if status == 0: #the to-be-added path ends at one vertex in p
        if pExt[0] != p[-1]:
            return 0
        else:
            p += pExt[1:]
    return p

def FindMorePath(p, g): #find additional paths starting from vertices in p or ending at vertices in p
    pExt, status, pos = FindFirstOfNew(p, g)
    if len(pExt) == 0:  #there are not paths connected with the one we found
        return None
    while len(g) != 0:  #extend the additional path
        for i in xrange(len(g)):
            (s,e,n) = g[i]
            if status == 1 and s == pExt[-1]:
                pExt += [n,e]
                g.pop(i)
                break
            if status == 0 and e == pExt[0]:
                pExt = [s,n] + pExt
                g.pop(i)
                break
        else:
            break
    return pExt, status, pos

def FindFirstOfNew(p, g):
    pExt = []
    for j in xrange(0, len(p), 2):
        for i in xrange(len(g)):
            (s,e,n) = g[i]
            if p[j] == s: #there is an additional path starting from vertices in p
                pExt = [s,n,e]
                g.pop(i)
                status = 1
                pos = j #record which vertex the additional path starts from
                return pExt, status, pos
            if p[j] == e: #there is an additional path ending at vertices in p
                pExt = [s,n,e]
                g.pop(i)
                status = 0
                pos = j #record which vertex the additional path ends at
                return pExt, status, pos
    return pExt, -1, -1

if __name__ == '__main__':
    l = [('a','b',1), ('b','c',2), ('c','j',17),('j','c',18),('c','d',3),('d','e',4),('e','f',5),
         ('f','g',6), ('g','a',19),('d','h',7), ('h','i',8),('i','j',9),('j','d',10),
         ('b','k',11), ('k','l',12), ('l','m',13), ('m','b',14),('e','h',15),('h','e',16)]
    m = [('a','b',1), ('b','c',2), ('c','d',3),('d','e',4),('e','f',5),
         ('f','g',6), ('g','a',11),('d','h',7), ('h','i',8),('i','j',9),('j','d',10),('z','y',50)]
    for i in xrange(len(l)):
        x = l[:i] + l[i:]
        y = m[:i] + m[i:]
        #print x
        print euler(x)
        print euler(y)
   # print euler(l)