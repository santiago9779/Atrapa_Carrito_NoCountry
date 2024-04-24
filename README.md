# Proyecto de Análisis de Carritos Abandonados

## Introducción
Este proyecto se centra en el análisis de carritos abandonados con el objetivo de proporcionar a los clientes una herramienta predictiva que les permita anticiparse a este comportamiento y tomar medidas correctivas. Para lograr este objetivo, el equipo realizó un proceso integral que abarcó desde la extracción, transformación y carga de datos (ETL), hasta el desarrollo y despliegue de un modelo de machine learning, así como la creación de un dashboard con insights clave y el cálculo de KPIs relevantes.

## Equipo
- Santiago Velásquez: Data Engineer
- Agustín Molins: ETL Developer
- Jesé Muñoz: Machine Learning Developer
- Florencia Peluffo: Data Analyst
- Lucas Koch: Data Analyst
## User Stories

1. Como Gerente de Ventas, quiero poder visualizar el comportamiento de los clientes que finalizaron la compra y aquellos que abandonaron el carrito para identificar patrones y oportunidades de mejora en el proceso de compra.

2. Como Gerente de Ventas, necesito tener KPIs relevantes, para tomar decisiones informadas y optimizar estrategias de ventas.

3. Como Gerente, deseo contar con un sistema de predicción que utilice datos históricos y variables relevantes del cliente para identificar posibles compradores potenciales y anticipar el abandono del carrito, permitiéndome tomar acciones preventivas.

## Descripción del Proceso
1. **Extracción de Datos**: Se utilizó un dataset sobre carritos abandonados como punto de partida para el proyecto.
   
2. **Transformación y Carga de Datos (ETL)**: Se llevó a cabo un proceso de limpieza, transformación y preparación de los datos utilizando Python. Este paso fue fundamental para garantizar la calidad y coherencia de los datos utilizados en el análisis y modelado subsiguientes.
- [`Proceso ETL`](proceso_etl.py)

3. **Desarrollo del Modelo de Machine Learning**: Se construyó un modelo de machine learning capaz de predecir la probabilidad de abandono de un carrito por parte de un cliente. Este modelo se entrenó utilizando técnicas de aprendizaje supervisado y se evaluó su rendimiento para garantizar su eficacia.

4. **Despliegue del Modelo en una Aplicación Web**: Se utilizó Streamlit para desarrollar una aplicación web donde los clientes pueden ingresar datos relevantes y obtener predicciones sobre el abandono de carritos en tiempo real.

5. **Creación del Dashboard de Insights**: Se diseñó un dashboard interactivo que proporciona a los usuarios una visión completa de los principales insights obtenidos del análisis de los datos. Este dashboard ayuda a identificar tendencias, patrones y áreas de mejora relacionadas con el comportamiento de los clientes.

6. **Cálculo de KPIs**: Se definieron y calcularon indicadores clave de rendimiento (KPIs) relacionados con el proceso de compra y el abandono de carritos. Estos KPIs proporcionan métricas cuantitativas que ayudan a medir el éxito del proyecto y a identificar áreas de oportunidad.

## Objetivos del Proyecto
- Ofrecer al cliente una herramienta predictiva para anticiparse al abandono de carritos por parte de los clientes.
- Proporcionar un dashboard personalizado con insights relevantes para la toma de decisiones.
- Entregar informes periódicos que ayuden a monitorear el rendimiento y realizar ajustes estratégicos según sea necesario.

## Conclusiones
El proyecto de análisis de carritos abandonados ha permitido al cliente obtener una comprensión más profunda del comportamiento de sus clientes y tomar medidas proactivas para mejorar la retención y la satisfacción del cliente. El despliegue del modelo de machine learning en una aplicación web, junto con el dashboard de insights y los KPIs calculados, proporciona una solución integral que puede adaptarse y evolucionar con las necesidades del negocio.

## Features

-**Modelo de predicción como aplicación web:** Desarrollar un modelo de predicción utilizando técnicas de machine learning para predecir el abandono del carrito de compras. La aplicación web permitirá a los usuarios, ingresando datos del cliente, obtener una predicción de si es probable que abandone el carrito o finalice la compra.

-[Link a la app](https://atrapa-carritos.streamlit.app/)

-**Dashboard interactivo con filtros:** Crear un dashboard interactivo que permita al Gerente de Ventas visualizar y analizar de forma dinámica el comportamiento de los clientes. Incluir filtros para segmentar datos por diferentes variables para obtener insights significativos.

-[Mockup del Dashboard](assets/Mockup_dashboard_carritos.pdf)

-[Link al dashboard](https://app.powerbi.com/view?r=eyJrIjoiNTA2ZmZiOGItMDZiZS00MTc5LWE5MzgtYTFmMDk4MmEyMzllIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9)

## Stack Tecnológico

![Stack tecnológico](assets/Stack%20Tecnológico.png)

## ETL (Extracción, Transformación y Carga)

El archivo [`proceso_etl.py`](proceso_etl.py) en este repositorio contiene el código necesario para llevar a cabo el proceso ETL. Este script se encarga de extraer datos relevantes, transformarlos según sea necesario y cargarlos en una base de datos para su posterior análisis.

## Raw Data

La carpeta `rawdata` contiene el dataset en bruto que utilizaremos para este proyecto.

