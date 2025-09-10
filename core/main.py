from fastapi import FastAPI,HTTPException,status,Query
from typing import Optional

from core.list_user import list_user

app=FastAPI()
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
def Show_User_Details (user_id:Optional[int]=None):
    for name in list_user:
        if name['id'] == user_id:
            return name

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found User")

#chang detail of user
@app.get('/user/Change_User')
def Change_User(user_id:Optional[int]=None,username:Optional[str]=None):
    for name in list_user:
        if name ['id']==user_id :
            name ['name'] = username 
            return name ['id']
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="NOT FOUND USER")

#add user 
@app.post('/user/Add_User')
def  Add_User(User_Id:int,User_name:str,age:int):
    list_user.append({'id':User_Id,'name':User_name,'age':age})
    return list_user


#update user 
@app.put("/user/update_user")
def update_user(id_user:int,name_user:Optional[str]=None,age:Optional[int]=None):
    for item in list_user:
        if item['id']==id_user:
            item['name']=name_user
            item['age']=age
            return{'massage':'update sucsses full'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="USER ID NOT FOUND")

    

#delete user
@app.delete("/user/delete_user")
def delete_user(user_id:int):
    for item in list_user:
        if item['id']==user_id:
            list_user.remove(item)
            return{'massage':"USER DELETED"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="USER NOT FOUND")
