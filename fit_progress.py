# app for novice users in sport 
# In app have you exercises and you can tracking your progress

# Github repository adress - https://github.com/Placius/fit_progress.git
# git remote add origin https://github.com/Placius/fit_progress.git
# git push -u origin main

# import modules
import sys

# app menu

class AppMenu():
    
    def __init__(self):   
        exercises_list = ["exercise1","exercise2","exercise3","exercise4",]   
        self.title = "FIT progress"
        self.exercises = exercises_list
        self.tracking_progress_function = "Track your progress"
        self.exit = "sys.exit(0)"

    def ShowAll(self):
        numerate = 1
        print(self.title, "\n")
        for exercise in self.exercises:
            print(numerate, " ", exercise)
            numerate +=1
        print(numerate, " ", self.tracking_progress_function)
        numerate +=1
        print("\n",numerate, "Exit")
    
    def MakeAchoice(self):
        pass


startApp = AppMenu()

startApp.ShowAll()