def scratchcards(input):
    r = open(input, "r")
    lines = []
    count = 0
    instances = []
    result1 = 0
    for i in r:
        instances.append(1)
        #get winning numbers and all the numbers to check in two lists
        b = 10
        e = 12
        b1 = 42
        e1 = 44
        numbs = []
        winning_numbs = []
        for j in range(10):
            winning_numbs.append(int(i[b:e]))
            if b < 40:
                b = b + 3
                e = e + 3
        for j in range(25):
            numbs.append(int(i[b1:e1]))
            if b1 < 117:
                b1 = b1 + 3
                e1 = e1 + 3
        #count the points
        points = 0
        numbers_in = 0
        for j in numbs:
            if j in winning_numbs:
                numbers_in += 1
                if points == 0:
                    points += 1
                else:
                    points = points * 2
        result1 += points
        lines.append(numbers_in)

    #part2
    result2 = 0
    for i, points in enumerate(lines):
        print(i,points)
        result2 += instances[i]
        for j in range(1, points+1):
            instances[j+i] += instances[i]
    print(result2)

    #result2 = 0
        #for i in instances:
    #result2 = result2 + i
    return result1, result2

print(scratchcards("input.txt"))
