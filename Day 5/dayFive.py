def getData():

    rules = []

    f = open("dayFiveInput.txt", "r")

    for line in f:
        rules += [line.strip().split("|")]

    return rules



if __name__ == "__main__":

    data = getData()

    print(data)

    # print(f"Task 1: {task1(data)}")
    
    # print(f"Task 2: {task2(data)}")




