# tracking progress fuction

# import modules
import account_create

class TrackYourProgress:
    def __init__(self, login):
        self.login = login

    def ShowProgress(self):
        pass

    def Actual_body_info(self):
        print("Coming soon access...")
    
    def Change_my_datas(self):
        user = account_create.User(self.login)
        user.ChangeInfos()