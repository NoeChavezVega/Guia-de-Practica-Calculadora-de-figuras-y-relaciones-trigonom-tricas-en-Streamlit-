import streamlit as st
import math 

st.title("Calculadora de figuras y Relaciones trigonométricas en Streamlit")
st.sidebar.write("Noe Chavez Vega")
st.sidebar.write("377347")

st.title("Figuras geométricas")
figura = st.selectbox("Seleccionar figura", ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"])

if figura == "Círculo":
    radio = st.number_input("Selecciona el radio", 0.0, 20.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.write(f"El área del círculo con radio {radio} es: {area:.2f}")
    st.write(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

elif figura == "Triángulo":
    base = st.number_input("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.number_input("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.number_input("Selecciona lado_a", 0.0, 20.0, 5.0)
    lado_b = st.number_input("Selecciona lado_b", 0.0, 20.0, 5.0)
    area = 0.5 * base * altura
    perimetro = base + lado_a + lado_b 
    st.write(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f}")
    st.write(f"El perímetro del triángulo con lados {base}, {lado_a}, {lado_b} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

elif figura == "Rectángulo":
    base = st.number_input("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.number_input("Selecciona la altura", 0.0, 20.0, 5.0)
    area = base * altura 
    perimetro = 2 * (base + altura)
    st.write(f"El área del rectángulo con base {base} y altura {altura} es: {area:.2f}")
    st.write(f"El perímetro del rectángulo con base {base} y altura {altura} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")

elif figura == "Cuadrado":
    lado = st.number_input("Selecciona el lado", 0.0, 20.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.write(f"El área del cuadrado con lado {lado} es: {area:.2f}")
    st.write(f"El perímetro del cuadrado con lado {lado} es: {perimetro:.2f}")
    st.success(f"Cálculos realizados correctamente para la figura seleccionada: {figura}")



  





