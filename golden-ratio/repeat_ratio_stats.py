import math

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

for r in range(500, 802, 2):
    diffvarsum = 0
    lst = []
    for i in range(1, 501):
        newratio = r / 1000 * i % 1
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
            print('%.3f, %.4f' % (r / 1000, diffvarsum))
