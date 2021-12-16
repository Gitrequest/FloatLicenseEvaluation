import csv

#GlobalVariables
names = []
dates = []
events = []
filterX = 0
u_names = None
n_filter = None
total_filtered = []


#Cut datalist into small lists
def ReadCSV(data):
    for line in data:
        if line[0] != "Name":
            total_filtered.append(line)
            names.append(line[0])
            dates.append(line[1])
            events.append(line[2])
            u_names = set(names)
            n_filter = len(names) - len(u_names)

    MaxLogins(events, dates)

# Max Logins Overall function
def MaxLogins(events, dates):
    counter = 0
    u_dates = LoginsPerDay(dates)
    maxlogin = 0
    for line in events:
        if line == "login":
            counter += 1
            if counter > maxlogin:
                maxlogin = counter
        elif line == "logout":
            counter -= 1

    print(f'Maximal usage of the license simultaneously: {maxlogin} in a span of {len(u_dates)} workdays.')
#############################
# NOT FINISHED
#Logins per day function
def LoginsPerDay(dates):
    counter2 = 0
    dates_filtered = []
    for line in dates:
        dates_filtered.append(line[0:10])

    for line in dates_filtered:
        if line == "03.01.2021":
            counter2 += 1

    u_dates = set(dates_filtered)
    u_dates = sorted(u_dates)
    return u_dates

    #print(u_dates)
    #print(counter2)
###############################


# Read the CSV and cast it as list(string) into data -> Call ReadCSV function
try:
    data = list(csv.reader(open('Testdaten.sortiert.csv'), delimiter=','))
    data[1][1]
    ReadCSV(data)

except IndexError:
    data = list(csv.reader(open('Testdaten.sortiert.csv'), delimiter=';'))
    data[1][1]
    ReadCSV(data)
