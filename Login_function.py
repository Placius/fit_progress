# Login menu / start site

# import modules
import time
import fit_progress
import account_create

# make a Log in function
class Login:
    def __init__(self):
        self.login = "login"
        self.password = "password"
        self.tries = 3
        self.user = ""
        self.user_datas = ""
        self.name = ""

    # check users datas (login and password)
    def Log(self):
        try_this_login = input("Login: ")
        try:
            lista = []
            with open("users/" + try_this_login + "/" + try_this_login+".txt") as file:
                for line in file:
                    lista.append(line.rstrip())
            
            self.login = try_this_login
            # getting the name for the welcome message
            self.user = account_create.User(self.login)
            self.user_datas = self.user.ReturnInfos()
            self.name = self.user_datas[1]

            while True:
                print("Login:", self.login)
                print(lista[-1])
                try_this_password = input("Password: ")

                if str(try_this_password) == str(lista[-1]):
                    print(self.name + "! Welcome in your private FIT-progress app account!")
                    time.sleep(3)
                    app = fit_progress.AppMenu(self.login, self.name)
                    app.MakeAchoice(app.ShowAll, app.CreateAllMovesList)

                elif self.tries <= 0:
                    print("I'm  sorry, your tries limit was finished.")
                    break

                else:
                    print("Bad password, please try again.")
                    print("Tries limit:", self.tries)
                    self.tries -= 1
        
        except FileNotFoundError:
            print("User not exist, try with another login or create a new account.")
            time.sleep(3)
