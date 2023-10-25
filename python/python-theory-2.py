### OOP
# Attributes (has) car.speed:
speed = 0
fuel = 32


# Methods (does) car.move():
def move():
    speed = 60


def stop():
    speed = 0


# PascalCase
# camelCase
# snake_case
def function():
    pass


class User:

    def __init__(self, user_id, username):  # initialise attributes
        print("new user being created")  # Mỗi khi tạo ra một object từ class, def __init__ sẽ được gọi ra
        self.id = user_id
        self.username = username
        self.followers = 0  # Set default giá trị của follower
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Ann"
user_1 = User("001", "Ann")
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Vo"
user_2 = User("002", "Vo")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

"""
class Car:
    def __init___(self,seats): #Initialise
        self.seats = seats
    def enter_race_mode(): #Method
        self.seats = 2
        
my_car = Car(5)   ==   my_car.seats = 5
my_car.enter_race_mode()

"""
