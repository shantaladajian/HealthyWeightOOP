import json
import os

class UserManager:
    def __init__(self):
        self.users = []

    def loadAllUsers(self):
        availableFiles = os.listdir()
        if "users.json" in availableFiles:
            with open("users.json") as file:
                users = json.load(file)
                for key in users:
                    user = User(key)
                    user.setData(users[key]["data"])
                    self.users.append(user)

    def saveAllUsers(self):
        file = open('users.json', 'w')
        usersJSON = {}
        for user in self.users:
            usersJSON[user.name] = user.toJSON()

        file.write(json.dumps(usersJSON))
        file.close()

    def addUser(self, user):
        self.users.append(user)

    def getUserByName(self, name):
        for user in self.users:
            if (user.name == name):
                return user
        return None;

    def displayAllUsers(self):
        for user in self.users:
            user.displayName()

class User:
    def __init__(self, name="", weight = "", weightGoal =""):
        self.name = name
        self.weight = weight
        self.weightGoal = weightGoal

    def setData(self, data):
        self.weight = data["weight"]
        self.weightGoal = data["weightGoal"]

    def toJSON(self):
        tmp = {}
        tmp["data"] = {}
        tmp["data"]["weight"] = self.weight
        tmp["data"]["weightGoal"] = self.weightGoal
        return tmp

    def setWeightGoal(self, weightGoal=""):
        if (weightGoal == ""):
            weightGoal = input("Please insert the weight Goal as lose/gain or maintain")
        self.weightGoal = weightGoal

    def setWeight(self, weight=""):
        if (weight == ""):
            weight = float(input("Please insert your weight value in kg "))
        self.weight = weight

    def findBMI(self,height=""):
        if (height == ""):
            height = int(input("\nPlease insert the height in integer form and cm : "))
        BMI = float(float(self.weight) * 10000 / (height * height))
        if BMI < 18.5:
            print("\nDear user, your BMI indicated that you're underweight.The normla range is between 18.5-24.9.")
            print("We suggest you choose the gaining goal if you haven't chosen that. ")
        elif BMI > 18.5 and BMI < 25:
            print(
                "\nDear user, your BMI indicated that you're in the normal weight range!The normla range is between 18.5-24.9 ")
            print("We suggest you choose the maintaining goal if you haven't chosen that.")
        elif BMI > 25 and BMI < 30:
            print(
            "\nDear user, your BMI indicated that you're in the overweight range.The normla range is between 18.5-24.9")
            print("We suggest you choose the losing goal if you haven't chosen that.")

    def findCalories(self,height="",gender="",age="",lose=""):
        if height == "":
            height = int(input("\nPlease insert the height in integer form and cm : "))
        if gender == "":
            gender = input("\nPlease insert your gender as male or female non-capital : ")
        if age== "":
            age= int(input("\nPlease insert your age in an integer form : "))
        if lose == "":
            lose = float(input("\nPlease insert how many kgs you want to lose per week : "))
        if gender == "male":
            CalorieIn = float(10 * float(self.weight)+ 6.25 *  height - 5 * age + 5 - (lose * 3500) / 7)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                    " Kgs from your current weight per week:)\nWe suggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if gender == "female":
            CalorieIn = float(10 * float(self.weight) + 6.25 *  height - 5 * age - 161 - (lose * 3500) / 7)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                    " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")

    def displayName(self):
        print(self.name)

    def display(self):
        print(self.name, self.weight, self.weightGoal)

    def checkprogress(self,oldweight,currentweight):
        difference=int(currentweight)-int(oldweight)
        if difference > 0 and (self.weightGoal == "maintain" or self.weightGoal == "lose"):
            print("\nDear user, you have gained : ", difference,
                  "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to", self.weightGoal,
                  " weight.\nWork harder you'll reach there")
        if difference > 0 and self.weightGoal == "gain":
            print("\nDear user, you have gained : ", difference,
                  "Kgs since we last saw you !\nYou're on the right track as your goal was to ", self.weightGoal,
                  "your weight :) Keep on going :)")
        if difference < 0 and (self.weightGoal == "maintain" or self.weightGoal == "gain"):
            print("\nDear user, you have lost: ", abs(difference),
                  "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to gain weight.\nWork harder you'll reach there")
        if difference < 0 and self.weightGoal == "lose":
            print("\nDear user, you have lost : ", abs(difference),
                  "Kgs since we last saw you !\nYou're on the right track as your goal was to lose"
                  "weight :) Keep on going :)")

def main():
    print("\nThis Application helps you reach your weight goal. :)")
    userManager = UserManager()
    userManager.loadAllUsers()
    print("\n***These are all registered users")
    userManager.displayAllUsers()
    while True:
        hasUsed = input("\nHave you used our app before? Please answer in yes or no : ")
        if hasUsed == "no":
            userName = input("\nPlease type your username to create an account: ")
            currentUser = User(userName)
            userManager.addUser(currentUser)
            currentUser.setWeightGoal()
            currentUser.setWeight()
            currentUser.findBMI()
            currentUser.findCalories()
            break
        elif hasUsed == "yes":
            userName = input("\nplease type your previously created username : ")
            currentUser = userManager.getUserByName(userName)
            if currentUser is None:
                currentUser = User(userName)
                userManager.addUser(currentUser)
                currentUser.findBMI()
                currentUser.findCalories()
            break
        else:
            print("\nsorry Try again!Please type yes or no.(not capital)")

    print("\n******This is the current user:")
    currentUser.display()
    change = input("\nDo you want to change the data? please type yes or no")
    if(change == "yes"):
        oldweight=currentUser.data["weight"]
        currentUser.setWeight(input("Please insert the weight"))
        currentweight =currentUser.data["weight"]
        currentUser.checkprogress(oldweight,currentweight)

    print("\nThe new updated list of Users is:")
    userManager.displayAllUsers()
    userManager.saveAllUsers()
main()