import streamlit as st
import math 
st.title("Calculadora de figuras y Relaciones trigonometricas en Streamlit")
st.title("Figuras geometricas")
figura = st.selectbox("Seleccionar figura",["Cuadrado","Rectangulo","Triangulo","Circulo"])
if figura == "Circulo":
  radio = st.slider("selecciona el radio", 0.0, 10.0, 5.0)
  area = math.pi * radio**2
  st.write(f"El area del circulo con radio {radio} es:{area:.2f}")
  perimetro = 2*math.pi*radio
  st.write(f"El perimetro del circulo con radio {radio} es:{area:.2f}")
  
elif figura == "Cuadrado":
  lado = st.slider("Selecciona el lado", 0.0, 10.0, 5.0)
area = lado**2
st.write(f"El area del Cuadrado con lado {lado} es:{area:.2f}")
perimetro = 4*lado
st.write(f"El perimetro del Cuadrado con lado {lado} es:{perimetro:.2f}")


elif figura == "Triangulo":
  base = st.number_input("Selecciona la base",0.0,10.0,5.0)
altura = st.slider("Selecciona la altura",0.0,10.0,5.0)
area= 0.5*base*altura

