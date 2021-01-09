# fuction for creating new account for user

# import modules

import datetime

class New_user:
    def __init__(self):
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
        self.sex = sex
        self.height = height
        self.weight = weight
        self.login = login
        self.password = password
    
    def PrintInfos(self):
        all_info = [self.name, self.year_of_birth, self.month_of_birth,
        self.day_of_birth, self.age, self.sex, self.height, self.weight,
        self.login, self.password]
        for info in all_info:
            print(info)
        
User1 = New_user()

User1.CreateAccount(User1.Age)

User1.PrintInfos()

input()