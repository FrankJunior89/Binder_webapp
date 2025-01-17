import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.header('Streamlit and Plotly')


df = px.data.gapminder()

countries = st.multiselect(
    "Country",
    df.country.values
)


if countries != None:
    fig = px.line(df[df['country'].isin(countries)],
                x='year',
                y='lifeExp',
                color='country',
                title="LifeExpectancy over time in France, Germany and Poland")
    
    st.plotly_chart(fig)
    


