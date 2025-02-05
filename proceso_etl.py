import pandas as pd
import mysql.connector
import db_connect

df = pd.read_csv("rawdata\data_cart_abandonment.csv")

columnas = list(df)

# Contar celdas vacías
celdas_vacias = df.isnull().sum()

# Contar celdas nulas
celdas_nulas = df.isna().sum()

# Combinar resultados en un DataFrame
resultados = pd.DataFrame({
    "Columna": columnas,
    "Celdas vacías": celdas_vacias,
    "Celdas nulas": celdas_nulas
})

# Mostrar resultados
print(resultados)

# Cambio los nombres al español
nombres_español = ['ID', 'Detalles_Del_Producto_Vistos', 'Cant_Actividades_De_Sesión', 'Nro_Articulos_En_Carrito', 'Nro_Articulos_Eliminados_Del_Carrito', 'Nro_Visualizaciones_Del_Carrito', 'Nro_Pago_Exitoso', 'Nro_Pago_Iniciado', 'Nro_Visualizaciones_Articulos__Carrito', 'Nro_Inicios_Sesion', 'Nro_Paginas_VistaS', 'Tipo_De_Cliente', 'Carrito_Abandonado' ]
df.columns = nombres_español

# Hago un mapeo de valores en la columna Detalles_Del_Producto_Vistos, pasando de Yes/No a 1/0
df['Detalles_Del_Producto_Vistos'] = df['Detalles_Del_Producto_Vistos'].replace({'Yes': 1, 'No': 0})


# Relleno los valores nulos existentes en las columnas Nro_Articulos_En_Carrito y Nro_Visualizaciones_Del_Carrito con la mediana
mediana_articulos = df['Nro_Articulos_En_Carrito'].median()
df['Nro_Articulos_En_Carrito'].fillna(mediana_articulos, inplace=True)

mediana_visualizaciones = df['Nro_Visualizaciones_Del_Carrito'].median()
df['Nro_Visualizaciones_Del_Carrito'].fillna(mediana_visualizaciones, inplace=True)

## Cambio el tipo de dato float a int en las columnas Nro_Articulos_En_Carrito y Nro_Visualizaciones_Del_Carrito
float_a_int = ['Nro_Articulos_En_Carrito', 'Nro_Visualizaciones_Del_Carrito']
df[float_a_int]= df[float_a_int].astype(int)

# Elimino la columna de pagos exitosos, ya que no nos aporta nada de información (es inversamente proporcional a carrito abandonado)
df = df.drop('Nro_Pago_Exitoso', axis=1)

# Incremento en uno todos los registros de Nro_Paginas_Vistas
df['Nro_Paginas_VistaS'] = df['Nro_Paginas_VistaS'].apply(lambda x: x + 1)

# Eliminar los registros de 'Nro_Articulos_En_Carrito' que estén en 0 cuando 'Carrito_Abandonado' también es 0
df = df.loc[~((df['Nro_Articulos_En_Carrito'] == 0) & (df['Carrito_Abandonado'] == 0))]

df.info()

# Pasar el df a excel
df.to_excel("abandonment_cart_datos_procesados.xlsx", index=False)

# Conectar a la base de datos
#hecho en modulo db_connect


# Crear el cursor

connection = db_connect.conexion_db()

mycursor = connection.cursor()

sql = """
SELECT *
FROM prueba

"""
mycursor.execute(sql)
resultados = mycursor.fetchall()
df3 = pd.DataFrame(resultados)
print(df3)

# # Convertir el DataFrame a un formato compatible con MySQL y guardarlo, especificando las columnas
# df.to_sql("datos_carrito", connection, if_exists="replace")

# # Cerrar la conexión
# cursor = connection.cursor()
# connection.close()