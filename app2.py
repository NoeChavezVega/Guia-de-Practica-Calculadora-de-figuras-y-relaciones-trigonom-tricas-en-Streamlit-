import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración de la página
st.set_page_config(
    page_title="Geometría y Trigonometría",
    layout="wide"
)

st.title("Aplicación de Geometría y Trigonometría con Streamlit 📐")

# Usar st.tabs para organizar las secciones
tab_geometria, tab_trigonometria = st.tabs(["**1 & 2. Figuras Geométricas y Visualización**", "**3. Relaciones Trigonométricas**"])

with tab_geometria:
    st.header("Cálculo y Visualización de Figuras Geométricas")
    st.markdown("Selecciona una figura y sus parámetros para calcular su área y perímetro, y ver su representación.")
    
    # 1. Parte 1 — Figuras geométricas
    
    # 1. Usa un st.selectbox para elegir la figura
    figura = st.selectbox(
        "Elige la figura geométrica:",
        ("Círculo", "Triángulo", "Rectángulo", "Cuadrado")
    )
    
    st.markdown("---")
    
    # Variables para parámetros
    radio, base, altura, lado, a, b, c = None, None, None, None, None, None, None
    area, perimetro = 0.0, 0.0
    
    # 2. Muestra solo los parámetros relevantes para la figura seleccionada
    if figura == "Círculo":
        st.subheader("Parámetros del Círculo")
        radio = st.number_input("Radio (r)", min_value=0.1, value=5.0, step=0.1)
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
    
    elif figura == "Triángulo":
        st.subheader("Parámetros del Triángulo")
        st.markdown("Para Área: Ingresa Base y Altura.")
        base = st.number_input("Base (b)", min_value=0.1, value=6.0, step=0.1)
        altura = st.number_input("Altura (h)", min_value=0.1, value=4.0, step=0.1)
        st.markdown("Para Perímetro: Ingresa los 3 lados (a, b, c).")
        a = st.number_input("Lado a", min_value=0.1, value=5.0, step=0.1)
        b = st.number_input("Lado b", min_value=0.1, value=6.0, step=0.1)
        c = st.number_input("Lado c", min_value=0.1, value=7.0, step=0.1)
        
        area = 0.5 * base * altura
        perimetro = a + b + c
    
    elif figura == "Rectángulo":
        st.subheader("Parámetros del Rectángulo")
        base = st.number_input("Base (b)", min_value=0.1, value=8.0, step=0.1)
        altura = st.number_input("Altura (h)", min_value=0.1, value=5.0, step=0.1)
        
        area = base * altura
        perimetro = 2 * (base + altura)
    
    elif figura == "Cuadrado":
        st.subheader("Parámetros del Cuadrado")
        lado = st.number_input("Lado (l)", min_value=0.1, value=4.0, step=0.1)
        
        area = lado ** 2
        perimetro = 4 * lado

    # 3 & 4. Calcula y Muestra los resultados
    col_area, col_perimetro = st.columns(2)
    with col_area:
        st.metric(label=f"Área del {figura}", value=f"{area:.2f}")
    with col_perimetro:
        st.metric(label=f"Perímetro del {figura}", value=f"{perimetro:.2f}")
    
    st.markdown("---")
    
    # 2. Parte 2 — Visualización
    st.subheader(f"Visualización del {figura}")
    
    # Permite cambiar color
    color = st.color_picker("Elige el color de la figura", "#1f77b4")
    
    # Crear la figura de Matplotlib
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off() # Ocultar ejes
    
    # Dibujar la figura seleccionada
    try:
        if figura == "Círculo" and radio is not None:
            # Ejemplo de la instrucción: circle = plt.Circle((0, 0), radio, color=color, fill=False)
            circulo = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=2)
            ax.add_artist(circulo)
            ax.set_xlim(-radio * 1.5, radio * 1.5)
            ax.set_ylim(-radio * 1.5, radio * 1.5)
        
        elif figura == "Triángulo" and a is not None and b is not None and c is not None:
            # Se dibuja un triángulo simple, no necesariamente con las longitudes a, b, c
            # Usaremos una representación genérica (un triángulo con base en el eje x)
            # Para una representación precisa necesitaría más trigonometría y validación (desigualdad triangular)
            # Para mantenerlo simple, usaremos un triángulo rectángulo para la visualización por defecto.
            puntos = np.array([[0, 0], [base, 0], [base, altura]])
            triangulo = plt.Polygon(puntos, closed=True, color=color, fill=False, linewidth=2)
            ax.add_patch(triangulo)
            ax.set_xlim(-1, base + 1)
            ax.set_ylim(-1, altura + 1)
        
        elif figura == "Rectángulo" and base is not None and altura is not None:
            rectangulo = plt.Rectangle((0, 0), base, altura, color=color, fill=False, linewidth=2)
            ax.add_patch(rectangulo)
            ax.set_xlim(-1, base + 1)
            ax.set_ylim(-1, altura + 1)
            
        elif figura == "Cuadrado" and lado is not None:
            cuadrado = plt.Rectangle((0, 0), lado, lado, color=color, fill=False, linewidth=2)
            ax.add_patch(cuadrado)
            ax.set_xlim(-1, lado + 1)
            ax.set_ylim(-1, lado + 1)
            
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error al dibujar la figura: {e}")

with tab_trigonometria:
    # 3. Parte 3 — Relaciones trigonométricas
    st.header("Gráficas de Funciones Trigonométricas")
    st.markdown("Visualiza las funciones seno, coseno y tangente, y ajusta su rango y amplitud.")
    
    # Parámetros para la gráfica
    col_amp, col_rango = st.columns(2)
    with col_amp:
        amplitud = st.slider("Amplitud", 0.1, 3.0, 1.0, 0.1)
    with col_rango:
        rango_max = st.slider("Rango de X (máximo, en $\pi$)", 1, 6, 2, 1)
    
    figura_trig, ax_trig = plt.subplots()
    
    # Definir el rango de x
    x = np.linspace(0, rango_max * np.pi, 500)
    
    # Crear los dataframes o gráficos individuales
    
    col_sin, col_cos, col_tan = st.columns(3)
    
    with col_sin:
        st.write("**Función Seno: $A \cdot \sin(x)$**")
        st.line_chart(amplitud * np.sin(x), use_container_width=True)
    
    with col_cos:
        st.write("**Función Coseno: $A \cdot \cos(x)$**")
        st.line_chart(amplitud * np.cos(x), use_container_width=True)

    with col_tan:
        st.write("**Función Tangente: $\\tan(x)$**")
        # st.line_chart no es ideal para la tangente debido a las asíntotas
        # Usamos Matplotlib para un mejor control
        y_tan = np.tan(x)
        # Limitar valores extremos para que Matplotlib pueda dibujar
        y_tan[y_tan > 10] = np.nan 
        y_tan[y_tan < -10] = np.nan
        
        fig_tan, ax_tan = plt.subplots()
        ax_tan.plot(x, y_tan, color='green')
        ax_tan.set_ylim(-10, 10)
        ax_tan.set_title("Tangente (límite $\pm 10$)")
        st.pyplot(fig_tan, use_container_width=True)

    st.markdown("---")
    
    # 4. Parte 4 — Extensión creativa (opcional)
    st.subheader("Extensión: Visualizador de Ondas Amortiguadas")
    
    col_freq, col_damp = st.columns(2)
    with col_freq:
        frecuencia = st.slider("Frecuencia ($k$)", 1.0, 10.0, 3.0, 0.1)
    with col_damp:
        amortiguacion = st.slider("Coeficiente de Amortiguación ($\\alpha$)", 0.05, 0.5, 0.1, 0.05)
    
    # f(x) = e^{-alpha * x} * sin(k * x)
    x_onda = np.linspace(0, 4 * np.pi, 1000)
    y_onda = np.exp(-amortiguacion * x_onda) * np.sin(frecuencia * x_onda)
    
    fig_onda, ax_onda = plt.subplots()
    ax_onda.plot(x_onda, y_onda, color='purple', label='$e^{-\\alpha x} \sin(kx)$')
    ax_onda.plot(x_onda, np.exp(-amortiguacion * x_onda), '--', color='grey', label='Envolvente $e^{-\\alpha x}$')
    ax_onda.plot(x_onda, -np.exp(-amortiguacion * x_onda), '--', color='grey')
    ax_onda.set_title(f"Onda Amortiguada: $\\alpha={amortiguacion}$, $k={frecuencia}$")
    ax_onda.legend()
    st.pyplot(fig_onda)

# Opcional: Calculadora de Pitágoras (se podría poner en una pestaña aparte o expander)
st.sidebar.header("Otras Herramientas")
with st.sidebar.expander("Calculadora de Pitágoras"):
    st.subheader("Teorema de Pitágoras $a^2 + b^2 = c^2$")
    cateto_a = st.number_input("Cateto a", min_value=0.1, value=3.0, step=0.1)
    cateto_b = st.number_input("Cateto b", min_value=0.1, value=4.0, step=0.1)
    hipotenusa_c = math.sqrt(cateto_a**2 + cateto_b**2)
    st.success(f"Hipotenusa (c) = $\\sqrt{{{cateto_a}^2 + {cateto_b}^2}} \\approx {hipotenusa_c:.2f}$")




  





