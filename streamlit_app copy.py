import streamlit as st
import pickle
import numpy as np

# Configurar el ancho total de la página
st.set_page_config(layout="wide")

# Cargar el modelo entrenado
modelo_path = 'modelo_entrenado.pkl'
with open(modelo_path, 'rb') as archivo:
    modelo = pickle.load(archivo)
    
# Función para predecir la probabilidad de abandono del carrito
def predecir_abandono_carrito(datos_cliente):
    X_cliente = np.array(datos_cliente).reshape(1, -1)
    probabilidad_abandono = modelo.predict(X_cliente)[:, 1]
    return probabilidad_abandono[0]

# Interfaz de usuario de la aplicación
st.title('Atrapa carritos')

# Subtítulo
st.markdown("<h3>Ingrese los detalles de la sesión que desea predecir</h3>", unsafe_allow_html=True)

column1, column2, column3 = st.columns(3)

with column1:
    detalles_producto = st.selectbox('Detalles de productos vistos', [0, 1])
    articulos_eliminados = st.number_input('Nro de articulos eliminados del carrito', min_value=0, step=1)
    sesiones_usuario = st.number_input('Nro de inicios de sesión', min_value=0, step=1)

with column2:
    paginas_cambiadas = st.number_input('Nro de visualizaciones a artículos del carrito', min_value=0, step=1)
    visualizaciones_carrito = st.number_input('Nro de visualizaciones del carrito', min_value=0, step=1)
    paginas_visitadas = st.number_input('Nro de páginas vistas', min_value=1, step=1)

with column3:
    articulos_carrito = st.number_input('Nro de articulos en el carrito', min_value=0, step=1)
    inicios_pago = st.number_input('Nro de pagos iniciados', min_value=0, step=1)
    tipo_cliente = st.selectbox('Tipo de cliente', [0, 1, 2])


if st.button('Predecir'):
    datos_cliente = [detalles_producto, paginas_cambiadas, articulos_carrito, articulos_eliminados, 
                      visualizaciones_carrito, inicios_pago, sesiones_usuario, paginas_visitadas, tipo_cliente]
    probabilidad_abandono = predecir_abandono_carrito(datos_cliente)
    st.write(f'La probabilidad de que el cliente abandone el carrito es: {probabilidad_abandono}')
