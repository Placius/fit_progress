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
        self.first_records_list = 0
        self.new_records_list = 0

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
            first_records_list = []
            new_records_list = []
            with open("users/" + str(self.login) + "/" + "firsts_records.txt", "r+") as f:
                lines = f.read().split("\n")
                for line in lines:
                    first_records_list.append(line)

            with open("users/" + str(self.login) + "/" + "new_records.txt", "r+") as f:
                lines = f.read().split("\n")
                for line in lines:
                    new_records_list.append(line)
            self.first_records_list = first_records_list
            self.new_records_list = new_records_list

            self.max_pushups = int(self.new_records_list[0])
            self.max_pullups = int(self.new_records_list[1])
            self.max_crunches = int(self.new_records_list[2])
            self.max_squats = int(self.new_records_list[3])
        
        except IOError or FileNotFoundError:
            pass

        # presentation records list and showing progress
        if self.max_pushups > 0 or self.max_pullups > 0 or self.max_crunches > 0 or self.max_squats > 0:
            print("\t\tFirsts records:\t\tActually records:\n\n")
            print("Push ups -\t\t\t", self.first_records_list[0], "\t\t\t", self.new_records_list[0])
            print("Pull ups -\t\t\t", self.first_records_list[1], "\t\t\t", self.new_records_list[1])
            print("Crunches -\t\t\t", self.first_records_list[2], "\t\t\t", self.new_records_list[2])
            print("Squats -\t\t\t", self.first_records_list[3], "\t\t\t", self.new_records_list[3], "\n\n")

            if int(self.first_records_list[0]) - int(self.new_records_list[0]) != 0:
                progress = int(self.new_records_list[0]) - int(self.first_records_list[0])
                if progress > 0:
                    print("You have made progress in Push ups +" + str(progress))

                elif progress < 0: 
                    print("Fall in exercise Push ups", str(progress))

                else:
                    pass

            if int(self.first_records_list[1]) - int(self.new_records_list[1]) != 0:
                progress = int(self.new_records_list[1]) - int(self.first_records_list[1])
                if progress > 0:
                    print("You have made progress in Pull ups +" + str(progress))

                elif progress < 0:
                    print("Fall in exercise Pull ups", str(progress))

                else:
                    pass

                
            if int(self.first_records_list[2]) - int(self.new_records_list[2]) != 0:
                progress = int(self.new_records_list[2]) - int(self.first_records_list[2])
                if progress > 0:
                    print("You have made progress in Crunches +" + str(progress))

                elif progress < 0:
                    print("Fall in exercise Crunches", str(progress))

                else:
                    pass


            if int(self.first_records_list[3]) - int(self.new_records_list[3]) != 0:
                progress = int(self.new_records_list[3]) - int(self.first_records_list[3])
                if progress > 0:
                    print("You have made progress in Squats +" + str(progress))

                elif progress < 0:
                    print("Fall in exercise Squats", str(progress))

                else:
                    pass

        
        else:
            print("Actually, your record list is empty, make challenges and input your first records!")

        input(" --> Enter")

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
            with open("users/" + str(self.login) + "/" + "firsts_records.txt", "r+") as f:
                pass

            with open("users/" + str(self.login) + "/" + "new_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))

        except IOError or FileNotFoundError:
            with open("users/" + str(self.login) + "/" + "firsts_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))
            with open("users/" + str(self.login) + "/" + "new_records.txt", "w+") as f:
                f.write(str(self.max_pushups) + "\n")
                f.write(str(self.max_pullups) + "\n")
                f.write(str(self.max_crunches) + "\n")
                f.write(str(self.max_squats))

progres = TrackYourProgress("Placius")
progres.ShowProgress()