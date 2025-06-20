import streamlit as st
from datetime import datetime
st.title('This is calculator that calculate your age')


min_date=datetime(1990,1,1)
max_date=datetime.now()


with st.form(key='user_calculate_form',clear_on_submit=True):
    name=st.text_input('Enter your name')

    birthdate=st.date_input('Enter your age',min_value=min_date,max_value=max_date)

    if birthdate:
        age=max_date.year-birthdate.year
        if birthdate.month>max_date.month or (max_date.month==birthdate.month and birthdate.day>max_date.day):
            age-=1
    st.write(f'your calculated age: {age} years')


    submit_button=st.form_submit_button(label='Submit Form')

    if submit_button:
        if not name or not birthdate:
            st.write('Please fill in all form fields')
        else:
            st.balloons()
            st.success(f'Thank you your age is {age}')



