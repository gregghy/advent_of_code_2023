def calibration(file_name):
    r = open(file_name, "r")
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = 0
    for i in r:
        pair = ""
        for j in i:
            if j in digits:
                pair += j
                break
        i = i[::-1]
        for j in i:
            if j in digits:
                pair += j
                break

        num = num + int(pair)

    return num

print(calibration("input1.txt"))

import regex
def calibration2(file_name):
    r = open(file_name, "r")
    digits = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }

    num = 0

    for i in r:
        numbers = regex.findall(r'0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine', i, overlapped=True)

        if numbers[0].isdigit() == False:
            numbers[0] = digits[numbers[0]]
        if numbers[-1].isdigit() == False:
            numbers[-1] = digits[numbers[-1]]

        pair = str(numbers[0]) + str(numbers[-1])

        num = num + int(pair)

    return num

print(calibration2("input1.txt"))






