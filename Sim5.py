import math


#our unit of time here, is going to be
#one minute, and we're going to run for one week
SIM_TIME=15

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

class Call(object):
    """The call process (each call has a ``name``) calls the district
        and requests a patrol car.
        """
    def __init__(self, name, call_length, latlon, historic_response_time):
        self.name=name
        self.call_length=call_length
        self.latlon=latlon
        self.call_log=None
        self.historic_response_time=historic_response_time
        self.response_time=None

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

#function degrees to radians
def deg2rad(deg):
    return (deg * math.pi / 180)

####################################################################################################
# gcd_slc calculates the geodesic distance between two points in miles specified by radian
# latitude/longitude using the Spherical Law of Cosines (slc).
# Requires coordinates be in radians so we do a conversion in the middle
#################################################################################################
def gcd_slc(long1, lat1, long2, lat2):
    # convert degrees to radians
    long1 = deg2rad(long1)
    lat1 = deg2rad(lat1)
    long2 = deg2rad(long2)
    lat2 = deg2rad(lat2)
    R = 3959  # Earth mean radius [miles]
    d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) *
        math.cos(long2 - long1)) * R
    return (d)  # Distance in miles

################################################################################
#manhattan.dist calculates the rectangular travel distance between two points
#by using north-south great circle distance and then east-west great circle distance
#
################################################################################
def manhattan_dist(latlon1, latlon2):
  v_dist=gcd_slc(latlon1.lon,latlon1.lat,latlon1.lon,latlon2.lat)
  h_dist=gcd_slc(latlon1.lon,latlon2.lat, latlon2.lon, latlon2.lat)
  return(v_dist+h_dist)

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

    if i == 13:
        call_1 = Call(1, 23, LatLon(33.51305,-112.0856),25)
        print("Call %d called in at %s %s %s " % (call_1.name,
                                                  current_day_hour_minute.day,
                                                  current_day_hour_minute.hour,
                                                  current_day_hour_minute.minute))
        dist1=manhattan_dist(call_1.latlon, car_one.current_latlon)
        dist2=manhattan_dist(call_1.latlon, car_two.current_latlon)
        if dist1 <= dist2:
            print("Car one is closer at distance %.2f miles versus %.2f miles" %(dist1, dist2))
        else:
            print("Car two is closer at distance %.2f miles versus %.2f miles" % (dist2, dist1))


    day_index = DOW.index(schedule[hour].day)
    current_day_hour_minute = DayHourMinute(schedule[hour].day,
                                            schedule[hour].hour, str(i - int(schedule[hour].hour) * 60
                                                                  - (1440 * day_index)))

    print("Day %s Hour %s Minute %s " % (current_day_hour_minute.day,
                                         current_day_hour_minute.hour,
                                         current_day_hour_minute.minute))
