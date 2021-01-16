# app for novice users in sport 
# On this app have you exercises and you can tracking your progress

# Github repository adress - https://github.com/Placius/fit_progress.git
# git remote add origin https://github.com/Placius/fit_progress.git
# git branch -M main     
# git push -u origin main

# import modules
import sys, os

# import modules from from your own libraries
import motivation
import tracking_progress
import exercises

# app menu

class AppMenu():
    
    def __init__(self):   
        options_list = ["Track your progress","Exercises", "Motivation for today"]   
        self.title = "FIT progress"
        self.options = options_list
        self.user_choice = None
        self.all_moves = {}
    
    def CreateAllMovesList(self):
        keys = 1
        for option in self.options:
            self.all_moves[keys] = [option]
            keys += 1
        self.all_moves[keys] = ["exit"]
        

    def ShowAll(self):
        numerate = 1
        print(self.title, "\n")
        for option in self.options:
            print(numerate, " - ", option)
            numerate +=1
        print("\n",numerate, "Exit")


    def MakeAchoice(self, show_menu, create_moves_list):
        create_moves_list()
        # checking if the warm-up has already been done
        if_warmup_was_done = 1
        
        while True:
            # auto clean window after new entry
            os.system("cls")

            # print menu option
            show_menu()

            # choices 
            print("\n")
            user_choice = input("What do you want now to do? - ")
            self.user_choice = user_choice

            # auto numbered for exit function 

            if self.user_choice == str(len(self.all_moves)):
                print("Bye Bye...")
                sys.exit(0)

            elif self.user_choice == '1':
                track = tracking_progress.TrackYourProgress()
                track.Print_info()

            elif self.user_choice == '2':
                print("""
                1 - All body training

                2 - Push-up

                3 - Pull-up

                4 - Crunches

                5 - Squats

                6 - Shooting fifteen
                \n
                """)

                while True:
                    choice = input("Your choice - ")

                    if choice == '1':
                        print("Exercise: All body training\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass

                    elif choice == '2':
                        print("Exercise: Push Up\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass

                    elif choice == '3':
                        print("Exercise: Pull Up\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass

                    elif choice == '4':
                        print("Exercise: Crunches\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass

                    elif choice == '5':
                        print("Exercise: Squats\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass

                    elif choice == '6':
                        print("Exercise: Shooting Fifteen\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1
                        
                        else:
                            pass
                    
                    elif choice == '7':
                        break

                    else:
                        print("Bad commant, please try again.")

            elif self.user_choice == '3':
                os.system("cls")
                citat = motivation.Motivation()
                print_citat = citat.Return_citat()
                print(print_citat)
                print("\n\n")
                input("press -> Enter")

            # more option in the future
            elif self.user_choice == '4':
                pass

            elif self.user_choice == '5':
                pass
            
            else:
                print("Somthing goes wrong, please try again!")
