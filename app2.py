import streamlit as st
import math 
import numpy as np 
import matplotlib.pyplot as plt
st.title("📐Calculadora de figuras y Relaciones trigonometricas en Streamlit📐")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")
st.title("Figuras geometricas")
figura = st.selectbox("Seleccionar figura",["🟦Cuadrado🟦","⬛Rectangulo⬛","🔺Triangulo🔺","⚪Circulo⚪"])
color = st.color_picker("Selecciona el color de la figura")
if figura == "⚪Circulo⚪":
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
  
  
   
  
  

elif figura == "🔺Triangulo🔺":
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
  triangle = plt.Polygon(((0, 0), (base, 0), (base / 2, altura)), closed=True, color=color, fill=False)
  ax.add_artist(triangle)
  ax.set_xlim(-1, base + 1)
  ax.set_ylim(-1, altura + 1)
  ax.set_aspect("equal")
  ax.set_title("Triángulo")
  st.pyplot(fig)

elif figura == "⬛Rectangulo⬛":
  base = st.number_input("Seleccione la base", 0.0, 20.0, 5.0)
  altura = st.number_input("Seleccione la altura", 0.0, 20.0, 5.0)
  area = base * altura
  st.write(f"El area del rectangulo con base {base} y altura {altura} es:{area:.2f}")
  perimetro = 2 * (base + altura)
  st.write(f"El perimetro del rectangulo con base {base} y altura {altura} es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  fig, ax = plt.subplots()
  rectangle = plt.Rectangle((0, 0), base, altura, color=color, fill=False)
  ax.add_artist(rectangle)
  ax.set_xlim(-1, base + 1)
  ax.set_ylim(-1, altura + 1)
  ax.set_aspect("equal")
  ax.set_title("Rectángulo")
  st.pyplot(fig)


  
  

elif figura == "🟦Cuadrado🟦":
  lado = st.number_input("Seleccione la base", 0.0, 20.0, 5.0)
  area = lado**2
  st.write(f"El area del cuadrado con lado {lado} es:{area:.2f}")
  perimetro = 4*lado
  st.write(f"El perimetro del cuadrado con lado {lado} es:{perimetro:.2f}")
  st.success(f"Calculos realizados correctamente para la figura seleccionada:{figura}")
  fig, ax = plt.subplots()
  square = plt.Rectangle((0, 0), lado, lado, edgecolor=color)
  ax.add_artist(square)
  ax.set_xlim(-1, lado + 1)
  ax.set_ylim(-1, lado + 1)
  ax.set_aspect("equal")
  ax.set_title("Cuadrado")
  st.pyplot(fig)

st.title(" Relaciones Trigonométricas")
angulo = st.slider("Selecciona un ángulo (en grados)", 0, 360, 45)
radianes = math.radians(angulo)

seno = math.sin(radianes)
coseno = math.cos(radianes)
tangente = math.tan(radianes) if coseno != 0 else float('inf')

st.metric("Seno", f"{seno:.3f}")
st.metric("Coseno", f"{coseno:.3f}")
st.metric("Tangente", f"{tangente:.3f}" if coseno != 0 else "Infinito")

# Graficar funciones trigonométricas
x = np.linspace(0, 2 * np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

fig, ax = plt.subplots()
ax.plot(x, y_sin, label="Seno", color="#FF5733")
ax.plot(x, y_cos, label="Coseno", color="#33C1FF")
ax.plot(x, y_tan, label="Tangente", color="#4CAF50", linestyle="--")
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_title("Funciones Trigonométricas")
ax.legend()
ax.grid(True)
st.pyplot(fig)
plt.close(fig))














  





