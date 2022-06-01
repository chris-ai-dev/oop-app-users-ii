# your improved User class goes here
from datetime import datetime
from Post import Post

class User:
    #class variable to store the post of every user
    #class variable to store user postes
    each_user_post = [] 
    
    #constructor to initialize instance variables
    def __init__(self, name, email, address, driver_licence): #
        self.name = name
        self.email = email
        self.address = address
        self.driver_licence = driver_licence

    def __str__(self):
        # return f"I am {self.name}. My email is {self.email}. I live on {self.address} and my driver licence is {self.driver_licence}"
        return each_user_post   
    
    #method for user to create new post that belongs to class itself(static method)
    def user_create_post(self):
       individual_post = input(f'What would you like to post? ')
       current_time = datetime.now()
       #calling instructo of post storing the parameters
       post = Post(self.name, individual_post, current_time)
       #remeber to use User class not self
       User.each_user_post.append(post)
        
    #this is for testing
    @staticmethod
    def test():
        for each in User.each_user_post:
            print(each)    
 
    
    
joe = User("Joe", "shmjoe@gmail.com", "123 fake st", "E910843") 
bo = User("Bo", "Bo@gmail.com", "3 hat st", "E910843") 
fill = User("Fill", "fill@gmail.com", "40 que st", "E910843") 

# print(joe)
# print(bo)
# print(fill)

joe.user_create_post()
bo.user_create_post()

User.test()



