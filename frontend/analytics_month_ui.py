import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = 'http://127.0.0.1:8000'

def analytics_by_month_tab():

    response=requests.get(f'{API_URL}/analytics_by_month')

    if response.status_code!=200:
        st.error('Failed to fetch expense analytics by month data')
    else:
        response = response.json()

        df = pd.DataFrame({
            'Month Num' : [datetime.strptime(i,'%B').month for i in response],
            'Month Name' : list(response.keys()),
            'Total' : [response[i] for i in response],
        })
        df.set_index('Month Num',inplace=True)
        df.sort_values(by='Total',ascending=False,inplace=True)
        st.subheader('Expense Breakdown by Month')
        st.bar_chart(df.set_index('Month Name')['Total'])
        df['Total'] = df['Total'].map('{:.2f}'.format)
        st.table(df)