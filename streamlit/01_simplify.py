from os import stat
import streamlit as st
import pandas as pd
pd.get_option("display.max_colwidth",100000)
status = 0

def display(df):
    placeholder = st.empty()
    with placeholder.container():
        st.write(df)
        st.write(f"Columns in file - {df.columns}")

def filter(df, levels, columns):
    print(levels)
    df = df[df['Level']==levels][columns]
    st.table(df)

@st.cache
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

state = 0

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    df = load_data(uploaded_file)
    button1 = st.button(label="Display")

    if button1:
        my_expander = st.container()
        with my_expander:
            display(df)

    if df is not None:
        levels = list(set(df["Level"].to_list()))
        print(levels)
        

        option = st.sidebar.selectbox("Filter by:", levels) 
        columns_to_display = st.multiselect("Columns to display:", df.columns)

        print(option)
        if len(option) >0:
            button2 = st.button(label="Filter")
            if button2:
                my_expander = st.container()
                with my_expander:
                    filter(df, option, columns_to_display)
            



