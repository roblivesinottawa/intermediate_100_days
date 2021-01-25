class User:
    
    def __init__(self, name, age, user_id, username):
        self.name = name
        self.age = age
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

    def __repr__(self):
        return f"""{self.name} is {self.age}. The user ID is: {self.user_id}. Username is {self.username}. 
        Their following count is {self.following} and their number of followers is {self.followers}."""

    __str__ = __repr__

userone = User("Rob", 34, 12435, "rob234")
usertwo = User("Vick", 34, 45830, "vickye")
userone.follow(usertwo)
usertwo.follow(userone)
print(userone)
print(usertwo)