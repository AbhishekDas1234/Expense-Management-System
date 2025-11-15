import streamlit as st
from datetime import date
import requests
import pandas as pd

API_URL = 'http://127.0.0.1:8000'

def analytics_by_category_tab():

    col1,col2=st.columns(2)

    with col1:
        start_date = st.date_input(label='Start Date 📆',value=date(2025,8,1))
    with col2:
        end_date = st.date_input(label='End Date 📆', value=date(2025, 8, 5))

    if st.button('Get Analytics'):
        data={'start_date':start_date.strftime('%Y-%m-%d'),'end_date':end_date.strftime('%Y-%m-%d')}
        response=requests.post(f'{API_URL}/analytics',json=data)

        if response.status_code!=200:
            st.error('Failed to fetch expense analytics by category data')
        else:
            response = response.json()
            df = pd.DataFrame({
                'Category' : list(response.keys()),
                'Total' : [response[i]['total'] for i in response],
                'Percentage' : [response[i]['percentage'] for i in response]
            })
            df.sort_values(by='Percentage',ascending=False,inplace=True)
            df['num']=[1,2,3,4,5]
            st.subheader('Expense Breakdown by Category')
            st.bar_chart(df.set_index('Category')['Percentage'])
            df['Total'] = df['Total'].map('{:.2f}'.format)
            df['Percentage'] = df['Percentage'].map('{:.2f}'.format)
            df.set_index('num',inplace=True)
            st.table(df)