import json
import os
import random

class Newuser:
    def __init__(self,username,gender,healthCondition,weightGoal,initialWeight,height,age):
        self.username=username
        self.gender=gender
        self.healthCondition=healthCondition
        self.initialWeightGoal=weightGoal
        self.initialWeight =initialWeight
        self.height = height
        self.age = age
        self.info={self.username: {"initialData": {'initialWeightGoal':self.initialWeightGoal, 'initialWeight': self.initialWeight }}}

    def SaveData(self):
        a = os.listdir()
        if "users.json" in a:
            with open('users.json') as file1:
                initialold = json.load(file1)
                initialold.update(self.info)
            file = open('users.json', 'w')
            file.write(json.dumps(initialold))
            file.close()
        else:
            file = open("users.json", "w")
            file.write(json.dumps(self.info))
            file.close()

    def CalculatingBMI(self):
        BMI = float(self.initialWeight * 10000 / (self.height * self.height))
        BMI = "{:.2f}".format(BMI)
        print("\nYour BMI is:", BMI )
        if float(BMI) < 18.5:
            print("\nDear user, your BMI indicated that you're underweight.The normla range is between 18.5-24.9.")
            print("We suggest you choose the gaining goal if you haven't chosen that. ")
        elif float(BMI) > 18.5 and float(BMI) < 25:
            print(
                "\nDear user, your BMI indicated that you're in the normal weight range!The normla range is between 18.5-24.9 ")
            print("We suggest you choose the maintaining goal if you haven't chosen that.")
        elif float(BMI) > 25 and float(BMI) < 30:
            print(
            "\nDear user, your BMI indicated that you're in the overweight range.The normla range is between 18.5-24.9")
            print("We suggest you choose the losing goal if you haven't chosen that.")

    def WeightMaintainBMR(self):
        if self.gender=="male":
            CalorieIn = float(10 * self.initialWeight + 6.25 * self.height - 5 * self.age + 5)
            print("\nYou should eat:", CalorieIn, "CaloriesPer day, to maintain your current weight :) \n")
        elif self.gender == "female":
            CalorieIn = float(10 * self.initialWeight + 6.25 * self.height - 5 * self.age - 161)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to maintain your current weight :) \n")

    @staticmethod
    def TipOfTheDay():
        with open('datas.json', 'r') as file:
            tips = json.load(file)
        j = random.choices(tips["TipsOfTheDay"]["aidDigestion"])
        w = random.choices(tips["TipsOfTheDay"]["essentialOils"])
        print("\nToday's Tip of the day is :", ', '.join(j))
        print("\nand a fact about essential oils is:", ', '.join(w))
        print("Dear user, thank you for using HealthyWeight :) Hope to see you soon!")

    @staticmethod
    def Load_Old_Data(name):
        with open("users.json") as a:
            load = json.load(a)
            Old_Weight = load[name]["initialData"]["initialWeight"]
            print('Your initial weight was : ', Old_Weight)
            while True:
                change = input("Do you want to change it? Please answer in yes or no : ")
                if change == "yes":
                    while True:
                        New_Weight = input("Insert your current weight in kg in numeric integer form : ")
                        if New_Weight.isnumeric():
                            New_Weight = int(New_Weight)
                            Newuser.CheckIfGoalisReached(New_Weight, name, Old_Weight)
                            Newuser.Save_New_Data(New_Weight, name)
                            Newuser.TipOfTheDay()
                            break
                        else:
                            print("\nPlease write in kg in a numeric integer form:(")
                    break
                elif change == "no":
                    print("Okey you can change it whenever you want :) \n")
                    Newuser.TipOfTheDay()
                    break
                else:
                    print("\nPlease try it again and answer in the form of yes or no :)")

    @staticmethod
    def CheckIfGoalisReached(New_Weight, name, Old_Weight):
        difference = New_Weight - Old_Weight
        with open("users.json") as a:
            load = json.load(a)
            Goal = load[name]["initialData"]["initialWeightGoal"]
            if difference > 0 and (Goal == "maintain" or Goal == "lose"):
                print("\nDear user, you have gained : ", difference,
                      "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to", Goal,
                      " weight.\nWork harder you'll reach there")
            if difference > 0 and Goal == "gain":
                print("\nDear user, you have gained : ", difference,
                      "Kgs since we last saw you !\nYou're on the right track as your goal was to ", Goal,
                      "your weight :) Keep on going :)")
            if difference < 0 and (Goal == "maintain" or Goal == "gain"):
                print("\nDear user, you have lost: ", abs(difference),
                      "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to gain weight.\nWork harder you'll reach there")
            if difference < 0 and Goal == "lose":
                print("\nDear user, you have lost : ", abs(difference),
                      "Kgs since we last saw you !\nYou're on the right track as your goal was to lose"
                      "weight :) Keep on going :)")

    @staticmethod
    def Save_New_Data(New_Weight, name):
        with open("users.json") as a:
            load = json.load(a)
            load[name]["initialData"]["initialWeight"] = New_Weight
            file = open('users.json', 'w')
            file.write(json.dumps(load))
            file.close()
    @staticmethod
    def Gender():
        while True:
            gender = input("please input 1 for female and 2 for male:")
            if gender == "1":
                gender = "female"
                return gender
            if gender == "2":
                gender = "male"
                return gender
            else:
                print("\nERROR ! please input 1 or 2 only :) ")
    @staticmethod
    def HealthCondition():
        while True:
            condition = input("\nPlease input your health condition as: bad, good, or very good")
            if condition == "good" or condition == "bad" or condition == "very good":
                return condition
            else:
                print("Please input your condition as written above :) ")
    @staticmethod
    def WeightGoal():
        while True:
            goal = input("\n Input your weight goal as written: lose, gain or maintain?")
            if goal == "maintain" or goal == "lose" or goal == "gain":
                return goal
            else:
                print("Please input your condition as written above :) ")
    @staticmethod
    def Weight():
        kg = float(input("\nplease input your weight in kgs"))
        if isinstance(kg, float):
            return kg
        else:
            print("please input in numeric form")
    @staticmethod
    def Height():
        while True:
            x = input("\nPlease input your height in cm and integer form : ")
            if x.isnumeric():
                return int(x)
            else:
                print("please input in numeric and integer form")
    @staticmethod
    def Age():
        while True:
            x = input("\nPlease input your age in years and integer form : ")
            if x.isnumeric():
                return int(x)
            else:
                print("please input in numeric and integer form")
    @staticmethod
    def NewUSer():
        print("Dear new user, Welcome to HealthyWeight :)")
        print(
            "\n you're going to fill the following: gender, healthCondition, initialWeightGoal, initialWeight, height, Age")
        username = input("\nplease create your username by typing it here : ")
        gender = Newuser.Gender()
        healthCondition = Newuser.HealthCondition()
        weightGoal = Newuser.WeightGoal()
        initialWeight = Newuser.Weight()
        height = Newuser.Height()
        age = Newuser.Age()
        newuser = Newuser(username, gender, healthCondition, weightGoal, initialWeight, height, age)
        newuser.CalculatingBMI()
        newuser.SaveData()
        if weightGoal == "maintain":
            newuser.WeightMaintainBMR()
        if weightGoal == "lose":
            lose = float(input("How many kgs yu want to lose per week? input here : "))
            WeightLossBMR(username,gender,healthCondition,weightGoal,initialWeight,height,age, lose)
        if weightGoal == "gain":
            gain = float(input("How many kgs yu want to gain per week? input here : "))
            WeightGainBMR(username,gender,healthCondition,weightGoal,initialWeight,height,age, gain)
        Newuser.TipOfTheDay()

    @staticmethod
    def UsernameisNone():
        while True:
            end = input(
            "\nSory this username doesn't exist. Type 0 to end the Application\nType 1 to create a new username.")
            if end.isnumeric():
                end = int(end)
                if end == 0:
                    print("\nDear user, thank you for using HealthyWeight :) Hope to see you soon!")
                    break
                elif end == 1:
                    Newuser.NewUser()
                    break
            else:
                print("please input an INTEGER.")

    @staticmethod
    def Create_New_Username():
        print("\nFile doesn't exist! so you do not have an account :(. ")
        create = input("\nDo you want to create a new account? Please answer in yes or no .")
        while True:
            if create == "yes":
                Newuser.NewUser()
                break
            elif create == "no":
                print("\nokey See you next time :)")
                break
            else:
                print("\nplease answer in yes or no form.")
class WeightGainBMR(Newuser):
    def __init__(self,username,gender,healthCondition,weightGoal,initialWeight,height,age,gain):
        super().__init__(username,gender,healthCondition,weightGoal,initialWeight,height,age)
        self.gain=gain
        if self.gender == "male":
            CalorieIn = float(10 * self.initialWeight + 6.25 * self.height - 5 * self.age + 5 + (self.gain * 3500) / 7)
            print("\nYou should eat:", CalorieIn, "Calorie Per day, to gain", self.gain,
                  " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if self.gender == "female":
            CalorieIn = float(10 * self.initialWeight + 6.25 * self.height - 5 * self.age- 161 + (self.gain * 3500) / 7)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to gain", self.gain,
                  " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories. ")

class WeightLossBMR(Newuser):
    def __init__(self, username,gender,healthCondition,weightGoal,initialWeight,height,age, lose):
        super().__init__(username,gender,healthCondition,weightGoal,initialWeight,height,age)
        self.lose = lose
        if self.gender == "male":
            CalorieIn = float(10 * self.initialWeight + 6.25 *  self.height - 5 * self.age + 5 - (self.lose * 3500) / 7)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", self.lose,
                    " Kgs from your current weight per week:)\nWe suggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if self.gender == "female":
            CalorieIn = float(10 * self.initialWeight + 6.25 *  self.height - 5 * self.age - 161 - (self.lose * 3500) / 7)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", self.lose,
                    " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")

def MAIN():
    print("\nThis Application helps you reach your weight goal. :)")
    while True:
        MAIN = input("Have you used our app before? Please answer in yes or no : ")
        if MAIN == "no":
            Newuser.NewUSer()
            break
        elif MAIN == "yes":
            a = os.listdir()
            if "users.json" in a:
                with open("users.json") as file:
                    user = json.load(file)
                    while True:
                        name = input("\nplease type your previously created username : ")
                        if user.get(name) is None:
                            Newuser.UsernameisNone()
                        else:
                            Newuser.Load_Old_Data(name)
                            break
            else:
                Newuser.Create_New_Username()
            break
        else:
            print("\nsorry Try again!Please type yes or no.(not capital)")
MAIN()