# application exercises functions

# import modules
import time, os, winsound

# general class for exercises classes
class Exercise:
    def __init__(self, name, description, lvl, repeat, series, weekly_plan, pause):
        self.name = name
        self.description = "descroiption"
        self.lvl = lvl
        self.series = series
        self.repeat = repeat
        self.pause_time_after_one_serie = pause

    # matching the task to the exercise
    def How_much_series_and_repeats(self):

        if self.lvl == "Beginner":
            pass
        
        elif self.lvl == "Low":
            pass

        elif self.lvl == "Medium":
            pass

        elif self.lvl == "High":
            pass
        
        else:
            pass

# warm-up
class WarmUp:
    def __init__(self):
        self.all_infos = []
        self.exercises = []

        # calling functions
        self.AddInfosToLists()
        
    def BeforeStart(self):
        t = 5
        for i in range(0,6):
            os.system("cls")
            print("Warm up starting in " + str(t) + "...")
            time.sleep(1)
            t -= 1
            winsound.Beep(400, 1000)
    
    def AddInfosToLists(self):
        with open("exercises/warm-up.txt") as file:
            lines = file.read().split("\n")
            line_num = 1
            for line in lines:
                self.all_infos.append(line)
                if line_num > 2:
                    self.exercises.append(line)
                line_num += 1
    
    def StartWarmUp(self):
        for exercise in self.exercises:
            length = int(self.all_infos[1])
            sec = length
            while sec != 0:
                os.system("cls")
                print(self.all_infos[0].upper())
                print("\n\nExercise:", exercise)
                print("Time for this exercise - " + str(sec))
                time.sleep(1)
                sec -= 1
            
            winsound.Beep(800, 1000)
            print("Next exercise....")
            time.sleep(3)
    
# push-ups
class Exercise1(Exercise):
    def __init__(self):    
        pass

# pull-up
class Exercise2(Exercise):
    def __init__(self):
        pass

# crunches
class Exercise3(Exercise):
    def __init__(self):
        pass

# squats
class Exercise4(Exercise):
    def __init__(self):
        pass

# extra "shooting 15" exercise
class Exercise5(Exercise):
    def __init__(self):
        pass

WarmUp()