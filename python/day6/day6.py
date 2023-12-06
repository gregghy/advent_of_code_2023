def boats(filename):
    f = open(filename, "r")
    lines = []
    for i in f:
        lines.append(i)
    
    time = []
    dist = []
    for i in lines:
        b = 11
        e = 15
        for j in range(4):
            x = i[b:e]
            time.append(x)
            b += 7
            e += 7
        b = 11
        e = 15
        for j in range(4):
            x = lines[1][b:e]
            dist.append(x)
            b += 7
            e += 7
        break

    tot = 1
    for i in time:
        poss = 0
        for j in range(int(i)):
            distance = j*(int(i)-j)
            if distance > int(dist[time.index(i)]):
                poss += 1

        tot = tot * poss
    
    #part 2
    big_time = ''
    for i in time:
        big_time = big_time + i.strip()
    big_dist = ''
    for i in dist:
        big_dist = big_dist + i.strip()
    poss = 0
    for j in range(int(big_time)):
        distance = j*(int(big_time)-j)
        if distance > int(big_dist):
            poss +=1
    
    print(tot)
    print(poss)
boats("input.txt")
