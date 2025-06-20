import streamlit as st
import os
st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')

code_example="""
def greet(name)
    print('hello',name) 
"""
st.code(code_example,language='python')

st.divider()

image_path = os.path.join(os.getcwd(), 'stonic', 'image.jpg')
st.image(image_path)












