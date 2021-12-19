import csv
import matplotlib.pyplot as plt

def readf():
    try:
        data = list(csv.reader(open('Testdaten.sortiert.csv'), delimiter=','))
        data[1][1] #Test for Indexerror
        return data

    except IndexError:
        data = list(csv.reader(open('Testdaten.sortiert.csv'), delimiter=';'))
        data[1][1] #Test for Indexerror
        return data

def maxlogins(events):
    counter = 0
    maxlogin = 0
    for line in events:
        if line == "login":
            counter += 1
            if counter > maxlogin:
                maxlogin = counter
        elif line == "logout":
            counter -= 1
    return maxlogin

def loginpd(n, dates, events):
    counter = 0
    maxlogs = 0
    datetocheck = n
    for num, x in enumerate(dates):
        if datetocheck == x:
            if events[num] == "login":
                counter += 1
                if counter > maxlogs:
                    maxlogs = counter
            elif events[num] == "logout":
                counter -= 1
    return maxlogs

def showgraph(logspdd):
    flag = 0
    while flag == 0:
        answer = input("Do you want to see a graph with max logins per day?\n [1] Yes \n [2] No\n")
        if answer == "1":
            plt.title(label="max concurrent logins/day")
            plt.bar(range(len(logspdd)), list(logspdd.values()), align='center')
            plt.xticks(rotation=30)
            plt.xticks(range(len(logspdd)), list(logspdd.keys()))
            plt.show()
            flag = 1
        elif answer == "2":
            print(logspdd)
            flag = 1

        else:
            print("Wrong input. Try again.")
