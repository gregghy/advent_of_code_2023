#12 red, 13 green, 14 blue
import regex

def cubi(filename):
    r = open(filename, "r")
    matrix = []
    maxred = 12
    maxgreen = 13
    maxblue = 14
    num = 0

    for i in r:
        i = i.replace(":", ";")
        infos = i.split(";")
        matrix.append(infos)

    for i in matrix:
        tmp = i[0][5:]
        valid = True
        
        for j in i[1:]:
            cubes = regex.findall(r'\d+\s+[red|green|blue]', j)
            for k in cubes:
                match k[-1]:
                    case 'r':
                        if int(k[:2]) > maxred:
                            valid = False
                            break
                    case 'g':
                        if int(k[:2]) > maxgreen:
                            valid = False
                            break
                    case 'b':
                        if int(k[:2]) > maxblue:
                            valid = False
                            break

        if valid:
            num = num + int(tmp)

    return num

print(cubi("input1.txt"))

def power(filename):
    r = open(filename, "r")
    matrix = []
    num = 0

    for i in r:
        i = i.replace(":", ";")
        infos = i.split(";")
        matrix.append(infos)

    for game in matrix:
        rmax = 0
        bmax = 0
        gmax = 0
        for j in game[1:]:
            cubes = regex.findall(r'\d+\s+[red|green|blue]', j)
            for k in cubes:
                match k[-1]:
                    case 'r':
                        if int(k[:2]) > rmax:
                            rmax = int(k[:2])
                    case 'g':
                        if int(k[:2]) > gmax:
                            gmax = int(k[:2])
                    case 'b':
                        if int(k[:2]) > bmax:
                            bmax = int(k[:2])
        power = rmax * bmax * gmax
        num = num + power

    return num

print(power("input1.txt"))
