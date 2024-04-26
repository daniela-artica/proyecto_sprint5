import pandas as pd
import plotly_express as px
import streamlit as st
car_data = pd.read_csv(
    "C:/Users/steph/Documents/python_projects/proyecto_sprint5/vehicles_us.csv")
st.header("Datos de anuncios de coches")
hist_button = st.button("Construir histograma")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")
    gif = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(gif, use_container_width=True)
