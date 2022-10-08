from randomuser import RandomUser
import pandas as pd
import os

r = RandomUser()

def get_users(num):
    users =[]
     
    for user in RandomUser.generate_users(num):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

df1 = pd.DataFrame(get_users(100))  

df1.to_json('.\List of people.json')
