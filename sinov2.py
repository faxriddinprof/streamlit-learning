# app.py
import streamlit as st
import pandas as pd
import os
from helpers import royxatdan_otish, tizimga_kirish

st.set_page_config("Xarajatlar kuzatuvchi", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None

st.title("💰 Kunlik xarajatlar kuzatuvchisi")

if st.session_state.user:
    st.success(f"Tizimga kirilgan: {st.session_state.user}")
    st.info("Pastdan chapdagi sahifalarga o'ting 👇")
else:
    menu = st.radio("Tanlang", ["Kirish", "Ro'yxatdan o'tish"])

    if menu == "Kirish":
        username = st.text_input("Username")
        password = st.text_input("Parol", type="password")
        if st.button("Kirish"):
            if tizimga_kirish(username, password):
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Username yoki parol noto‘g‘ri.")
    else:
        username = st.text_input("Yangi username")
        password = st.text_input("Yangi parol", type="password")
        if st.button("Ro'yxatdan o'tish"):
            if royxatdan_otish(username, password):
                st.success("Ro'yxatdan o‘tildi. Endi kiring.")
            else:
                st.error("Username band.")

# helpers.py
import pandas as pd
import os

USER_FILE = "users.csv"
EXPENSE_FILE = "expenses.csv"

if not os.path.exists(USER_FILE):
    pd.DataFrame(columns=["username", "password"]).to_csv(USER_FILE, index=False)

if not os.path.exists(EXPENSE_FILE):
    pd.DataFrame(columns=["username", "sana", "toifa", "izoh", "summa"]).to_csv(EXPENSE_FILE, index=False)

def royxatdan_otish(username, password):
    df = pd.read_csv(USER_FILE)
    if username in df['username'].values:
        return False
    df.loc[len(df.index)] = [username, password]
    df.to_csv(USER_FILE, index=False)
    return True

def tizimga_kirish(username, password):
    df = pd.read_csv(USER_FILE)
    user = df[(df["username"] == username) & (df["password"] == password)]
    return not user.empty

def saqlash(username, sana, toifa, izoh, summa):
    df = pd.read_csv(EXPENSE_FILE)
    df.loc[len(df.index)] = [username, sana, toifa, izoh, summa]
    df.to_csv(EXPENSE_FILE, index=False)

def yuklash(username):
    df = pd.read_csv(EXPENSE_FILE)
    return df[df["username"] == username]

# pages/1_📅_Xarajat_Kiritish.py
import streamlit as st
from datetime import date
from helpers import saqlash

st.title("📅 Harajat kiritish")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Iltimos, tizimga kiring.")
    st.stop()

username = st.session_state.user
sana = st.date_input("Sana", value=date.today())
toifa = st.selectbox("Toifa", ["Ovqat", "Transport", "Ko‘ngilochar", "Kiyim", "Boshqa"])
izoh = st.text_input("Izoh")
summa = st.number_input("Summa (so‘m)", min_value=0.0)

if st.button("Saqlash"):
    saqlash(username, sana, toifa, izoh, summa)
    st.success("Harajat saqlandi!")

# pages/2_📊_Tahliliy_Tahlil.py
import streamlit as st
from helpers import yuklash
import pandas as pd

st.title("📊 Tahliliy ma'lumotlar")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Iltimos, tizimga kiring.")
    st.stop()

df = yuklash(st.session_state.user)

if df.empty:
    st.info("Ma'lumotlar mavjud emas.")
else:
    st.dataframe(df)
    st.write(f"**Jami harajat:** {df['summa'].sum():,.2f} so‘m")

    # Toifa bo’yicha
    st.subheader("Toifalarga ko‘ra")
    st.bar_chart(df.groupby("toifa")["summa"].sum())

    # Oylik
    df["sana"] = pd.to_datetime(df["sana"])
    df["oy"] = df["sana"].dt.to_period("M")
    oylik = df.groupby("oy")["summa"].sum()
    st.subheader("Oylik harajatlar")
    st.line_chart(oylik)

    # Yillik
    df["yil"] = df["sana"].dt.year
    yillik = df.groupby("yil")["summa"].sum()
    st.subheader("Yillik harajatlar")
    st.line_chart(yillik)