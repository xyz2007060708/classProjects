def align(v, w):
    extgap = -0.5
    newgap = -1+extgap
    matrixN = [[[0.0,0.0,0.0]]]
    matrixD = [['']]
    for i in xrange(len(v)):
        matrixN[0].append([extgap*(i+1)-1,-100000.0,extgap*(i+1)-1])
        matrixD[0].append('')
    for i in xrange(len(w)):
        matrixN.append([[-100000.0,extgap*(i+1)-1,extgap*(i+1)-1]])
        matrixD.append([''])
    for i in xrange(1,len(w)+1):
        for j in xrange(1,len(v)+1):
            eleN = []
            #calculating values coming from left
            if matrixN[i-1][j-1][2] + newgap < matrixN[i][j-1][0] + extgap:
                eleN.append(matrixN[i][j-1][0] + extgap)
            else:
                eleN.append(matrixN[i-1][j-1][2] + newgap)
            #calculating values coming from up
            if matrixN[i-1][j-1][2] + newgap < matrixN[i-1][j][1] + extgap:
                eleN.append(matrixN[i-1][j][1] + extgap)
            else:
                eleN.append(matrixN[i-1][j-1][2] + newgap)
            #calculating all valuess
            maxN = matrixN[i-1][j-1][2]
            if v[j-1] == w[i-1]:
                maxN += 1
            else:
                maxN -= 1
            eleN.append(maxN)
            if maxN >= eleN[0]:
                if maxN >= eleN[1]:
                    eleN[2] = maxN
                    eleD = 'a'
                else:
                    eleN[2] = eleN[1]
                    eleD = 'u'
            else:
                if eleN[0] >= eleN[1]:
                    eleN[2] = eleN[0]
                    eleD = 'l'
                else:
                    eleN[2] = eleN[1]
                    eleD = 'u'
            #append new element
            matrixN[i].append(eleN)
            matrixD[i].append(eleD)
    return matrixN, matrixD

def printRes(v, w, y):
    vRes = []
    wRes = []
    i = len(w)
    j = len(v)
    vindex = len(v)-1
    windex = len(w)-1
    while y[i][j] != '':
        if y[i][j] == 'a':
            vRes.append(v[vindex])
            wRes.append(w[windex])
            i -= 1
            j -= 1
            vindex -= 1
            windex -= 1
        elif y[i][j] == 'u':
            vRes.append('_')
            wRes.append(w[windex])
            i -= 1
            windex -= 1
        else:
            vRes.append(v[vindex])
            wRes.append('_')
            j -= 1
            vindex -= 1
    print list(reversed(vRes))
    print list(reversed(wRes))

if __name__ == '__main__':
    v = ['T','A','C','G','G','G','T','A','T']
    w = ['G','G','A','C','G','T','A','C','G']
    x, y = align (v,w)
    for t in x:
       ## for x in t:
       ##     print x[2],
        print t
    print '----------------------------------------------------'
    for t in y:
        print t
    print '---------------------------------------------------'
    printRes(v,w,y)