from datetime import datetime
from django.utils import timezone
import json
import pytz
from rest_framework.response import Response

class ClassSession(object):

    def __init__(self,day_of_week=None,session_start=None,session_end=None):
        if(session_start < session_end):
            self.day_of_week = day_of_week
            self.session = [0,0,0,0,0,0,0,0,0,0,0,0]
            for i in range(session_start-1,session_end):
                self.session[i] = 1
        else:
            return Response("Time start cannot greater than time end!!!")
            

    
    def get_all_attr(self):
        return self.day_of_week, self.session
    
    def get_day(self):
        return self.day_of_week
    
    def get_session(self):
        return self.session
    
    def compare(self,other):
        if(self.get_day() == other.get_day()):
            result = sum([self.get_session()[i]*other.get_session()[i] for i in range(12)])           
            if(result == 0):
                return True
            else:
                return False
        else:
            return True
    

class ClassSchedule(object):
    
    def __init__(self,start_time=None,end_time=None,schedule=[]):
        if(start_time < end_time):
            z = False
            for i in range(len(schedule)):
                for j in range(i + 1,len(schedule)):
                    if(schedule[i].compare(schedule[j]) == True):
                        z = True
                        # print("ERROR, two sessions are coincided")

            if z == False :
                self.start_time = start_time
                self.end_time = end_time
                self.schedule = schedule
            else:
                self.start_time = None
                self.end_time = None
                self.schedule = []
        else:
            # print("Time start cannot greater than time end!!!")
            self.start_time = None
            self.end_time = None
            self.schedule = []

    
    def get_all(self):
        return self.start_time,self.end_time, self.schedule

    def add_session(self,session):
        z = True
        for i in self.schedule:
            if(session.compare(i)):
                # print("ERROR, two sessions are coincided")
                z = False
        if z : self.schedule.append(session)
        
        
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time

    def get_schedule(self):
        return self.schedule

    def compare(self,other):
        if(self.get_start_time() == None or self.get_end_time == None or len(self.schedule) == 0):
            # print("Schedule is empty!!")
            return
        else:
            if((self.get_start_time() == other.get_start_time() and self.get_end_time() == other.get_end_time()) or \
                (self.get_start_time() < other.get_start_time() and self.get_end_time() > other.get_end_time()) or \
                (self.get_start_time() > other.get_start_time() and self.get_end_time() < other.get_end_time()) or \
                (self.get_start_time() < other.get_start_time() and self.get_end_time() < other.get_end_time() and self.get_end_time() > other.get_start_time()) or \
                (self.get_start_time() > other.get_start_time() and self.get_end_time() > other.get_end_time() and self.get_start_time() < other.get_end_time())): 
                z = False
                for i in self.get_schedule():
                    for j in other.get_schedule():
                        if(i.compare(j) == True):
                            # print("a")
                            z = True
                            break
                return z
            else:
                return False

            

if __name__=="__main__":
    test   = ClassSession(4,1,3)
    test_2 = ClassSession(5,1,3)
    test_3 = ClassSession(5,2,4)
    test_4 = ClassSession(4,5,7)
    test_5 = ClassSession(3,1,3)

    schedule_1 = ClassSchedule(datetime(2005,7,14),datetime(2006,1,14),[test,test_2])
    schedule_2 = ClassSchedule(datetime(2005,11,14),datetime(2007,8,14),[test_2,test_4])

    schedule_3 = ClassSchedule(datetime(2005,7,14),datetime(2006,1,14),[test_3,test_2])
    schedule_4 = ClassSchedule(datetime(2004,11,14),datetime(2005,8,14),[test_4,test_5])

    
    print(schedule_1.compare(schedule_2))


# return False when schedule is not coincided else return True
# check not coincided
# check time_start time_end 
# check session_start session_end
# check in a schedule
# check 2 schedule