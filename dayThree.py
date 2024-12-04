import re

def getData():

    corruptedString = ""

    f = open("dayThreeInput.txt", "r")

    for line in f:
        corruptedString += line

    return re.sub("\n","",corruptedString)

def task1(data):

    valid = re.findall("mul\(\d{1,3},\d{1,3}\)", data)

    return processMultiplication(valid)

def processMultiplication(list):

    total = 0

    for calc in list:
        calc = calc[4:-1]
        calc = calc.split(",")

        total  += (int(calc[0]) * int(calc[1]))

    return total

def task2(data):

    processed = re.sub("don't\(\).*?do\(\)","do()", data)

    while re.search("don't\(\)", processed):
        processed = re.sub("don't\(\).*?do\(\)","do()", processed)

    return task1(processed)
    

if __name__ == "__main__":

    data = getData()

    print(f"Task 1: {task1(data)}")

    print(f"Task 2: {task2(data)}")





