
li=['gcc.trace','gzip.trace','mcf.trace','swim.trace','twolf.trace']
for i in li:
    mf = open(i, "r")
    print("File to read: ", mf.name)
    print("------------------------------------")
    file_content=mf.readlines()

# The cache contains 3^13 sets named set0, set1, set2... and so on. So we create a list of list to simulate the cache
    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on
                #this cache is a dictionary here where it's keys store the the index bits and it's value is a 2d-list which store tag and the valid bits

    for i in file_content:
        x = i.split()
        b="{:032b}".format(int(x[1],16))
    
        if b[13:30] in cache:
            if [1,b[0:13]] in cache[b[13:30]]:      # the index maps to a list of 4 terms consisting of (valid bit, tag bit)
                hit=hit+1
                #LRU
                cache[b[13:30]].pop(cache[b[13:30]].index([1,b[0:13]]))
                cache[b[13:30]].append([1,b[0:13]])
            else:
                miss=miss+1
                cache[b[13:30]].pop(0)
                cache[b[13:30]].append([1,b[0:13]])
        else:
            miss=miss+1
            cache[b[13:30]]=[[0,00000000000000000],[0,00000000000000000],[0,00000000000000000]]
            cache[b[13:30]].append([1,b[0:13]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ",hit/miss)
    print()