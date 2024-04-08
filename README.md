# Proyecto de Data sobre Carritos Abandonados

Este proyecto tiene como objetivo analizar el comportamiento de los usuarios en un e-commerce para identificar y comprender los carritos abandonados. A través de la recopilación, transformación y análisis de datos, buscamos obtener información valiosa que pueda utilizarse para mejorar la experiencia del usuario y aumentar las conversiones.

## User Stories

1. Como Gerente de Ventas, quiero poder visualizar el comportamiento de los clientes que finalizaron la compra y aquellos que abandonaron el carrito para identificar patrones y oportunidades de mejora en el proceso de compra.

2. Como Gerente de Ventas, necesito tener KPIs relevantes, para tomar decisiones informadas y optimizar estrategias de ventas.

3. Como Gerente, deseo contar con un sistema de predicción que utilice datos históricos y variables relevantes del cliente para identificar posibles compradores potenciales y anticipar el abandono del carrito, permitiéndome tomar acciones preventivas.

## Features

-**Modelo de predicción como aplicación web:** Desarrollar un modelo de predicción utilizando técnicas de machine learning para predecir el abandono del carrito de compras. La aplicación web permitirá a los usuarios, ingresando datos del cliente, obtener una predicción de si es probable que abandone el carrito o finalice la compra.


-**Dashboard interactivo con filtros:** Crear un dashboard interactivo que permita al Gerente de Ventas visualizar y analizar de forma dinámica el comportamiento de los clientes. Incluir filtros para segmentar datos por diferentes variables para obtener insights significativos.

## Mockup del Dashboard

![Mockup del Dashboard]("assets\Mockup_dashboard_carritos.pdf")

## Stack Tecnológico

![Mockup del Dashboard](assets\Stack Tecnológico.png)

## ETL (Extracción, Transformación y Carga)

El archivo [`proceso_etl.py`](proceso_etl.py) en este repositorio contiene el código necesario para llevar a cabo el proceso ETL. Este script se encarga de extraer datos relevantes, transformarlos según sea necesario y cargarlos en una base de datos para su posterior análisis.

## Raw Data

La carpeta `rawdata` contiene el dataset en bruto que utilizaremos para este proyecto.

