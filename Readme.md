# 📊 Reto Técnico – Dashboard Interactivo de Campaña de Marketing

Este proyecto fue desarrollado como parte del proceso de prueba técnica para Alegra. Consiste en un análisis y visualización interactiva de datos de una campaña de marketing directo, con métricas clave y un dashboard web.

## 🧠 Funcionalidades

- Cálculo automático de KPIs:
  - Tasa de contacto efectivo
  - Conversión de clientes previos
  - Total de contactos
- Identificación del analista con mayor tasa de éxito
- Visualización de tasas de éxito por analista
- Dashboard visual e interactivo con [Plotly Dash](https://dash.plotly.com/)
- API REST con [FastAPI](https://fastapi.tiangolo.com/) para exponer los datos

## 📁 Estructura del proyecto

📦 proyecto_alegra/
├── marketing_dashboard.py # Aplicación Dash
├── direct-marketing-campaigns.csv # Dataset base
├── README.md # Este archivo
└── requirements.txt # Dependencias


## 🚀 Requisitos de instalación

1. Asegúrate de tener Python 3.8 o superior.

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows
Instala las dependencias:

touch requirements.txt

pip install -r requirements.txt
Si no tienes un archivo requirements.txt, puedes generarlo con:
pip freeze > requirements.txt

▶️ Ejecutar el dashboard
bash
Copy
Edit
python marketing_dashboard.py
Luego abre tu navegador en: http://127.0.0.1:8050


## 📸 Vista previa

!Vista del Dashboard (dashboard.png)




👤 Autor
José Jose Alejandro Rubio
Proyecto desarrollado para prueba técnica.
Contacto: alejandro.rub.men@gmail.com
