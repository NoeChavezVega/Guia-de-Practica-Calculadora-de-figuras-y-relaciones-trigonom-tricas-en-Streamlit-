import streamlit as st
import math 
st.title("Calculadora de figuras y Relaciones trigonometricas en Streamlit")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")
st.title("Figuras geometricas")
figura = st.selectbox("Seleccionar figura",["Cuadrado","Rectangulo","Triangulo","Circulo"])
if figura == "Circulo":
  radio = st.number_input("selecciona el radio", 0.0, 20.0, 5.0)
  area = math.pi * radio**2
  st.write(f"El area del circulo con radio {radio} es:{area:.2f}")
  perimetro = 2*math.pi*radio
  st.write(f"El perimetro del circulo con radio {radio} es:{area:.2f}")

elif figura == "Triangulo":
  base = st.number_input("selecciona la base", 0.0, 20.0, 5.0)
  altura = st.number_input("selecciona la altura", 0.0, 20.0, 5.0)
  lado_a = st.number_input("selecciona lado_a", 0.0, 20.0, 5.0)
  lado_b = st.number_input("selecciona lado_b", 0.0, 20.0, 5.0)
  area = 0.5 * base * altura
  st.write(f"El area del triangulo con base {base} y altura {altura} es:{area:.2f}")
  perimetro = base + lado_a + lado_b 
  st.write(f"El perimetro del triangulo con lado_a {lado_a} y lado_b {lado_b}  es:{perimetro:.2f}")

elif figura == "Rectangulo":
  base = st.number_input("selecciona la base", 0.0, 20.0, 5.0)
  altura = st.number_input("selecciona la altura", 0.0, 20.0, 5.0)
  
 




