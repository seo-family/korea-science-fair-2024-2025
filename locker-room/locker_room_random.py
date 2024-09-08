import random

numlockers = 300
maxpeople = 100
lockers = [-1 for i in range(numlockers)]

def random_hash(n):
    return random.randint(0, n - 1)

def avg_dist():
    previd = -1
    sumdist = 0
    numdist = 0
    for i in range(len(lockers)):
        if lockers[i] != -1:
            if previd != -1:
                sumdist += i - previd
                numdist += 1
            previd = i
    avgdist = sumdist / numdist if numdist > 0 else 0
    return avgdist

def minmax_dist():
    previd = -1
    mindist = 0
    maxdist = 0
    for i in range(len(lockers)):
        if lockers[i] != -1:
            if previd != -1:
                dist = i - previd
                if mindist == 0 or dist < mindist:
                    mindist = dist
                if maxdist == 0 or dist > maxdist:
                    maxdist = dist
            previd = i
    return [mindist, maxdist]

def lockers_bmap():
    bmap = ''
    for i in range(len(lockers)):
        bmap += '1' if lockers[i] != -1 else '0'
    return bmap


random.seed(0)
time = 0
numpeople = 0
while numpeople < maxpeople:
    numpeople += 1
    lockerid = random_hash(numlockers)
    while lockers[lockerid] != -1:
        lockerid = random_hash(numlockers)
            
    lockers[lockerid] = time

    avgdist = avg_dist()
    minmaxdist = minmax_dist()
    print('%d, %d, %d, %d, %.2f' % (time, numpeople, minmaxdist[0], minmaxdist[1], avgdist))
    #bmap = lockers_bmap()
    #print(bmap)
    
    time += 1
