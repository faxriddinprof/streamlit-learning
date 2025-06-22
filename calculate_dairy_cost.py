
# -----------kirish login bolimi----------
import streamlit as st
import os 
from datetime import date
import pandas as pd
st.title('_BU_ _KUNLIK_ :green[_XARAJATLARINGGIZNI_] _SAQLAB_ _BORADIGAN_ :red[_SAYT_]')
#---------------------------------------------------

FAYL_NOMI = "users.csv"
EXPENSE_FILE = "expenses.csv"

# Agar users.csv yo'q bo'lsa — yaratamiz
if not os.path.exists(FAYL_NOMI):
    df = pd.DataFrame(columns=["username", "password"])
    df.to_csv(FAYL_NOMI, index=False)

if not os.path.exists(EXPENSE_FILE):
    pd.DataFrame(columns=["username", "sana", "toifa", "izoh", "summa"]).to_csv(EXPENSE_FILE, index=False)
#-----------------------------------------------------------------------------------------------------------------------

def royxatdan_otish(username, password):
    df = pd.read_csv(FAYL_NOMI)
    if username in df['username'].values:
        return False                       # Username allaqachon mavjud
    df = pd.concat([df, pd.DataFrame([[username, password]], columns=["username", "password"])], ignore_index=True)
    df.to_csv(FAYL_NOMI, index=False)
    return True
#--------------------------------------------------------------------------------------------------------------------------
def tizimga_kirish(username, password):
    df = pd.read_csv(FAYL_NOMI)
    user = df[(df["username"] == username) & (df["password"] == password)]
    return not user.empty
#--------------------------------------------------------------------------------------------------------------------------
def saqlash(username, sana, toifa, izoh, summa):
    yangi = pd.DataFrame([[username,sana, toifa, izoh,summa]], columns=["username", "sana", "toifa", "izoh","summa"])
    df1 = pd.read_csv(EXPENSE_FILE)
    df1 = pd.concat([df1, yangi], ignore_index=True)
    df1.to_csv(EXPENSE_FILE, index=False)
    # df = pd.read_csv(EXPENSE_FILE)
    # df.loc[len(df.index)] = [username, sana, toifa, izoh, summa]
    # df.to_csv(EXPENSE_FILE, index=False)
#----------------------------------------------------------------------------------------------------------------------
def yuklash(username):
    df = pd.read_csv(EXPENSE_FILE)
    return df[df["username"] == username]
#----------------------------------------------------------------------------------------------------------------------

def main():

    if 'step' not in st.session_state:
        st.session_state.step=0

    st.title(" Oddiy Login / Ro'yxatdan o'tish tizimi")
    tanlov = st.radio("Bolimni tanlang:", ["Ro'yxatdan o'tish", "Kirish"])
    if tanlov == "Ro'yxatdan o'tish":
        st.subheader("Yangi foydalanuvchi")
        username = st.text_input("Username")
        password = st.text_input("Parol", type="password")
        if st.button("Ro'yxatdan o'tish"):
            if royxatdan_otish(username, password):
                st.success("Ro'yxatdan otish muvaffaqiyatli! Endi kiring.")
            else:
                st.error("Bu username allaqachon mavjud.")
                st.rerun()
    elif tanlov == "Kirish":
        st.subheader("Tizimga kirish")
        username = st.text_input("Username")
        password = st.text_input("Parol", type="password")
        if st.button("Kirish"):
            if tizimga_kirish(username, password):
                st.success(f"Xush kelibsiz, {username}!")
                st.session_state.step=1
            else:
                st.error("Username yoki parol noturi.")
                st.rerun()

# -----------------asosiy menu------------------------------------------------------
    
    if st.session_state.step==1:

        sidebar=st.sidebar.selectbox('bollimni tanlang',('Menu','statistks'))
        if sidebar=='Menu':  
            st.subheader('kunlik harajatlaringizni saqlab boring')
            # --------userdan infolarni qabul qilamiz----------
            sana = st.date_input("Sana", value=date.today())
            toifa = st.selectbox("Toifa", ["Ovqat", "Transport", "Kongilochar", "Kiyim", "Boshqa"])
            izoh = st.text_input("Izoh")
            summa = st.number_input("Summa (som)", min_value=0.0)

            if st.button("Saqlash"):
                saqlash(username, sana, toifa, izoh, summa)
                st.success("Harajat saqlandi!")
            # Ma'lumotlarni ko‘rsatish-----------
                st.subheader("Xarajatlar ro'yxati")
                df = pd.read_csv(EXPENSE_FILE)
                st.dataframe(df)

        if sidebar=='statistks':
            st.write('bu yerda turli statistik malumotlar boladi')
            
         
if __name__ == "__main__":
    main()
