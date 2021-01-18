# main file

import login_function, account_create, sys, os, time

class Main:
    def __init__(self):
        self.welcome_message = "Hello!"
    
    def MainWindow(self):
        while True:
            os.system("cls")
            print(self.welcome_message)
            print("\n")
            print("1 - Log in")
            print("2 - Create a new account")
            print("3 - Exit")
            print("\n")

            choice = input("What do you want to do now? - ")

            if choice == '1':
                log = login_function.Login()
                log.Log()

            elif choice == '2':
                new_account = account_create.NewUser()
                new_account.CreateAccount(new_account.Age)
                time.sleep(3)
            
            elif choice == '3':
                sys.exit(0)

            else:
                print("Bad command, please try again.")
                time.sleep(3)


main = Main()

main.MainWindow()