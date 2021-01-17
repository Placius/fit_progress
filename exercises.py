# application exercises functions

# import modules
import time, os, winsound

# general class for exercises classes
class Exercise:
    def __init__(self, description, name, pause, lvl):
        self.name = name
        self.description = description
        self.lvl = lvl
        self.series = "series"
        self.repeat = "repeat"
        self.pause = pause
        self.week = "week"

        self.How_much_series_and_repeats()

    # matching the task to the exercise
    def How_much_series_and_repeats(self):
        while True:
            week = int(input("Training week -"))
            if week < 1 or week > 10:
                print("Bad command, please try again.")
            
            else:
                self.week = week
                break

        if self.lvl == "Beginner":
            lista =[]
            with open("training_plans/begginer/week"+str(self.week)+".txt") as file:
                lines = file.read().split("\n")
                for line in lines:
                    lista.append(line)
            
            self.series = int(lista[0])
            self.repeat = int(lista[1])
        
        elif self.lvl == "Low":
            if self.week > 8:
                self.week = 8

            lista =[]
            with open("training_plans/low/week"+str(self.week)+".txt") as file:
                lines = file.read().split("\n")
                for line in lines:
                    lista.append(line)
            
            self.series = int(lista[0])
            self.repeat = int(lista[1])

        elif self.lvl == "Medium":
            if self.week > 6:
                self.week = 6
                
            lista =[]
            with open("training_plans/medium/week"+str(self.week)+".txt") as file:
                lines = file.read().split("\n")
                for line in lines:
                    lista.append(line)
            
            self.series = int(lista[0])
            self.repeat = int(lista[1])

        elif self.lvl == "High":
            if self.week > 4:
                self.week = 4
                
            lista =[]
            with open("training_plans/high/week"+str(self.week)+".txt") as file:
                lines = file.read().split("\n")
                for line in lines:
                    lista.append(line)
            
            self.series = int(lista[0])
            self.repeat = int(lista[1])
        
        else:
            pass
    # function to start training
    def DoExercise(self):
        t = 5
        for i in range(0,6):
            os.system("cls")
            print(self.description)
            print("Training starting in " + str(t) + "...")
            time.sleep(1)
            t -= 1

        winsound.Beep(800, 1000)

        for serie in range (1,self.series):
            os.system("cls")
            print("Serie", serie)
            print("\n\nMake", self.repeat,"repeats of", self.name,"\n\n")

            input("When you finish, press --> Enter")

            # pause
            sec = int(self.pause)
            winsound.Beep(800, 1000)
            while sec != 0:
                os.system("cls")
                print("The break will end in:", sec)
                time.sleep(1)
                sec -= 1
            winsound.Beep(800, 1000)
            print("Start next serie, good luck!")
            time.sleep(2)

    def PrintInfos(self):
        print(self.name, self.description, self.lvl, self.series, self.repeat, self.pause)

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
    def __init__(self, lvl):   
        lista =[]
        with open("exercises/push-up.txt") as file:
            lines = file.read().split("\n")
        
            for line in lines:
                lista.append(line)

        super().__init__(lista[0], lista[1], lista[2], lvl)
    
# pull-up
class Exercise2(Exercise):
    def __init__(self, lvl):   
        lista =[]
        with open("exercises/pull-up.txt") as file:
            lines = file.read().split("\n")
        
            for line in lines:
                lista.append(line)

        super().__init__(lista[0], lista[1], lista[2], lvl)

# crunches
class Exercise3(Exercise):
    def __init__(self, lvl):   
        lista =[]
        with open("exercises/crunches.txt") as file:
            lines = file.read().split("\n")
        
            for line in lines:
                lista.append(line)

        super().__init__(lista[0], lista[1], lista[2], lvl)

# squats
class Exercise4(Exercise):
    def __init__(self, lvl):   
        lista =[]
        with open("exercises/squats.txt") as file:
            lines = file.read().split("\n")
        
            for line in lines:
                lista.append(line)

        super().__init__(lista[0], lista[1], lista[2], lvl)

# extra "shooting 15" exercise
class Exercise5(Exercise):
    def __init__(self, lvl):   
        lista =[]
        with open("exercises/shooting.txt") as file:
            lines = file.read().split("\n")
        
            for line in lines:
                lista.append(line)

        super().__init__(lista[0], lista[1], lista[2], lvl)

ex = Exercise2("Beginner")

ex.DoExercise()