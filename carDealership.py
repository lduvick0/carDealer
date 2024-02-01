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
class Vehicle():
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
    def make_motorcycle(self):
        print("Vroom vroom!")

# Create two lists: bikes, and trucks. Create at least 3 instances of both subclasses
# and store in the appropriate list.
v1=Truck("Ford",1500, 43000)
v2=Truck("Dodge", 12000,38000)
v3=Truck("Chevy",38000,30000)
v4=Motorcycle("Suzuki",12520,20000,200)
v5=Motorcycle("Harley",5370,15000,120)
v6=Motorcycle("Yamaha",22980,1200,60)

vehicles_to_compare=[v1,v2,v3,v4,v5,v6]
# Create an empty list named vehicles_to_compare and fill with the user’s selection(s).
