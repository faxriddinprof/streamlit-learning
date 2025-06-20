import streamlit as st
import os
from datetime import datetime

min_date=datetime(1990,1,1)
max_date=datetime.now()

st.title(f'this is my new project. User information Form')

form_values={
    'name':None,
    'age':None,
    'height':None,
    'gender':None,
    'birthday':None
}

with st.form(key='user_information_form'):
    form_values['name']=st.text_input('Enter your full name')
    form_values['age']=st.number_input('Enter your age')
    form_values['height']=st.number_input('Enter your height (sm)')
    form_values['gender']=st.selectbox('Gender',['Male','Female'])
    form_values['birthday']=st.date_input('Enter your birthday',min_value=min_date,max_value=max_date)
    

    submit_button=st.form_submit_button(label='Submit')
    if submit_button:
        if not all(form_values.values()):
            st.warning('Please fill in all of the fields')

        else:
            st.balloons()
            st.write('### info')

            for key, valeu in form_values.items():
                st.write(f'{key}: {valeu}')










                