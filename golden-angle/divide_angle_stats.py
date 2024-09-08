def findmax(lst):
    if len(lst) <= 1:
        return [0, 360]
    else:
        maxdiff = 0
        maxval = 0
        for i in range(len(lst)):
            a = lst[i]
            b = lst[(i + 1) % len(lst)]
            diff = abs(b - a) if b >= a else b + 360 - a
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
    newangle = 0
    if i > 1:
        ret = findmax(lst)
        maxval = ret[0]
        maxdiff = ret[1]
        newangle = maxval + maxdiff / 2
    #print(newangle)
    lst.append(newangle)
    lst.sort()
    #print(lst)

    diff = []                    
    for l in range(0, i - 1):
        diff.append(lst[l + 1] - lst[l])
    diff.append(360 - lst[i - 1])
    #print(diff)

    diffvar = getvar(diff)
    diffvarsum += diffvar
    if i == 500:
        print('divide angle => %.2f' % (diffvarsum))


    
    
    
    
