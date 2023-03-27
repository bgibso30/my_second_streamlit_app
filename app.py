import streamlit as st
import pandas as pd
import altair as alt
import numpy as np



df = pd.read_csv(r'C:/Users/briaa/Documents/streamlit/customer_shopping_data.csv')

st.sidebar.header("Pick two variables for your bar chart")
x_val = st.sidebar.selectbox("Pick your x-axis",df.select_dtypes(include=object).columns.tolist())

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')




bar = alt.Chart(df).transform_aggregate(
    mean = 'mean(price)',
    groupby=[x_val]
).mark_bar().encode(
    x = alt.X(x_val, title=f'{x_val}'),
    y = alt.Y('mean:Q', title='average money spent (by or on)'),
    color = alt.Color(x_val)
).properties(
    title=(f'This is {user_name}\'s graph!')
    )

#(f'Hello {user_name}')

st.altair_chart(bar, use_container_width=True)
