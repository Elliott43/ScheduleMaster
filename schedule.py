import datetime
from funclib import *
import thing
class Schedule:
    def __init__(self, things, starting_time):
        self.things = things
        self.starting_time = starting_time


    def do(self):
        pass

    def add(self, thing, index=0):
        if index in range(len(self.things)):
            self.things.insert(thing, index)
        else:
            raise IndexError

    def remove(self, index=0):
        if index in range(len(self.things)):
            return self.things.pop(index)
        else:
            raise IndexError

    def save(self):
        pass

    def load(self):
        pass

    def __str__(self):
        x = ""
        y = datetime.datetime.now()
        y = [y.strftime("%H"), y.strftime("%M"), y.strftime("%S")
        for i in self.things:
            pass

    def __dict__(self):
        x = {"starting_time": self.starting_time}
        x["things"] = [i.__dict__() for i in self.things]
        return x


def make_schedule():
    # might be kinda poggers
    # x = datetime.datetime.now()
    options = []
    things = []
    while True:
        x = query("What classes do you have?")
        if x:
            options.append(x)
        else:
            break

    date = query("What time does this schedule start at (format: 'ss/mm/HH/DD/MM/YYYY')")
    while True:
        x = thing.make_thinge(options)
        if x.name == "":
            break
        else:
            things.append(x)

    return Schedule(things, date)

