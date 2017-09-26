#our unit of time here, is going to be
#one minute, and we're going to run for one week
SIM_TIME=7*24*60

DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

hour_array=["00","01", "02", "03", "04", "05", "06",
              "07","08", "09", "10", "11", "12", "13",
              "14","15", "16", "17", "18", "19", "20",
              "21","22", "23"]

current_day_hour_minute=None


class DayHourMinute(object):
    def __init__(self, day_string, hour_string, minute_string):
        self.day=day_string
        self.hour=hour_string
        self.minute=minute_string


class ScheduleHour(object):
    def __init__(self, day, hour, index):
        self.day = day
        self.hour = hour
        self.index = index

####START SIM RUN
hour=0
schedule = []

h=0
for this_day in DOW:
    for this_hour in hour_array:
        temp_hour = ScheduleHour(this_day, this_hour, h)
        schedule.append(temp_hour)
        h += 1



for i in range(1, SIM_TIME):
    if i % 60 == 0:
        print("Another hour has passed. Last hour %d" % hour)
        hour+=1
        print("This hour: %d" % hour)

    day_index = DOW.index(schedule[hour].day)
    current_day_hour_minute = DayHourMinute(schedule[hour].day,
                                            schedule[hour].hour, str(i - int(schedule[hour].hour) * 60
                                                                  - (1440 * day_index)))

    print("Day %s Hour %s Minute %s " % (current_day_hour_minute.day,
                                         current_day_hour_minute.hour,
                                         current_day_hour_minute.minute))
