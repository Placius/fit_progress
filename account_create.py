# fuction for creating new account for user

# import modules

import datetime

class New_user:
    def __init__(self):
        self.user_id = 1
        self.name = "name"
        self.year_of_birth = "year"
        self.month_of_birth = "month"
        self.day_of_birth = "day"
        self.age = "age"
        self.sex = "M/F"
        self.height = "height"
        self.weight = "weight"
        self.login = "login"
        self.password = "password"
    
    def Age(self,yob,mob,dob):
        now = datetime.datetime.now()  
        today_day = int(now.day)
        today_month = int(now.month)
        today_year = int(now.year)

        age = today_year - yob

        if today_month > mob:
            age -= 1
        
        else:
            if today_day > dob:
                age -= 1
        
        self.age = age

    
    def CreateAccount(self, age):
        # get the Id number for new user
        try:
            with open("actual_id_num.txt", "r") as file:
                id = file.read()
                self.user_id = id

        # if file not exist, making a new file with start id
        except IOError:
            with open("actual_id_num.txt", "w") as file:
                self.user_id = 1
                file.write(str(self.user_id))  

        # get information about user
        name = input("Name: ")
        year_of_birth = int(input("Year of birth: "))
        month_of_birth = int(input("Month of birth: "))
        day_of_birth = int(input("Day of birth: "))
        age(year_of_birth, month_of_birth, day_of_birth)
        while True:
            sex = input("Sex(M/F): ")
            if sex.upper() == "M":
                self.sex = "Male"
                break
            elif sex.upper() == "F":
                self.sex = "Female"
                break
            else:
                print("Bad command, try again!")
            
        height = int(input("Height: "))
        weight = int(input("Weight: "))
        login = input("Login: ")
        password = "password"
        check_password = "check_password"
        while password != check_password:
            password = input("Password: ")
            check_password = input("Password(check): ")

            if password != check_password:
                print("The passwords do not match, try again.")
        self.name = name
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.day_of_birth = day_of_birth
        self.height = height
        self.weight = weight
        self.login = login
        self.password = password

        # function for save user datas in file    
        all_info = [self.user_id, self.name, self.year_of_birth, self.month_of_birth,
                    self.day_of_birth, self.age, self.sex, self.height, self.weight,
                    self.login, self.password]    
        
        with open("users/" + str(self.login) + ".txt", "w+") as file:
            for el in all_info:
                file.write(str(el) + "\n")
        
        with open("actual_id_num.txt", "w") as file:
                self.user_id = int(self.user_id) + 1
                file.write(str(self.user_id))


"""class User:
    def __init__(self):
        pass

    def PrintInfos(self):
        all_info = [self.user_id, self.name, self.year_of_birth, self.month_of_birth,
                    self.day_of_birth, self.age, self.sex, self.height, self.weight,
                    self.login, self.password]
        info_names = ["Id:", "Name: ", "Year of birth: ", "Month of birth: ", "Day of birth: ",
                        "Age: ", "Sex: ", "Height: ", "Weight: ", "Login: ", "Password: "]
        for el in range(0,int(len(all_info))):
            print(info_names[el], all_info[el])"""
            
        
User1 = New_user()

User1.CreateAccount(User1.Age)

input()