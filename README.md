# 👕 Retail Inventory ETL Pipeline (Migración de Sistema)

## 📌 Descripción del Proyecto
Este proyecto es un pipeline **ETL (Extract, Transform, Load)** automatizado, desarrollado en Python, diseñado para resolver un problema real de negocio: la migración de datos de un sistema de gestión de stock de ropa (legacy) a una nueva plataforma de punto de venta e inventario.

El script elimina la necesidad de procesar manualmente planillas de cálculo, estandarizando los datos crudos y preparándolos para una importación limpia y sin errores en el nuevo sistema.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías principales:** `pandas` (Manipulación y análisis de datos).
* **Formatos de datos:** Excel (`.xlsx`).

## ⚙️ Arquitectura del Pipeline (ETL)

1. **Extract (Extracción):** * Ingesta automatizada del archivo crudo exportado desde el sistema de origen (`articulos_exportados.xlsx`).
   
2. **Transform (Transformación):**
   * **Filtrado Dimensional:** Reducción del dataset original extrayendo únicamente las columnas críticas para el negocio (ID, código de barras, nombre, marca, precio de venta y curva de talles desde XXS hasta XXL).
   * **Estandarización de Esquema (Schema Mapping):** Renombrado de variables mediante diccionarios para hacer coincidir el esquema de datos extraído con los requerimientos exactos de la base de datos del nuevo sistema destino.

3. **Load (Carga):**
   * Exportación del dataset procesado a un nuevo archivo (`articulos_exportados_limpio.xlsx`), sin índices autogenerados, dejándolo 100% listo para la ingesta final en el nuevo software.
