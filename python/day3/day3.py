import regex
def engine_parts(filename):
    r = open(filename, "r")
    matrix = []

    numb_of_lines = 0
    matrix.append([])
    for i in r:
        line = []
        line.append([])
        for j in i:
            c = regex.findall(r'[^a-zA-Z|.|\n]+', j)
            line.append(c)

        matrix.append(line)
        numb_of_lines +=1
    matrix.append([])
    for i in range(142):
        matrix[0].append([])
        matrix[numb_of_lines+1].append([])

    valid_numb = []
    for line in matrix:
        valid_char = ''
        validity = False
        c_index = 0
        for c in line:
            if c:
                if c[0].isdigit():
                    right_char = line[c_index+1]
                    left_char = line[c_index-1]
                    under_char = matrix[matrix.index(line)+1][c_index]
                    right_under_char = matrix[matrix.index(line)+1][c_index+1]
                    left_under_char = matrix[matrix.index(line)+1][c_index-1]
                    upper_char = matrix[matrix.index(line)-1][c_index]
                    right_upper_char = matrix[matrix.index(line)-1][c_index+1]
                    left_upper_char = matrix[matrix.index(line)-1][c_index-1]
                    
                    if valid_char == '':
                        validity = False
                        valid_char = valid_char + c[0]
                    
                    #char under
                    if under_char:
                        if under_char[0].isdigit() == False:
                            validity = True
                    #char upper
                    if upper_char:
                        if upper_char[0].isdigit() == False:
                            validity = True
                    #char right-under:
                    if right_under_char:
                        if right_under_char[0].isdigit() == False:
                            validity = True
                    #char right-upper:
                    if right_upper_char:
                        if right_upper_char[0].isdigit() == False:
                            validity = True
                    #char left:
                    if left_char:
                        if left_char[0].isdigit() == False:
                            validity = True
                    #char left-under:
                    if left_under_char:
                        if left_under_char[0].isdigit() == False:
                            validity = True
                    #char left_upper:
                    if left_upper_char:
                        if left_upper_char[0].isdigit() == False:
                            validity = True
                    #right char
                    if right_char:
                        if right_char[0].isdigit():
                            valid_char = valid_char + right_char[0]
                        elif right_char[0].isdigit() == False:
                            validity = True
                            valid_numb.append(valid_char)
                            valid_char = ''
                    else:
                        #print(c)
                        if validity:
                            valid_numb.append(valid_char)
                            valid_char = ''
                            validity = False
                        else:
                            valid_char = ''
            c_index +=1
    result = 0
    for i in valid_numb:
        result = result + int(i)

    return result

def gears(filename):
    r = open(filename, "r")
    matrix = []

    numb_of_lines = 0
    matrix.append([])
    for i in r:
        line = []
        line.append([])
        for j in i:
            c = regex.findall(r'[^a-zA-Z|.|\n]+', j)
            line.append(c)

        matrix.append(line)
        numb_of_lines +=1
    matrix.append([])
    for i in range(142):
        matrix[0].append([])
        matrix[numb_of_lines+1].append([])

    valid_numb = []
    for line in matrix:
        valid_char = ''
        validity = False
        c_index = 0
        for c in line:
            if c:
                if c[0] == '*':
                    right_char = line[c_index+1]
                    left_char = line[c_index-1]
                    under_char = matrix[matrix.index(line)][c_index]
                    right_under_char = matrix[matrix.index(line)+1][c_index+1]
                    left_under_char = matrix[matrix.index(line)+1][c_index-1]
                    upper_char = matrix[matrix.index(line)-1][c_index]
                    right_upper_char = matrix[matrix.index(line)-1][c_index+1]
                    left_upper_char = matrix[matrix.index(line)-1][c_index-1]

                    positions = []

                    if right_char:
                        if right_char[0].isdigit():
                            positions.append(right_char)
                    if left_char:
                        if left_char[0].isdigit():
                            positions.append(left_char)
                    if under_char:
                        if under_char[0].isdigit():
                            positions.append(under_char)
                    if upper_char:
                        if upper_char[0].isdigit():
                            positions.append(upper_char)
                    if left_upper_char:
                        if left_upper_char[0].isdigit():
                            positions.append(left_upper_char)
                    if right_upper_char:
                        if right_upper_char[0].isdigit():
                            positions.append(right_upper_char)
                    if left_under_char:
                        if left_under_char[0].isdigit():
                            positions.append(left_under_char)
                    if right_under_char:
                        if right_under_char[0].isdigit():
                            positions.append(right_under_char)
                    print(positions)
                    if len(positions) > 1:
                        for i in positions:
                            matrix[i].append(True)

                    print(positions)
        for c in line:
            if c:
                if c[0].isdigit():
                    right_char = line[c_index+1]
                    left_char = line[c_index-1]
                    under_char = matrix[matrix.index(line)+1][c_index]
                    right_under_char = matrix[matrix.index(line)+1][c_index+1]
                    left_under_char = matrix[matrix.index(line)+1][c_index-1]
                    upper_char = matrix[matrix.index(line)-1][c_index]
                    right_upper_char = matrix[matrix.index(line)-1][c_index+1]
                    left_upper_char = matrix[matrix.index(line)-1][c_index-1]
                    
                    if valid_char == '':
                        validity = False
                        valid_char = valid_char + c[0]
                    
                    #char under
                    if under_char:
                        if under_char[0] == '*':
                            validity = True
                    #char upper
                    if upper_char:
                        if upper_char[0] == '*':
                            validity = True
                    #char right-under:
                    if right_under_char:
                        if right_under_char[0] == '*':
                            validity = True
                    #char right-upper:
                    if right_upper_char:
                        if right_upper_char[0] == '*':
                            validity = True
                    #char left:
                    if left_char:
                        if left_char[0] == '*':
                            validity = True
                    #char left-under:
                    if left_under_char:
                        if left_under_char[0] == '*':
                            validity = True
                    #char left_upper:
                    if left_upper_char:
                        if left_upper_char[0] == '*':
                            validity = True
                    #right char
                    if right_char:
                        if right_char[0].isdigit():
                            valid_char = valid_char + right_char[0]
                        elif right_char[0] == '*':
                            validity = True
                            valid_numb.append(valid_char)
                            valid_char = ''
                    else:
                        #print(c)
                        if validity:
                            valid_numb.append(valid_char)
                            valid_char = ''
                            validity = False
                        else:
                            valid_char = ''
            c_index +=1
    result = 0
    for i in valid_numb:
        result = result + int(i)
    print(valid_numb)
    return result


print(gears("prova.txt"))
