import streamlit as st

def main():
    st.title('Aplicación Básica de Streamlit')
    
    st.write('¡Hola Mundo!')
    
    # Agregar un slider para seleccionar un número
    numero = st.slider('Seleccione un número', 0, 100, 50)
    st.write('El número seleccionado es:', numero)
    
    # Agregar un checkbox
    if st.checkbox('Mostrar mensaje'):
        st.write('Este es un mensaje mostrado con Streamlit')

if __name__ == "__main__":
    main()