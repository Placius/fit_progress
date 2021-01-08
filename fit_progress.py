# app for novice users in sport 
# In app have you exercises and you can tracking your progress

# Github repository adress - https://github.com/Placius/fit_progress.git
# git remote add origin https://github.com/Placius/fit_progress.git
# git branch -M main     
# git push -u origin main

# import modules
import sys, os

# app menu

class AppMenu():
    
    def __init__(self):   
        exercises_list = ["exercise1","exercise2","exercise3","exercise4","exercise5"]   
        self.title = "FIT progress"
        self.tracking_progress_function = "Track your progress"
        self.exercises = exercises_list
        self.user_choice = None
        self.all_moves = {}
    
    def CreateAllMovesList(self):
        keys = 1
        self.all_moves[keys] = [self.tracking_progress_function]
        keys += 1
        for exercise in self.exercises:
            self.all_moves[keys] = [exercise]
            keys += 1
        self.all_moves[keys] = ["exit"]

        print(self.all_moves)
        

    def ShowAll(self):
        numerate = 1
        print(self.title, "\n")
        print(numerate, " - ", self.tracking_progress_function)
        numerate +=1
        for exercise in self.exercises:
            print(numerate, " - ", exercise)
            numerate +=1
        print("\n",numerate, "Exit")


    def MakeAchoice(self, show_menu):
        while True:
            # auto clean window after new entry
            os.system("cls")

            # print menu option
            show_menu()

            # choices 
            user_choice = input("What do you want now to do? - ")
            self.user_choice = user_choice
            if self.user_choice == '1':
                pass
            
            elif self.user_choice == '2':
                pass

            elif self.user_choice == '3':
                pass

            elif self.user_choice == '4':
                pass

            elif self.user_choice == '5':
                pass
            
            # auto numbered for exit function 

            elif self.user_choice == str(len(self.all_moves)):
                print("Bye Bye...")
                sys.exit(0)
            
            else:
                print("Somthing goes wrong, please try again!")


startApp = AppMenu()

startApp.CreateAllMovesList()

startApp.MakeAchoice(startApp.ShowAll)