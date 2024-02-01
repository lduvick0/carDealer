# Prompt the user to choose from different categories of vehicle to compare for purchase.
# Display an error if the user enters invalid data and asks the user again for a selection.
# When the user enters valid data, print each vehicle within that collection of their choosing.
# Ask the user if they would like to add a vehicle to compare.
# If yes, the user will make a selection and that vehicle will be placed in a collection containing for them to later “compare”.
# If not, give the user the option to look at more vehicles in other categories or go ahead and “compare vehicles”.
# The user will receive a detailed list of all chosen vehicles, listing their make, miles, and price. Each vehicle should also “make noise” as the program iterates through the list.


# Create a base class named Vehicle to store the data about each vehicle.
# This class should contain these specifications:
# Initialization (self, make, miles, price)
# Sets the make, miles and price properties
# Also sets a engine_on property to False
# Methods
# start_engine()
# Prints a message: “Starting engine…”
# Sets engine_on to True
# make_noise()
# Prints a message: “Beep beep!”
class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        engine_on=False
    def start_engine(self):
        print("Starting engine")
        engine_on=True
    def make_noise(self):
        print("Beep beep!")
# Create a derived class from Vehicle named Truck to store the data about each vehicle.
# This class should contain these specifications:
# Initialization (self, make, miles, price)
# Sets the make, miles and price properties
# Also sets a cargo property to False
# Additional Methods
# load_cargo()
# Prints a message: “Loading the truck bed…”
# Sets cargo to True

class Truck(Vehicle):
    def __init__(self, make, miles,price):
        Vehicle.__init__(self, make, miles, price)
        cargo=False
    def load_cargo(self):
        print("Loading the truck bed...")
        cargo=True
# Create a derived class from Vehicle named Motorcycle to store the data about each vehicle.
# This class should contain these specifications:
# Initialization (self, make, miles, price, top_speed)
# Sets the make, miles and price properties
# Sets additional method of top_speed
# Override Methods
# make_noise()
# Prints a message: “Vroom vroom!”

class Motorcycle(Vehicle):
    def __init__(self, make , miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed
    def make_noise(self):
        print("Vroom vroom!")
v1=Truck("Ford",1500, 43000)
v2=Truck("Dodge", 12000,38000)
v3=Truck("Chevy",38000,30000)
truckList=[(f"1: {v1.make}: with {v1.miles} miles costs ${v1.price}"),
            (f"2: {v2.make}: with {v2.miles} miles costs ${v2.price}"),
            (f"3: {v3.make}: with {v3.miles} miles costs ${v3.price}")]
v4=Motorcycle("Suzuki",12520,20000,200)
v5=Motorcycle("Harley",5370,15000,120)
v6=Motorcycle("Yamaha",22980,1200,60)
cycleList=[ (f"1: {v4.make}: with {v4.miles} miles and a top speed of {v4.top_speed}costs ${v4.price}"),
            (f"2: {v5.make}: with {v5.miles} miles and a top speed of {v5.top_speed}costs ${v5.price}"),
            (f"3: {v6.make}: with {v6.miles} miles and a top speed of {v6.top_speed}costs ${v6.price}")]
vehicles_to_compare=[]
# Create two lists: bikes, and trucks. Create at least 3 instances of both subclasses
# and store in the appropriate list.
print("Hello")
print("Welcome to KAL Bikes and Trucks!")
validInput="n"
while validInput=="n":
    choiceInput=input("Would you like to view bikes or trucks? (b or t)")
    if choiceInput=="t":
        for i in range(0,3):
            print(truckList[i])
        validInput="y"
        compInput = input("Would you like to compare one of these vehicles today? (y or n)")
        if compInput=="y":
            numInput=int(input("Which vehicle would you like to compare? (please list number)"))
            vehicles_to_compare.append(truckList[numInput-1])
    elif choiceInput=="b":
        for i in range(0,3):
            print(cycleList[i])
        validInput="y"
        compInput=input("Would you like to compare one of these vehicles today? (y or n)")
        if compInput == "y":
            numInput = int(input("Which vehicle would you like to compare? (please list number)"))
            vehicles_to_compare.append(cycleList[numInput - 1])
    else:
        print("Invalid Input Please Try again")
    validInput=input("Would you like to compare your vehicles now? (y or n)")
    if validInput=="y":
        print("Here are your vehicles to compare:")
        for vehicle in vehicles_to_compare:
            print(vehicle)
            vehicle.make_noise()
        print("Thank you and have a nice day!")


# Create an empty list named vehicles_to_compare and fill with the user’s selection(s).
