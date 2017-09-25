#our unit of time here, is going to be
#one minute, and we're going to run for one week
SIM_TIME=10

DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

hour_array=["00","01", "02", "03", "04", "05", "06",
              "07","08", "09", "10", "11", "12", "13",
              "14","15", "16", "17", "18", "19", "20",
              "21","22", "23"]

current_day_hour_minute=None

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def get(self, name):
        return_item=None
        object_list=[item for item in self.items if item.name==name]
        if len(object_list) > 0:
            return_item=object_list[0]
        #remove item from list
        self.items=[item for item in self.items if item.name!=name]

        return return_item

    def size(self):
        return len(self.items)

    def peek(self, name):
        return_item = None
        object_list = [item for item in self.items if item.name == name]
        if len(object_list) > 0:
            return_item = object_list[0]
        return return_item

class PatrolCar(object):
    def __init__(self,car_number,latlon):
        self.name=car_number
        print("New Car %d assigned pos %.4f %.4f" % (car_number, latlon.lat, latlon.lon))
        self.current_latlon=latlon
        self.patrol_latlon=latlon
        self.call_wait=0
        self.move_wait=0
        self.on_call=False
        self.call=None
        self.car_removed=False

class LatLon(object):
    def __init__(self, lat, lon):
        self.lat=lat
        self.lon=lon

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
        this_hour = ScheduleHour(this_day, this_hour, h)
        schedule.append(this_hour)
        h += 1

car_pool = Queue()
car_one = PatrolCar(1,LatLon(33.448,-112.083))
car_pool.enqueue(car_one)
car_two = PatrolCar(2,LatLon(33.466,-112.100))
car_pool.enqueue(car_two)


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
