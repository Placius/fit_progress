# tracking progress fuction

# import modules
import account_create, os

class TrackYourProgress:
    def __init__(self, login):
        self.login = login
        self.user = account_create.User(self.login)
        self.user_datas = self.user.ReturnInfos()

        # records
        self.max_pushups = 0
        self.max_pullups = 0
        self.max_crunches = 0
        self.max_squats = 0
        # records lists
        self.last_records_list = 0
        self.new_records_list = 0
    
    def CheckProgress(self, last_check, new_check):
        progress = int(new_check) - int(last_check)
        if progress > 0:
            return ("You have made progress in Push ups +" + str(progress))

        elif progress < 0: 
            return ("Fall in exercise Push ups " + str(progress))

        else:
            return ("-")

    def ShowProgress(self):
        # WEIGHT PROGRESS
        lista = []
        with open("users/" + str(self.login) + "/" + "start_body_datas.txt", "r+") as f:
            lines = f.read().split("\n")
            for line in lines:
                lista.append(line)
        
        weight_progress = int(lista[1]) - int(self.user_datas[8])

        # showing weight progress
        if weight_progress > 0:
            print("Congratulations, your weight has dropped by", str(weight_progress) + "kg!")
        elif weight_progress < 0:
            print("Your weight has increased by", str(weight_progress * (-1)) + "kg!")
        else:
            print("Your weight is the same as at the beginning.")

        print("\n\nYour starting weight was", lista[1])
        print("Your current weight is", self.user_datas[8], "\n\n")

        # PROGRESS IN EXERCISES
        try:
            last_records_list = []
            new_records_list = []
            with open("users/" + str(self.login) + "/" + "lasts_records.txt", "r+") as f:
                lines = f.read().split("\n")
                for line in lines:
                    last_records_list.append(line)

            with open("users/" + str(self.login) + "/" + "new_records.txt", "r+") as f:
                lines = f.read().split("\n")
                for line in lines:
                    new_records_list.append(line)
            self.last_records_list = last_records_list
            self.new_records_list = new_records_list

            self.max_pushups = int(self.new_records_list[0])
            self.max_pullups = int(self.new_records_list[1])
            self.max_crunches = int(self.new_records_list[2])
            self.max_squats = int(self.new_records_list[3])
        
        except IOError:
            pass

        # presentation records list and showing progress
        if self.max_pushups > 0 or self.max_pullups > 0 or self.max_crunches > 0 or self.max_squats > 0:
            print("\t\tLasts records:\t\tActually records:\n\n")
            print("Push ups -\t\t\t", self.last_records_list[0], "\t\t\t", self.new_records_list[0])
            print("Pull ups -\t\t\t", self.last_records_list[1], "\t\t\t", self.new_records_list[1])
            print("Crunches -\t\t\t", self.last_records_list[2], "\t\t\t", self.new_records_list[2])
            print("Squats -\t\t\t", self.last_records_list[3], "\t\t\t", self.new_records_list[3], "\n\n")

            print(self.CheckProgress(self.last_records_list[0], self.new_records_list[0]))
            print(self.CheckProgress(self.last_records_list[1], self.new_records_list[1]))
            print(self.CheckProgress(self.last_records_list[2], self.new_records_list[2]))
            print(self.CheckProgress(self.last_records_list[3], self.new_records_list[3]))

        else:
            print("Actually, your record list is empty, make challenges and input your first records!\n\n")

    def Actual_body_info(self):
        print("Fit Progress\n\n")
        print("Height:", self.user_datas[7])
        print("Weight:", self.user_datas[8], "\n\n")

        input(" --> Enter")
    
    def Change_my_datas(self):
        self.user.ChangeInfos()
    
    def NewRecordsList(self):
        os.system("cls")
        print("Your new records:\n\n")

        max_pushups = int(input("Push ups - "))
        max_pullups = int(input("Pull ups - "))
        max_crunches = int(input("Crunches - "))
        max_squats = int(input("Squats - "))

        self.max_pushups = max_pushups
        self.max_pullups = max_pullups
        self.max_crunches = max_crunches
        self.max_squats = max_squats

        try:
            # if file exist make a file with new records
            with open("users/" + str(self.login) + "/" + "lasts_records.txt", "r+") as f:
                pass

            # save last records
            lista = []
            with open("users/" + str(self.login) + "/" + "new_records.txt", "r+") as f:
                lines = f.read().split("\n")
                for line in lines:
                    lista.append(line)
            
            with open("users/" + str(self.login) + "/" + "lasts_records.txt", "w+") as f:
                for data in lista:
                    f.write(data + "\n")

            # save new/actual records
            with open("users/" + str(self.login) + "/" + "new_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))

        except IOError:
            with open("users/" + str(self.login) + "/" + "lasts_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))
            with open("users/" + str(self.login) + "/" + "new_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))