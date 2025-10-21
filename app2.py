import streamlit as st
import math 
import numpy as np 
st.title("📐Calculadora de figuras y Relaciones trigonometricas en Streamlit📐")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")
st.title("Figuras geometricas")
figura = st.selectbox("Seleccionar figura",["🟦Cuadrado🟦","⬛Rectangulo⬛","🔺Triangulo🔺","⚪Circulo⚪"])
color = st.color_picker("Selecciona el color de la figura", "#FF0000")
if figura == "Circulo":
  radio = st.number_input("selecciona el radio", 0.0, 20.0, 5.0)
  area = math.pi * radio**2
  st.write(f"El area del circulo con radio {radio} es:{area:.2f}")
  perimetro = 2*math.pi*radio
  st.write(f"El perimetro del circulo con radio {radio} es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  st.success(f"Cálculos y visualización realizados correctamente para: {figura}")
  fig, ax = plt.subplots()
  circle = plt.Circle((0,0), radio, color=color, fill=False)
  ax.add_artist(circle)
  ax.set_xlim(-radio*1.5, radio*1.5)
  ax.set_ylim(-radio*1.5, radio*1.5)
  ax.set_aspect('equal')
  st.pyplot(fig)
  
  

elif figura == "Triangulo":
  base = st.number_input("selecciona la base", 0.0, 20.0, 5.0)
  altura = st.number_input("selecciona la altura", 0.0, 20.0, 5.0)
  lado_a = st.number_input("selecciona lado_a", 0.0, 20.0, 5.0)
  lado_b = st.number_input("selecciona lado_b", 0.0, 20.0, 5.0)
  area = 0.5 * base * altura
  st.write(f"El area del triangulo con base {base} y altura {altura} es:{area:.2f}")
  perimetro = base + lado_a + lado_b 
  st.write(f"El perimetro del triangulo con lado_a {lado_a} y lado_b {lado_b}  es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  fig, ax = plt.subplots()
  triangle = plt.Polygon(((0,0),(base,0),(base/2, altura)), closed=True, color=color, fill=False)
  ax.add_artist(triangle)
  ax.set_xlim(-1, base + 1)
  ax.set_ylim(-1, altura + 1)
  ax.set_aspect('equal')
  st.pyplot(fig)

elif figura == "Rectangulo":
  base = st.number_input("Seleccione la base", 0.0, 20.0, 5.0)
  altura = st.number_input("Seleccione la altura", 0.0, 20.0, 5.0)
  area = base * altura
  st.write(f"El area del rectangulo con base {base} y altura {altura} es:{area:.2f}")
  perimetro = 2 * (base + altura)
  st.write(f"El perimetro del rectangulo con base {base} y altura {altura} es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  fig, ax = plt.subplots()
  rectangle = plt.Rectangle((0,0), base, altura,  color=color, fill=False)
  ax.add_artist(rectangle)
  ax.set_xlim(-1, base + 1)
  ax.set_ylim(-1, altura + 1)
  ax.set_aspect('equal')
  st.pyplot(fig)

  
  

elif figura == "Cuadrado":
  lado = st.number_input("Seleccione la base", 0.0, 20.0, 5.0)
  area = lado**2
  st.write(f"El area del cuadrado con lado {lado} es:{area:.2f}")
  perimetro = 4*lado
  st.write(f"El perimetro del cuadrado con lado {lado} es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  fig, ax = plt.subplots()
  square = plt.Rectangle((0,0), lado, lado,  color=color, fill=False)
  ax.add_artist(square)
  ax.set_xlim(-1, lado + 1)
  ax.set_ylim(-1, lado + 1)
  ax.set_aspect('equal')
  st.pyplot(fig)
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Calculadora de Figuras y Trig", layout="centered")
st.title("📐 Calculadora de figuras y relaciones trigonométricas 📐")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")

# Mapa: clave interna -> etiqueta mostrada (con emoji)
etiquetas = {
    "Cuadrado": "🟦 Cuadrado 🟦",
    "Rectangulo": "⬛ Rectángulo ⬛",
    "Triangulo": "🔺 Triángulo 🔺",
    "Circulo": "⚪ Círculo ⚪"
}

figura = st.selectbox("Seleccionar figura", options=list(etiquetas.keys()), format_func=lambda k: etiquetas[k])

color = st.color_picker("Selecciona el color de la figura", "#FF0000")

if figura == "Circulo":
    radio = st.number_input("Selecciona el radio", 0.0, 20.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.write(f"El área del círculo con radio {radio} es: {area:.2f}")
    st.write(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")
    st.success(f"Cálculos y visualización realizados correctamente para: {etiquetas[figura]}")

    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radio, edgecolor=color, fill=False, linewidth=2)
    ax.add_artist(circle)
    ax.set_xlim(-radio * 1.5, radio * 1.5)
    ax.set_ylim(-radio * 1.5, radio * 1.5)
    ax.set_aspect("equal")
    ax.set_title("Círculo")
    st.pyplot(fig)

elif figura == "Triangulo":
    base = st.number_input("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.number_input("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.number_input("Selecciona lado_a", 0.0, 20.0, 5.0)
    lado_b = st.number_input("Selecciona lado_b", 0.0, 20.0, 5.0)
    area = 0.5 * base * altura
    perimetro = base + lado_a + lado_b
    st.write(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f}")
    st.write(f"El perímetro del triángulo es: {perimetro:.2f}")
    st.success(f"Cálculos y visualización realizados correctamente para: {etiquetas[figura]}")

    fig, ax = plt.subplots()
    triangle = plt.Polygon(((0, 0), (base, 0), (base / 2, altura)), closed=True, edgecolor=color, fill=False, linewidth=2)
    ax.add_artist(triangle)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect("equal")
    ax.set_title("Triángulo")
    st.pyplot(fig)

elif figura == "Rectangulo":
    base = st.number_input("Seleccione la base", 0.0, 20.0, 5.0, key="rect_base")
    altura = st.number_input("Seleccione la altura", 0.0, 20.0, 5.0, key="rect_altura")
    area = base * altura
    perimetro = 2 * (base + altura)
    st.write(f"El área del rectángulo con base {base} y altura {altura} es: {area:.2f}")
    st.write(f"El perímetro del rectángulo es: {perimetro:.2f}")
    st.success(f"Cálculos y visualización realizados correctamente para: {etiquetas[figura]}")

    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((0, 0), base, altura, edgecolor=color, fill=False, linewidth=2)
    ax.add_artist(rectangle)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect("equal")
    ax.set_title("Rectángulo")
    st.pyplot(fig)

elif figura == "Cuadrado":
    lado = st.number_input("Seleccione el lado", 0.0, 20.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.write(f"El área del cuadrado con lado {lado} es: {area:.2f}")
    st.write(f"El perímetro del cuadrado es: {perimetro:.2f}")
    st.success(f"Cálculos y visualización realizados correctamente para: {etiquetas[figura]}")

    fig, ax = plt.subplots()
    square = plt.Rectangle((0, 0), lado, lado, edgecolor=color, fill=False, linewidth=2)
    ax.add_artist(square)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)
    ax.set_aspect("equal")
    ax.set_title("Cuadrado")
    st.pyplot(fig)










  





