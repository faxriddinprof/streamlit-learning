
# -----------kirish login bolimi----------
import streamlit as st
import os 
from datetime import date
import pandas as pd


st.title('_BU_ _KUNLIK_ :green[_XARAJATLARINGGIZNI_] _SAQLAB_ _BORADIGAN_ :red[_SAYT_]')
#---------------------------------------------------
if 'user_info' not in st.session_state:
    users_info=st.session_state.info={}

if 'step' not in st.session_state:
    st.session_state.step=0
# kirish va yoki login bo'limini choose qilish
select_choose=st.selectbox('Kategoriyani tanlang',['Kirish','Login'])
if select_choose=='Login':
    st.session_state.step=1
if select_choose=='Kirish':
    st.session_state.step=2

def go_to_step2():
    st.session_state.info['name']=name
    st.session_state.info['password']=password
    st.session_state.step=2
#---------------Create login-------------------------------------
if st.session_state.step==1:
    st.header('user name va password kiriting !')
    name= st.text_input('Name',value=st.session_state.info.get('name',''))
    password=st.text_input('Password',value=st.session_state.info.get('password',''))
    
    if st.button('Tasdiqlash',on_click=go_to_step2):
        st.success('tabriklayman malumotlaringiz muvaffaqiyatli saqlandi !')
        st.balloons()


# ----this is a cheking part-------------------------------------

# chek qilish uchun funksiya
def cheking_login(name1,password1):
    for key, valeu in users_info.items():
        if key ==name1:
            print('user name topildi')
            if valeu==password1:
                st.session_state.step=3
            
#------------------------------------------------------------------
if st.session_state.step==2:
    st.header('User name va parolni tasdiqlang !')
    name2= st.text_input('Name')
    password2=st.text_input('Password')
    
    if st.button('Login va parolni tasdiqlash',on_click=cheking_login(name2,password2)):
        st.success('Tabriklayman siz muvaffaqiyatli otdiz !')
    else:
        st.warning('Parol yoki username xato !')











