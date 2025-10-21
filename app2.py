import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="centered", page_title="Calculadora de Figuras y Trigonometría")
st.title("Calculadora de Figuras y Relaciones Trigonométricas")
st.sidebar.write("**Autor:** Noe Chavez Vega")
st.sidebar.write("**Matrícula:** 377347")

# ----------------------------
# Crear pestañas para separar partes
# ----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Figuras Geométricas", "Visualización", "Trigonometría", "Extensión Creativa"])

# ----------------------------
# PARTE 1 — Figuras geométricas
# ----------------------------
with tab1:
    st.header("Parte 1 — Figuras Geométricas")
    figura = st.selectbox("Seleccionar figura", ["Cuadrado", "Rectangulo", "Triangulo", "Circulo"])
    
    if figura == "Circulo":
        radio = st.number_input("Radio", 0.0, 100.0, 5.0)
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")

    elif figura == "Triangulo":
        base = st.number_input("Base", 0.0, 100.0, 6.0)
        altura = st.number_input("Altura", 0.0, 100.0, 4.0)
        lado_a = st.number_input("Lado a", 0.0, 100.0, 5.0)
        lado_b = st.number_input("Lado b", 0.0, 100.0, 5.0)
        area = 0.5 * base * altura
        perimetro = base + lado_a + lado_b
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")

    elif figura == "Rectangulo":
        base = st.number_input("Base", 0.0, 100.0, 6.0)
        altura = st.number_input("Altura", 0.0, 100.0, 4.0)
        area = base * altura
        perimetro = 2 * (base + altura)
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")

    elif figura == "Cuadrado":
        lado = st.number_input("Lado", 0.0, 100.0, 5.0)
        area = lado**2
        perimetro = 4 * lado
        st.metric("Área", f"{area:.2f}")
        st.metric("Perímetro", f"{perimetro:.2f}")

# ----------------------------
# PARTE 2 — Visualización de figuras
# ----------------------------
with tab2:
    st.header("Parte 2 — Visualización de Figuras")
    color = st.color_picker("Elige un color para la figura", "#1f77b4")

    fig, ax = plt.subplots()
    
    if figura == "Circulo":
        circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=3)
        ax.add_artist(circle)
        ax.set_xlim(-radio*1.2, radio*1.2)
        ax.set_ylim(-radio*1.2, radio*1.2)
        ax.set_title("Círculo")
        
    elif figura == "Triangulo":
        xs = [0, base / 2, base, 0]
        ys = [0, altura, 0, 0]
        ax.plot(xs, ys, linewidth=3, color=color)
        ax.set_title("Triángulo")
        
    elif figura == "Rectangulo":
        rect = plt.Rectangle((0,0), base, altura, fill=False, linewidth=3, edgecolor=color)
        ax.add_patch(rect)
        ax.set_xlim(-1, base*1.1)
        ax.set_ylim(-1, altura*1.1)
        ax.set_title("Rectángulo")
        
    elif figura == "Cuadrado":
        sq = plt.Rectangle((0,0), lado, lado, fill=False, linewidth=3, edgecolor=color)
        ax.add_patch(sq)
        ax.set_xlim(-1, lado*1.1)
        ax.set_ylim(-1, lado*1.1)
        ax.set_title("Cuadrado")
    
    ax.set_aspect("equal")
    st.pyplot(fig)
    plt.close(fig)

# ----------------------------
# PARTE 3 — Relaciones trigonométricas
# ----------------------------
with tab3:
    st.header("Parte 3 — Relaciones Trigonométricas")
    rango = st.slider("Rango máximo (rad)", 0.1, 2*math.pi, 2*math.pi)
    amp = st.slider("Amplitud", 0.1, 2.0, 1.0)
    
    x = np.linspace(0, rango, 300)
    st.subheader("Función Seno")
    st.line_chart(amp * np.sin(x))
    
    st.subheader("Función Coseno")
    st.line_chart(amp * np.cos(x))
    
    st.subheader("Función Tangente")
    # limitar valores extremos para que no se corte la gráfica
    y_tan = np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan
    st.line_chart(amp * y_tan)

# ----------------------------
# PARTE 4 — Extensión creativa (opcional)
# ----------------------------
with tab4:
    st.header("Parte 4 — Extensión Creativa")
    
    st.subheader("Teorema de Pitágoras")
    cateto1 = st.number_input("Cateto 1", 0.0, 100.0, 3.0)
    cateto2 = st.number_input("Cateto 2", 0.0, 100.0, 4.0)
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    st.metric("Hipotenusa", f"{hipotenusa:.2f}")
    
    st.subheader("Visualizador de ondas: f(x) = e^(-0.1x) * sin(f*x)")
    freq = st.slider("Frecuencia", 0.1, 5.0, 1.0)
    amp_wave = st.slider("Amplitud", 0.1, 2.0, 1.0)
    x_wave = np.linspace(0, 20, 500)
    y_wave = amp_wave * np.exp(-0.1*x_wave) * np.sin(freq * x_wave)
    fig_wave, ax_wave = plt.subplots()
    ax_wave.plot(x_wave, y_wave, color="#FF33AA")
    ax_wave.set_title("Onda amortiguada")
    ax_wave.grid(True)
    st.pyplot(fig_wave)
    plt.close(fig_wave)





  





