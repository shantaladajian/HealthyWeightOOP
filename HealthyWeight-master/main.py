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
    def __init__(self, name="", data={"weight":"", "weightGoal": ""}):
        self.name = name
        self.data = data

    def setData(self, data):
        self.data = data

    def toJSON(self):
        tmp = {}
        tmp["data"] = self.data
        return tmp

    def setWeightGoal(self, weightGoal=""):
        if (weightGoal == ""):
            weightGoal = input("Please insert the weight Goal value")
        self.data["weightGoal"] = weightGoal

    def setWeight(self, weight=""):
        if (weight == ""):
            weight = input("Please insert the weight value")
        self.data["weight"] = weight

    def displayName(self):
        print(self.name)

    def display(self):
        print(self.name, self.data["weight"], self.data["weightGoal"])

def main():
    print("\nThis Application helps you reach your weight goal. :)")
    userManager = UserManager()
    userManager.loadAllUsers()
    print("\n***These are all registered users")
    userManager.displayAllUsers()
    currentUser = User()
    while True:
        hasUsed = input("\nHave you used our app before? Please answer in yes or no : ")
        if hasUsed == "no":
            userName = input("\nPlease type your username to create an account: ")
            currentUser = User(userName)
            userManager.addUser(currentUser)
            break
        elif hasUsed == "yes":
            userName = input("\nplease type your previously created username : ")
            currentUser = userManager.getUserByName(userName)
            if currentUser is None:
                currentUser = User(userName)
                userManager.addUser(currentUser)
            break
        else:
            print("\nsorry Try again!Please type yes or no.(not capital)")

    print("\n******This is the current user:")
    currentUser.display()
    change = input("\nDo you want to change the data? please type yes or no")
    if(change == "yes"):
        currentUser.setWeight(input("Please insert the weight"))


    print("\nThe new updated list of Users is:")
    userManager.displayAllUsers()
    userManager.saveAllUsers()
main()