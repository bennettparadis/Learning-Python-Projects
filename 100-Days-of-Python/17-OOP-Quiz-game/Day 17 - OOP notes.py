class User:
    #Constructor -- initialize function, can include n parameters for attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        #can set default attributes that do not need to be coded when creating an object of that class; not listed in the ()s, do not need to specify
        self.followers = 0
        self.following = 0
    
    #methods that change the default value of an attribute 
    def follow(self, user):
        #user we are following goes up by 1
        user.followers += 1
        #own account adds one more to its following count 
        self.following +=1


user1 = User("007", "bond")
print(user1.id)    
user2 = User("003", "jack")

#user 1 decides to follow user 2 -- counts go up
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)



class Car:
    def __init__(self, seats):
        self.seats = seats
    
    #can create a method that changes the attributes
    def enter_race_mode(self):
        self.seats =2

limo = Car(5)
print(limo.seats)

limo.enter_race_mode()
print(limo.seats)