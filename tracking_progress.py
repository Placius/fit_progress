# tracking progress fuction

# import modules
import account_create

class TrackYourProgress:
    def __init__(self, login):
        self.login = login
        self.user = account_create.User(self.login)
        self.user_datas = self.user.ReturnInfos()

    def ShowProgress(self):
        lista = []
        with open("users/" + str(self.login) + "/" + "start_body_datas.txt", "r+") as f:
            lines = f.read().split("\n")
            for line in lines:
                lista.append(line)
        
        weight_progress = int(lista[1]) - int(self.user_datas[8])

        if weight_progress > 0:
            print("Congratulations, your weight has dropped by", str(weight_progress) + "kg!")
        elif weight_progress < 0:
            print("Your weight has increased by", str(weight_progress * (-1)) + "kg!")
        else:
            print("Your weight is the same as at the beginning.")

        print("\n\nYour starting weight was", lista[1])
        print("Your current weight is", self.user_datas[8], "\n\n")

        input(" --> Enter")

    def Actual_body_info(self):
        print("Fit Progress\n\n")
        print("Height:", self.user_datas[7])
        print("Weight:", self.user_datas[8], "\n\n")

        input(" --> Enter")
    
    def Change_my_datas(self):
        self.user.ChangeInfos()