#! python3

class Time:
    """Blueprint for a Time object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def print_time(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)

    def Tick(self):
        if(self.__second < 59):
            self.__second == __second + 1
        elif(self.__second == 59):
            if(self.__minute < 59):
                self.__minute == __minute + 1
            elif(self.__minute == 59):
                self.__hour == __hour + 1
        else:
            print("Something is hinky with your time countingy stuffz")

    def set_second(self, second):
        self.__second = second

    def set_minute(self, minute):
        self.__minute = minute

    def set_hour(self, hour):
        self.__hour
                

#First Time object
myTime1 = Time()
myTime1.print_time()
myTime1.set_time(1, 2, 3)
myTime1.Tick()
myTime1.print_time()

#Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)

print("My two time objects are now storing:")
myTime1.print_time()
myTime2.print_time()
