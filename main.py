import csv
import csvlf



#Read CSV
data_raw = csvlf.readf()

###################################################################
################### GlobalVariables ###############################
###################################################################
data = []       #Placeholder for filtered CSV list
names = []      #Filtered names from data
names_s = []    #filtered unique names from data
dates_raw = []  #unmodified dates with time stamps
dates = []      #filtered dates dates from raw file
dates_s = []    #filtered unique dates
time_v = []     #filtered timestamps only for time statistics
events = []     #login/logout events filtered
logspdd = {}    #Dictionary for Date:MaxLogins values
###################################################################


#Filter Process | CSV -> Lists
for line in data_raw:
    if line[0] != "Name":
        data.append(line)
        names.append(line[0])
        dates_raw.append(line[1])
        events.append(line[2])
    else:
        print("Line filtered.")

# Cutting time from Dates and save in different lists
for line in dates_raw:
    dates.append(line[0:10])
    time_v.append(line[12:16])

# Sorting / setting uniques
names_s = set(names)
dates_s = sorted(set(dates))

#Iterates thru unigue dates and calls function to count maxlogs/day
for num, n in enumerate(dates_s):
    loginspd = csvlf.loginpd(n, dates, events)
    logspdd[n] = loginspd


# calls the function & prints the result of max logs overall
print(f'The total logins at the same time over the timespan of {len(dates_s)} days is: "  {csvlf.maxlogins(events)}')

# calls graph function
csvlf.showgraph(logspdd)
