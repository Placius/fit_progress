# import modules
import sys, os, time

# import modules from from your own libraries
import motivation
import tracking_progress
import exercises
import account_create

# app menu

class AppMenu():
    
    def __init__(self, login, name):   
        options_list = ["Track your progress","Exercises", "Motivation for today"]   
        self.options = options_list
        self.user_choice = None
        self.all_moves = {}
        self.login = login
        self.name = name
        self.title = "FIT progress\t\t\t\t" + str(self.name)

        self.lvl = "lvl"

        # current level of exercises
        user = account_create.User(self.login)
        user.GetInfos()
        infos = user.ReturnInfos()
        # index of level information
        self.lvl =  infos[9] 
    
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
                track_menu = """
                1 - Change your weight and height

                2 - Show your progress

                3 - Up-to-date information about you

                4 - Back to menu

                5 - Exit
                """

                while True:
                    os.system("cls")
                    print(track_menu)
                    choice = input("Your choice: ")
                    track = tracking_progress.TrackYourProgress(self.login)
                    if choice == '1':
                        os.system("cls")
                        track.Change_my_datas()
                    
                    elif choice == '2':        
                        os.system("cls")          
                        track.ShowProgress()
                        print("\n\nIf you want to change your records --> entry '1' and press Enter")
                        print("If you want to back to menu --> press Enter\n\n")
                        choice = input("Your choice: ")
                        if choice == '1':
                            track.NewRecordsList()
                        else:
                            break

                    elif choice == '3':
                        os.system("cls")
                        track.Actual_body_info()
                    
                    elif choice == '4':
                        break

                    elif choice == '5':
                        sys.exit(0)
                    
                    else:
                        os.system("cls")
                        print("Bad command, please try again.")
                        time.sleep(3)

            elif self.user_choice == '2':
                exercises_menu = ("Actual level -  " + self.lvl.upper() + 
                """\n\n
        1 - Push-up

        2 - Pull-up

        3 - Crunches

        4 - Squats

        5 - Shooting fifteen

        6 - CHANGE LEVEL OF EXERCISES

        7 - Back to menu

            8 - Exit
                \n
                """)

                while True:
                    os.system("cls")
                    print(exercises_menu)
                    choice = input("Your choice - ")

                    if choice == '1':
                        print("Exercise: Push Up\n")
                        print("Level:", self.lvl, "\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1

                            exercise = exercises.Exercise1(self.lvl)
                            exercise.DoExercise()
                        
                        else:
                            exercise = exercises.Exercise1(self.lvl)
                            exercise.DoExercise()

                    elif choice == '2':
                        print("Exercise: Pull Up\n")
                        print("Level:", self.lvl, "\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1

                            exercise = exercises.Exercise2(self.lvl)
                            exercise.DoExercise()
                        
                        else:
                            exercise = exercises.Exercise2(self.lvl)
                            exercise.DoExercise()

                    elif choice == '3':
                        print("Exercise: Crunches\n")
                        print("Level:", self.lvl, "\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1

                            exercise = exercises.Exercise3(self.lvl)
                            exercise.DoExercise()
                        
                        else:
                            exercise = exercises.Exercise3(self.lvl)
                            exercise.DoExercise()

                    elif choice == '4':
                        print("Exercise: Squats\n")
                        print("Level:", self.lvl, "\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1

                            exercise = exercises.Exercise4(self.lvl)
                            exercise.DoExercise()
                        
                        else:
                            exercise = exercises.Exercise4(self.lvl)
                            exercise.DoExercise()

                    elif choice == '5':
                        print("Exercise: Shooting Fifteen\n")
                        print("Level:", self.lvl, "\n\n")
                        input("If you ready --> press Enter")
                        if if_warmup_was_done == 1:
                            warmUp = exercises.WarmUp()
                            warmUp.BeforeStart()
                            warmUp.StartWarmUp()
                            if_warmup_was_done += 1

                            exercise = exercises.Exercise5(self.lvl)
                            exercise.DoExercise()
                        
                        else:
                            exercise = exercises.Exercise5(self.lvl)
                            exercise.DoExercise()

                    elif choice == '6':
                        os.system("cls")
                        lista = account_create.User(self.login)
                        lista.ChangeLevel()
                        lvl = lista.ReturnInfos()
                        self.lvl = lvl[9]
                        print("\n\nYour lvl was changed!")
                        time.sleep(2)

                    elif choice == '7':
                        break

                    elif choice == '8':
                        sys.exit(0)

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
