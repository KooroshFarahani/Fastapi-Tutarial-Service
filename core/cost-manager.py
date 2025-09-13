from fastapi import FastAPI,HTTPException,Query,status,Body
from typing import Optional
import random
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):  # اضافه کردن async
    print("Starting application...")  # قبل از yield
    yield  # اینجا برنامه اجرا می‌شود
    print("Closing application...")   # بعد از yield

app = FastAPI(lifespan=lifespan)  

app=FastAPI(lifespan=lifespan)
cost_list=[
    {'id':0,'description':'description','amount':0},
    {'id':1,'description':'description1','amount':1},
    {'id':2,'description':'description2','amount':2}
]
#create new cost
@app.post('/create',status_code=status.HTTP_201_CREATED)
def create_new_cost(
                    description:Optional[str]=Body(default=None,min_length=0,max_length=200,description="Description for new cost",title="Description"),
                    amount:float=Body(ge=0,le=1000000,description="Cost amount",title="amount")
                    ):
                    cost_list.append({'id':random.randint(3,100),'description':description,'amount':amount})
                    return{
                            'Message':'Create New Cost Successful',
                            'Cost_Description':description,
                            'Cost_Amount':amount
                        }

#show all cost
@app.get('/show_all',status_code=status.HTTP_202_ACCEPTED)
def show_all():
        return cost_list

#show spectial cost
@app.get('/show_detail',status_code=status.HTTP_202_ACCEPTED)
def show_detail(id:int=Query(ge=0,le=100,description="Show Details of cost",title="ID Number")):
        for item in cost_list:
                if item['id']==id:
                        return{
                                'Message':'Your Cost Find',
                                'Cost ID':item['id'],
                                'Cost_Description':item['description'],
                                'Cost_Amount':item['amount']
                        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Your ID Is NotFound")  

#change detaile cost
@app.put('/change_detail',status_code=status.HTTP_202_ACCEPTED)
def change_detail(id:int=Query(ge=0,le=100,description="most use uniq id",title="ID Number"),
                  description:Optional[str]=Body(default=None,min_length=0,max_length=200,description="Description for change",title="Description"),
                  amount:int=Body(ge=0,le=1000000,description="Cost amount",title="amount")):
        for item in cost_list:
                if item['id']==id:
                        item['description']=description
                        item['amount']=amount
                        return{
                                'Message':'Your Cost Changed',
                                'Cost ID':id,
                                'Cost_Description':description,
                                'Cost_Amount':amount
                        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Your ID Number Is Not Valid")

#DELET cost
@app.delete('/delete_cost',status_code=status.HTTP_508_LOOP_DETECTED)
def delete_cost(id:int=Query(ge=0,le=100,description="delete cost",title="ID Number")):
        for item in cost_list:
                if item['id']==id:
                        cost_list.remove(item)
                        return{
                                'Message':'Your Cost Deleted',
                                'Cost ID':item['id']
                        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Your ID Is NotFound")