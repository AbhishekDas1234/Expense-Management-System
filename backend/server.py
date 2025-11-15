from fastapi import FastAPI,HTTPException
import db_helper
from datetime import date
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class Analytics(BaseModel):
    start_date:date
    end_date:date

app=FastAPI()

@app.get('/expenses/{expense_date}',response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500,detail='Failed to retrieve expense from the database')
    return expenses

@app.post('/expenses/{expense_date}')
def add_or_update_expenses(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
    return {'Message': 'Expenses Updated Successfully!!'}

@app.post('/analytics')
def get_analytics(date_range:Analytics):
    response=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if response is None:
        raise HTTPException(status_code=500,detail='Failed to retrieve expense summary from the database')
    total=sum([row['total'] for row in response])
    dic={}
    for row in response:
        percentage=(row['total']/total)*100 if total!= 0 else 0
        dic[row['category']] = {'total': row['total'], 'percentage': percentage}
    return dic

@app.get('/analytics_by_month')
def fetch_expense_by_month():
    expenses = db_helper.fetch_expense_by_month()
    if expenses is None:
        raise HTTPException(status_code=500, detail='Failed to retrieve expense from the database')
    dic={}
    for row in expenses:
        dic[row['month']] = row['total']
    return dic