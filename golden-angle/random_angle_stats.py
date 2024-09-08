import random

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

random.seed(0)
diffvarsumsum = 0
numtrial = 100
for t in range(numtrial):
    diffvarsum = 0
    lst = []
    for i in range(1, 501):
        newangle = 0
        if i > 1:
            newangle = random.randint(0, 3600) / 10
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
            print('%3d, %.2f' % (t + 1, diffvarsum))
    diffvarsumsum += diffvarsum

diffvarsumavg = diffvarsumsum / numtrial
print('\nrandom angle avg => %.2f' % (diffvarsumavg))
