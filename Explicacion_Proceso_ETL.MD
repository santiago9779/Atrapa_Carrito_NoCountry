# Proceso ETL

Como primer paso del proyecto, y a partir del dataset [`data_cart_abandonment.csv`](rawdata/data_cart_abandonment.csv), extraímos los datos para limpiarlos, transformarlos y sacarle las inconsistencias para facilitar su posterior análisis.

### Cambio de Nombres de Columnas
Se cambiaron los nombres de las columnas del conjunto de datos al español para una mejor comprensión. Los nuevos nombres en español se asignaron a través de una lista `nombres_español`, y luego se aplicaron a las columnas del DataFrame.

### Mapeo de Valores en la Columna Detalles_Del_Producto_Vistos
Los valores "Yes" y "No" en la columna "Detalles_Del_Producto_Vistos" se mapearon a los valores binarios 1 y 0, respectivamente. Esto se realizó para estandarizar la representación de estos datos.

### Relleno de Valores Nulos
Se rellenaron los valores nulos en las columnas "Nro_Articulos_En_Carrito" y "Nro_Visualizaciones_Del_Carrito" con la mediana de cada columna. Esto se hizo ya que el número de registros no era para nada elevado (de hecho, eran 9 en cada columna), por lo que no alteraría los datos en su posterior análisis. Además, se decidió ello para evitar la pérdida de datos y para garantizar que todas las filas tengan valores válidos en estas columnas.

### Cambio del Tipo de Datos
Se cambió el tipo de datos de las columnas "Nro_Articulos_En_Carrito" y "Nro_Visualizaciones_Del_Carrito" de float a int. Esto se realizó para reflejar que estas columnas representan cantidades enteras y no fraccionales, y para que todas las columnas tengan el mismo tipo de dato, dando una consistencia superior.

### Eliminación de la Columna Nro_Pago_Exitoso
Se eliminó la columna "Nro_Pago_Exitoso" del conjunto de datos, ya que se consideró que no aportaba información relevante para el análisis y además estaba inversamente relacionada con la variable de interés "Carrito_Abandonado".

### Incremento de Valores en la Columna Nro_Paginas_Vistas
Se incrementaron en uno todos los valores en la columna "Nro_Paginas_Vistas". Esto debido a que el dataset arrancaba a contar desde 0, pero el equipo consideró que el mero hecho de entrar a la página ya debía contabilizarse como página vista.

### Eliminación de Registros Específicos
Se eliminaron los registros en los que la columna "Nro_Articulos_En_Carrito" estaba en 0 cuando la columna "Carrito_Abandonado" también era 0 ya que se trataba de una inconsistencia: un cliente no puede haber efectuado una compra sin antes haber agregado un sólo articulo al carrito.
