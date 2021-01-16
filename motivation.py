# function for choosing random motivation text

import random

class Motivation:
    def __init__(self):
        self.citations = [
        "“It's not whether you get knocked down; it's whether you get up. ” - Vince Lombardi", 
        "“I don’t count my situps. I only start counting once it starts hurting. ” - Muhammad Ali",
        "“I’ve failed over and over again in my life. And that is why I succeed.” – Michael Jordan",
        "“The only way to prove you are a good sport is to lose.” – Ernie Banks",
        "“If you fail to prepare, you’re prepared to fail.” – Mark Spitz",
        "“The road to Easy Street goes through the sewer.” – John Madden",
        "“It is not the size of a man but the size of his heart that matters.” – Evander Holyfield",
        "“You miss 100 percent of the shots you don’t take.” – Wayne Gretzky",
        "“Never give up! Failure and rejection are only the first step to succeeding.” – Jim Valvano",
        "“A trophy carries dust. Memories last forever.” – Mary Lou Retton",
        "“Without self-discipline, success is impossible, period.” – Lou Holtz",
        "“Good is not good when better is expected.” – Vin Scully",
        "“Never say never because limits, like fears, are often just an illusion.” – Michael Jordan",
        "“Hard work beats talent when talent doesn’t work hard.” – Tim Notke",
        "“It’s not whether you get knocked down; it’s whether you get up.” – Vince Lombardi",
        "“Wisdom is always an overmatch for strength.” – Phil Jackson"]
        self.citat_for_today = "Try..."
        self.Choose_citat()

    def Choose_citat(self):
        citat = random.choice(self.citations)
        self.citat_for_today = citat
    
    def Return_citat(self):
        return self.citat_for_today