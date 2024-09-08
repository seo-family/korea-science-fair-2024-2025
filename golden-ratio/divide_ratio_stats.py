import math

def findmax(lst):
    if len(lst) == 0:
        return [0, 1]
    else:
        maxdiff = lst[0]
        maxval = 0
        for i in range(len(lst)):
            a = lst[i]
            b = 1 if i == len(lst) - 1 else lst[i + 1] 
            diff = abs(b - a)
            if diff > maxdiff:
                maxdiff = diff
                maxval = lst[i]
        return [maxval, maxdiff]

def getvar(lst):
    lstlen = len(lst)
    if lstlen == 0:
        return 0

    valsum = 0
    for m in range(lstlen):
        valsum += lst[m]
    valavg = valsum / lstlen
    
    valsqsum = 0
    for n in range(lstlen):
        valsqsum += lst[n] ** 2
    valsqavg = valsqsum / lstlen

    valvar = valsqavg - valavg ** 2
    return valvar

diffvarsum = 0
lst = []
for i in range(1, 501):
    ret = findmax(lst)
    #print('findmax', ret)
    maxval = ret[0]
    maxdiff = ret[1]
    divide = maxval + maxdiff / 2
    newratio = divide - math.floor(divide)
    #print(newratio)
    lst.append(newratio)
    lst.sort()
    #print(lst)

    diff = []                    
    for l in range(0, i - 1):
        diff.append(lst[l + 1] - lst[l])
    #print(diff)
        
    diffvar = getvar(diff)
    diffvarsum += diffvar
    if i == 500:
        print('divide ratio => %.4f' % (diffvarsum))
