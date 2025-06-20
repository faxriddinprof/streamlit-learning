import streamlit as st
import numpy as np
# Sidebar layout 

st.sidebar.title('This is Sidebar')
st.sidebar.write('you can place lelement like slidibar,buttons,and text here. ')
sitebar_input=st.sidebar.text_input('Enter somthing in this here')


st.title('This is my new project')


# tabs layout 

tab1,tab2,tab3=st.tabs(['Tab1','Tab2','Tab3'],)

with tab1:
    st.write('You are in Tab1')
    

with tab2:
    st.write('You are in Tab2')
with tab3:
    st.write('You are in Tab3')

# Columns layout 

col1,col2,col3=st.columns(3)

with col1:
    st.header('Column 1')
with col2:
    st.header('Column 2')
with col3:
    st.header('Column 3')


# bu chartlar bilan ishlashga bir misol
tap1, tap2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 4)
tap1.subheader("A tab with a chart")
tap1.line_chart(data)
tap2.subheader("A tab with the data")
tap2.write(data)

# container layout 

with st.container(border=True):
    st.write('Its a place that you ca do something')
    st.write('hush birnima birnima')


# emty placeholder

placeholder=st.empty()
placeholder.write('this is empty placeholder,useful for dynamic content.')

if st.button('Update Placeholder'):
    placeholder.write('The content of this placeholder ha been updated.')

# Expander

with st.expander('Enter for more details'):
    st.write('sen 1111 ni tanla')
    st.write('sen 2222 ni tanla ')
# popover (tooltip)

st.write('Hover over this buttons for a tooltip')
st.button('Button with tooltip',help='tis is a tooltip be careful !')

# sidebar input handling
if sitebar_input:
    st.write(f'You entered in this sidebar: {sitebar_input}')