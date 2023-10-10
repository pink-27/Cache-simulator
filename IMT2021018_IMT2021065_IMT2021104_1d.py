li=['gcc.trace','gzip.trace','mcf.trace','swim.trace','twolf.trace']
for i in li:
    mf = open(i, "r")
    print("File to read: ", mf.name)
    print("------------------------------------")
    file_content=mf.readlines()

    # The cache contains 3^15 sets named set0, set1, set2... and so on. So we create a list of list to simulate the cache
    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                    #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on
                    #this cache is a dictionary here where it's keys store the the index bits and it's value is a 2d-list which store tag and the valid bits

    print("---1-way Set Associative:---")
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
            cache[b[13:30]]=[]
            cache[b[13:30]].append([1,b[0:13]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ", hit/miss)
    print()
    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                    #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on

    print("---2-way Set Associative:---")
    for i in file_content:
        x = i.split()
        b="{:032b}".format(int(x[1],16))
        
        if b[14:30] in cache:
            if [1,b[0:14]] in cache[b[14:30]]:      # the index maps to a list of 4 terms consisting of (valid bit, tag bit)
                hit=hit+1
                #LRU
                cache[b[14:30]].pop(cache[b[14:30]].index([1,b[0:14]]))
                cache[b[14:30]].append([1,b[0:14]])
            else:
                miss=miss+1
                cache[b[14:30]].pop(0)
                cache[b[14:30]].append([1,b[0:14]])
        else:
            miss=miss+1
            cache[b[14:30]]=[[0,00000000000000]]
            cache[b[14:30]].append([1,b[0:14]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ", hit/miss)
    print()
    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                    #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on

    print("---4-way Set Associative:---")
    for i in file_content:
        x = i.split()
        b="{:032b}".format(int(x[1],16))

        if b[15:30] in cache:
            if [1,b[0:15]] in cache[b[15:30]]:      # the index maps to a list of 4 terms consisting of (valid bit, tag bit)
                hit=hit+1
                #LRU
                cache[b[15:30]].pop(cache[b[15:30]].index([1,b[0:15]]))
                cache[b[15:30]].append([1,b[0:15]])
            else:
                miss=miss+1
                cache[b[15:30]].pop(0)
                cache[b[15:30]].append([1,b[0:15]])
        else:
            miss=miss+1
            cache[b[15:30]]=[[0,000000000000000],[0,000000000000000],[0,000000000000000]]
            cache[b[15:30]].append([1,b[0:15]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ", hit/miss)
    print()

    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                    #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on

    print("---8-way Set Associative:---")
    for i in file_content:
        x = i.split()
        b="{:032b}".format(int(x[1],16))
    
        if b[16:30] in cache:
            if [1,b[0:16]] in cache[b[16:30]]:      # the index maps to a list of 4 terms consisting of (valid bit, tag bit)
                hit=hit+1
                #LRU
                cache[b[16:30]].pop(cache[b[16:30]].index([1,b[0:16]]))
                cache[b[16:30]].append([1,b[0:16]])
            else:
                miss=miss+1
                cache[b[16:30]].pop(0)
                cache[b[16:30]].append([1,b[0:16]])
        else:
            miss=miss+1
            cache[b[16:30]]=[[0,0000000000000000],[0,000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000]]
            cache[b[16:30]].append([1,b[0:16]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ", hit/miss)
    print()

    hit=0
    miss=0
    cache = {}      #index1 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit))
                    #index2 ---> ((valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit),(valid bit,tag bit)) and so on
    print("---16-way Set Associative:---")

    for i in file_content:
        x = i.split()
        b="{:032b}".format(int(x[1],16))
    
        if b[17:30] in cache:
            if [1,b[0:17]] in cache[b[17:30]]:      # the index maps to a list of 4 terms consisting of (valid bit, tag bit)
                hit=hit+1
                #LRU
                cache[b[17:30]].pop(cache[b[17:30]].index([1,b[0:17]]))
                cache[b[17:30]].append([1,b[0:17]])
            else:
                miss=miss+1
                cache[b[17:30]].pop(0)
                cache[b[17:30]].append([1,b[0:17]])
        else:
            miss=miss+1
            cache[b[17:30]]=[[0,00000000000000000],[0,00000000000000000],[0,00000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000],[0,0000000000000000]]
            cache[b[17:30]].append([1,b[0:17]])

    print("hits = ", hit)
    print("misses = ", miss)
    print("hit% = ", hit/(miss+hit)*100)
    print("miss% = ", 100-hit/(miss+hit)*100)
    print("hit/miss = ", hit/miss)
    print()