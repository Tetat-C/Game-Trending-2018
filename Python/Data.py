"""Read Data"""

def ReadAndWrite():
    """Read And Write Data"""

    data = open("Data_Fixed.txt", 'r')
    yourResult = [line.split(',') for line in data.readlines()]
    print(yourResult)

ReadAndWrite()