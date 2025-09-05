from fastapi import FastAPI

app=FastAPI()
#list of user
list_user = [
    {'id':0,'name':'koorosh','age':27},
    {'id':1,'name':'kirash','age':17},
    {'id':2,'name':'bahram','age':52},
    {'id':3,'name':'shayan','age':26},
    {'id':4,'name':'farhan','age':27},
]
#example of route
@app.get("/")
def root():
    return{"massage":"hello"}

#show all user
@app.get("/user")
def show_user():
    return list_user

#show details of user
@app.get("/user/{user_id}")
def Show_User_Details (user_id:int=None):
    for name in list_user:
        if name['id'] == user_id:
            return name

    return{'massage': 'Name Not Found '} 

#chang detail of user
@app.get('/user/Change_User')
def Change_User(user_id:int=None,username:str=None):
    for name in list_user:
        if name ['id']==user_id :
            name ['name'] = username 
            return name ['id']
    return{'massage': 'Name Not Found '}

#add user 
@app.post('/user/Add_User')
def  Add_User(User_Id:int,User_name:str,age:int):
    list_user.append({'id':User_Id,'name':User_name,'age':age})
    return list_user
    


