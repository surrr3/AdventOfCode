# Get input from file and split into array
def getData():

    reports = []

    f = open("dayTwoInput.txt", "r")

    for line in f:
        reports.append(line.split(" "))

    return reports

'''
Checks if a report is "safe" - returns True if safe, False otherwise

Report only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

'''
def checkSafeReport(report):

    if len(report) <=1:
        return True

    # check if ascending or descending
    ascending = int(report[0]) < int(report[1])

    # go through 2 at a time and check difference
    for index,val in enumerate(report[1:]):

        diff = int(val) - int(report[index])

        if ascending:
             if diff < 1 or diff > 3:
                return False
        else:
            if diff > -1 or diff < -3:
                return False

    return True

'''
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe

Returns True if safe, False if not

'''
def problemDampener(report):
    
    # remove one item at a time and re-check
    for i in range(len(report)):

        newReport = report[:i] + report[i+1:]

        if checkSafeReport(newReport):
            return True
        
    return False

def task1(data):

    count = 0

    for line in data:

        if checkSafeReport(line):
            count+=1

    return count

def task2(data):

    count = 0

    for line in data:

        if checkSafeReport(line):
            count+=1
        else:
            if problemDampener(line):
                count+=1

    return count


if __name__ == "__main__":

    data = getData()

    print(f"Task 1 Answer: {task1(data)}")


    print(f"Task 2 Answer: {task2(data)}")



