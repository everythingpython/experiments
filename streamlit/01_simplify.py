from os import stat
import streamlit as st
import pandas as pd

pd.get_option("display.max_colwidth",100000)

def display(df,columns_to_display):
    placeholder = st.empty()
    with placeholder.container():
        st.write(df[columns_to_display])
        st.write(f"Columns in file - {df.columns}")

def filter(df, levels, columns):
    print(levels)
    df = df.astype(str).apply(lambda x: x.str[:100]).dropna()
    df = df[df['Level']==levels][columns]
    st.table(df)

@st.cache
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

        
st.title("Log File Look-up-er", anchor=None)

uploaded_file = st.file_uploader("Choose a file")

try:
    if uploaded_file:
        df = load_data(uploaded_file)
        columns_to_display = st.multiselect("Columns to display:", df.columns)
        col1, col2 = st.columns(2)
        button1 = col1.button(label="Display")


        if button1:
            my_container = st.container() #expander
            with my_container:
                display(df, columns_to_display)

        if df is not None:
            levels = list(set(df["Level"].to_list()))
            print(levels)
            
            option = st.sidebar.selectbox("Filter by:", levels) 

            if len(option) >0:
                button2 = col2.button(label="Filter")
                if button2:
                    my_container = st.container()
                    with my_container:
                        filter(df, option, columns_to_display)
except Exception as e:
    print(f"Error - {e}")



