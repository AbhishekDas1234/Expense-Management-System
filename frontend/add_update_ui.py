import streamlit as st
from datetime import date
import requests

API_URL = 'http://127.0.0.1:8000'

def add_update_tab():
    expense_date = st.date_input(label="Enter Date 📆",value=date(2025,8,1))
    response = requests.get(f'{API_URL}/expenses/{expense_date}')

    if response.status_code == 200:
        existing_expenses = response.json()

    else:
        st.error('Fail to retrieve expenses')
        existing_expenses = []

    categories = ['Select','Rent', 'Food', 'Shopping', 'Entertainment', 'Other']
    column_spec=[0.1,1.5,1.5,2.5]

    with st.form(key='expense_form'):
        col1, col2, col3, col4 = st.columns(spec=column_spec)

        with col1:
            pass

        with col2:
            st.markdown("<h6 style='text-align: center; color: white;'>Amount</h6>", unsafe_allow_html=True)

        with col3:
           st.markdown("<h6 style='text-align: center; color: white;'>Category</h6>", unsafe_allow_html=True)

        with col4:
            st.markdown("<h6 style='text-align: center; color: white;'>Notes</h6>", unsafe_allow_html=True)

        expenses = []
        set_submit = 1
        miss_cat_list=[]

        for i in range(7):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = 'Select'
                notes = ''

            col1, col2, col3, col4 = st.columns(spec=column_spec)

            with col1:
                st.write(f'{i+1}.')

            with col2:
                amount_input = st.number_input(label='Amount', min_value=0.0, step=1.0, value=amount, key=f'amount_{i}',
                                               label_visibility='collapsed')
            with col3:
                category_input = st.selectbox(label='Category', options=categories, index=categories.index(category),
                                              key=f'category_{i}', label_visibility='collapsed')
            with col4:
                notes_input = st.text_input(label='Notes', value=notes, key=f'text_{i}', label_visibility='collapsed')

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

            if amount_input > 0 and category_input == 'Select':
                set_submit = 0
                miss_cat_list.append(i+1)

        submit_button = st.form_submit_button()
        if submit_button and set_submit == 1:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            response = requests.post(f'{API_URL}/expenses/{expense_date}', json=filtered_expenses)
            if response.status_code == 200:
                st.success(response.json()['Message'])
            else:
                st.error('Failed to update expenses')
        elif submit_button and set_submit == 0:
            st.error(f'* Enter Category for row no. {miss_cat_list[0]}')