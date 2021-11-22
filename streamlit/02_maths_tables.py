import streamlit as st
import plotly.graph_objects as grph_obj

st.title("Math Tables in 2021", anchor=None)


num = st.slider('Which times tables do you want to display', 1, 100, 7)

values = [str(num), str(num)+"*x="]
fig = grph_obj.Figure(data=[grph_obj.Table(header=dict(values=[str(num), str(num)+"*x="]),
                 cells=dict(values=[[str(num)+"*"+str(i)+"=" for i in range(1,10)], [num*i for i in range(1,10)]]))
                     ])

st.write(fig)