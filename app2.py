import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="centered", page_title="Calculadora de Figuras y Trigonometría")
st.title("Calculadora de Figuras y Relaciones Trigonométricas")
st.sidebar.write("**Autor:** Noe Chavez Vega")
st.sidebar.write("**Matrícula:** 377347")

# ----------------------------
# PARTE 1 Y 2: FIGURAS GEOMÉTRICAS
# ----------------------------
st.header("Parte 1 y 2 — Figuras Geométricas y Visualización")

figura = st.selectbox("Seleccionar figura", ["Cuadrado", "Rectangulo", "Triangulo", "Circulo"])
color = st.color_picker("Elige un color para la figura", "#1f77b4")

if figura == "Circulo":
    radio = st.number_input("Selecciona el radio", 0.0, 100.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")

    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=3)
    ax.add_artist(circle)
    ax.set_xlim(-radio * 1.2, radio * 1.2)
    ax.set_ylim(-radio * 1.2, radio * 1.2)
    ax.set_aspect("equal")
    ax.set_title("Círculo")
    st.pyplot(fig)
    plt.close(fig)

elif figura == "Triangulo":
    base = st.number_input("Selecciona la base", 0.0, 100.0, 6.0)
    altura = st.number_input("Selecciona la altura", 0.0, 100.0, 4.0)
    lado_a = st.number_input("Lado a", 0.0, 100.0, 5.0)
    lado_b = st.number_input("Lado b", 0.0, 100.0, 5.0)
    area = 0.5 * base * altura
    perimetro = base + lado_a + lado_b
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")

    fig, ax = plt.subplots()
    xs = [0, base / 2, base, 0]
    ys = [0, altura, 0, 0]
    ax.plot(xs, ys, linewidth=3, color=color)
    ax.set_aspect("equal")
    ax.set_title("Triángulo")
    st.pyplot(fig)
    plt.close(fig)

elif figura == "Rectangulo":
    base = st.number_input("Selecciona la base", 0.0, 100.0, 6.0)
    altura = st.number_input("Selecciona la altura", 0.0, 100.0, 4.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")

    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), base, altura, fill=False, linewidth=3, edgecolor=color)
    ax.add_patch(rect)
    ax.set_xlim(-1, base * 1.1)
    ax.set_ylim(-1, altura * 1.1)
    ax.set_aspect("equal")
    ax.set_title("Rectángulo")
    st.pyplot(fig)
    plt.close(fig)

elif figura == "Cuadrado":
    lado = st.number_input("Selecciona el lado", 0.0, 100.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")

    fig, ax = plt.subplots()
    sq = plt.Rectangle((0, 0), lado, lado, fill=False, linewidth=3, edgecolor=color)
    ax.add_patch(sq)
    ax.set_xlim(-1, lado * 1.1)




  





