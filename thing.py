import json
import time
from funclib import *
ASSIGNMENTS = ["Workbook", "Checkpoint", "Discussion Board", "Session", "Project", "Exam"]


# This is just here to make things neater. This is the timer.
def timed(txt="> "):
    x = time.time()
    input(txt)
    return -x + time.time()

class Thing():
    def __init__(self, name, subject, species):
        self.name = name
        self.subject = subject
        self.species = species
        self.time = self.get_time()

    # This times the assignment, and saves the time taken.
    def do(self):
        return self.save_time(timed(f"{self.subject}, {self.species}: {self.name}\nPRESS 'ENTER' WHEN FINISHED"))

    # Takes an average of all times with the particular subject, species combination.
    # Otherwise returns 15 and adds that to the json file.
    # It adds 15 to offset the inconsistency that is present at the start
    def get_time(self):
        info = json.load(open("data.json", "r"))

        if f"{self.subject}, {self.species}" in info["assignments"]:
            return sum(info["assignments"][f"{self.subject}, {self.species}"])

        else:
            info["assignments"][f"{self.subject}, {self.species}"] = [15]
            return 15

    # Over writes the json file with the new data added in the appropriate location.
    def save_time(self, saved):
        with open("data.json", "r") as f:
            info = json.load(f)
            info["assignments"][f"{self.subject}, {self.species}"].append(saved)

        json.dump(info, open("json.data", 'w'), indent=4)
        return self.get_time() - saved

    def __str__(self):
        return f"{self.subject}, {self.species}: {self.name}"

    def __dict__(self):
        pass



# I plan to make it so that different things can go through different schedules.
# Each schedule will have a start point and a stop point.
# This will solve the dinner / fixed item problem I was having

def make_thing(options):
    name = query("What is the name of this thing?")
    subject = query("What class is this thing for?", options)
    species = query("What type of assignment is it?", ASSIGNMENTS)
    return Thing(name, subject, species)