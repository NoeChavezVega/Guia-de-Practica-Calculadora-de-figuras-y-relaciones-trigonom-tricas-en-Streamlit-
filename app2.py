import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("Calculadora de Figuras y Relaciones Trigonométricas en Streamlit")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")

st.header("Figuras Geométricas")

# Selección de figura
figura = st.selectbox("Seleccionar figura", ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"])

# Selector de color
color = st.color_picker("Elige un color para la figura", "#1f77b4")

# Cálculos y visualización
if figura == "Círculo":
    radio = st.number_input("Selecciona el radio", 0.0, 20.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.write(f"El área del círculo con radio {radio} es: {area:.2f}")
    st.write(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

    # --- Visualización ---
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=3)
    ax.add_artist(circle)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-radio*1.2, radio*1.2)
    ax.set_ylim(-radio*1.2, radio*1.2)
    ax.set_title("Círculo")
    st.pyplot(fig)

elif figura == "Triángulo":
    base = st.number_input("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.number_input("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.number_input("Selecciona lado_a", 0.0, 20.0, 5.0)
    lado_b = st.number_input("Selecciona lado_b", 0.0, 20.0, 5.0)
    area = 0.5 * base * altura
    perimetro = base + lado_a + lado_b
    st.write(f"El área del triángulo es: {area:.2f}")
    st.write(f"El perímetro del triángulo es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

    # --- Visualización ---
    fig, ax = plt.subplots()
    # Dibujamos un triángulo equilátero aproximado en base y altura
    ax.plot([0, base/2, base, 0], [0, altura, 0, 0], color=color, linewidth=3)
    ax.set_aspect('equal')
    ax.set_title("Triángulo")
    st.pyplot(fig)

elif figura == "Rectángulo":
    base = st.number_input("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.number_input("Selecciona la altura", 0.0, 20.0, 5.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.write(f"El área del rectángulo es: {area:.2f}")
    st.write(f"El perímetro del rectángulo es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

    # --- Visualización ---
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), base, altura, color=color, fill=False, linewidth=3)
    ax.add_patch(rect)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, base * 1.2)
    ax.set_ylim(0, altura * 1.2)
    ax.set_title("Rectángulo")
    st.pyplot(fig)

elif figura == "Cuadrado":
    lado = st.number_input("Selecciona el lado", 0.0, 20.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.write(f"El área del cuadrado con lado {lado} es: {area:.2f}")
    st.write(f"El perímetro del cuadrado con lado {lado} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")


    fig, ax = plt.subplots()
    cuadrado = plt.Rectangle((0, 0), lado, lado, color=color, fill=False, linewidth=3)
    ax.add_patch(cuadrado)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, lado * 1.2)
    ax.set_ylim(0, lado * 1.2)
    ax.set_title("Cuadrado")
    st.pyplot(fig)


  





