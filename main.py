from pprint import pprint
global request_day
request_day= {  # Zadanie wolnego od D
    1: [4,5,6],
    2: [],
    3: [4,5,11,12],
    4: [4,5,6,7,8,9,10,11]
}
global request_night
request_night= {  # Zadanie wolnego od N
    1: [4,5],
    2: [],
    3: [3,11,12],
    4: [3,4,5,6,7,8,9,10,11]
}
global time_of_break_day
global time_of_break_night
time_of_break_day = [] # zmeczenie liczone od 7:00, dnia 1 - index 1
time_of_break_night = [] # zmeczenie liczone od 19:00, dnia 1 - index 1
global calendar
calendar = []
for j in range(0,31):
    calendar.append([0, 0])
    time_of_break_day.append([0, 0, 0, 0])
    time_of_break_night.append([0, 0, 0, 0])
calendar = dict(enumerate(calendar, 0))
time_of_break_day = dict(enumerate(time_of_break_day, 0))
time_of_break_night = dict(enumerate(time_of_break_night, 0))
calendar.update({0: [3,1]})
time_of_break_day.update({0: [12,3*24,0,24]})
time_of_break_night.update({0: [0,3*24+12,12,24+12]})


def shifter(day_of_month, request_day, request_night, calendar, time_of_break_day, time_of_break_night):
    i = 0
    while(calendar[day_of_month][0] == 0):
        l1 = time_of_break_night[day_of_month-1]
        list = [l1.index(x)+1 for x in sorted(l1,reverse=True)]
        print(list)
        wybraniec_id = list[i]
        if(not(day_of_month in request_day[wybraniec_id])):
            calendar.update({day_of_month: [wybraniec_id,calendar[day_of_month][1]]})
            time_of_break_day[1][wybraniec_id-1] = 0
            break
        i+=1
    for j in range(len(time_of_break_day[day_of_month])):
        if j==wybraniec_id-1:
            time_of_break_day[day_of_month][j] = 0
        else:
            time_of_break_day[day_of_month][j] = time_of_break_night[day_of_month-1][j]+12
    wybraniec_id = 0
    i = 0
    while (calendar[day_of_month][1] == 0):
        l2 = time_of_break_day[day_of_month]
        list = [l2.index(x) + 1 for x in sorted(l2, reverse=True)]
        # print(list)
        wybraniec_id = list[i]
        #print(wybraniec_id)
        if (not (day_of_month in request_night[wybraniec_id])):

            calendar.update({day_of_month: [calendar[day_of_month][0],wybraniec_id]})
            time_of_break_day[1][wybraniec_id - 1] = 0
            break
        i += 1
    for j in range(len(time_of_break_night[day_of_month])):
        if j==wybraniec_id-1:
            time_of_break_night[day_of_month][j] = 0
        else:
            time_of_break_night[day_of_month][j] = time_of_break_day[day_of_month][j]+12
for o in range(1,30):
    shifter(o, request_day, request_night, calendar, time_of_break_day, time_of_break_night)
print(calendar)
print(time_of_break_day)
print(time_of_break_night)
