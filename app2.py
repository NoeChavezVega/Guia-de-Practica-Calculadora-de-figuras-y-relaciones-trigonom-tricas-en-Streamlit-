import streamlit as st
import math 
st.title("Calculadora de figuras y Relaciones trigonometricas en Streamlit")
st.title("Figuras geometricas")
figura = st.selectbox("Seleccionar figura",["Cuadrado","Rectangulo","Triangulo","Circulo"])
area = None
Perimetro = None
if figura == "Cuadrado":
  radio = st.slider("selecciona el radio", 0.0, 10.0, 5.0)
area = math.pi * radio**2
st.write(f"El area del circulo con radio {radio} es:{area:.2f}")
