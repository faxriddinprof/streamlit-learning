import streamlit as st
import pandas as pd
import os
from datetime import date

FAYL = 'expenses.csv'

# Fayl mavjud bo'lmasa yaratib qo'yamiz
if not os.path.exists(FAYL):
    df = pd.DataFrame(columns=["Sana", "Kategoriya", "Izoh", "Summa"])
    df.to_csv(FAYL, index=False)

# Ma'lumot kiritish formasi
st.title("💸 Kunlik Xarajatlar Hisobi")

st.subheader("Yangi xarajat qo'shish")
sana = st.date_input("Sana", value=date.today())
kategoriya = st.selectbox("Kategoriya", ["Ovqat", "Transport", "Ko‘ngilochar", "Kiyim", "Boshqa"])
izoh = st.text_input("Izoh")
summa = st.number_input("Summa (so'mda)", min_value=0.0, format="%.2f")

if st.button("Saqlash"):
    yangi = pd.DataFrame([[sana, kategoriya, izoh, summa]], columns=["Sana", "Kategoriya", "Izoh", "Summa"])
    df = pd.read_csv(FAYL)
    df = pd.concat([df, yangi], ignore_index=True)
    df.to_csv(FAYL, index=False)
    st.success("✅ Ma'lumot saqlandi!")

# Ma'lumotlarni ko‘rsatish
st.subheader("📊 Xarajatlar ro'yxati")
df = pd.read_csv(FAYL)
st.dataframe(df)

# Umumiy tahlil
st.subheader("📈 Umumiy xarajatlar bo'yicha tahlil")
st.write(f"Jami xarajat: {df['Summa'].sum():,.2f} so'm")
st.line_chart(df.groupby("Kategoriya")["Summa"].sum())
