#importar librerias de analisis de datos
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

#cargar el archivo csv y normalizar los nombres de las columnas
df = pd.read_csv("./direct-marketing-campaigns - bank-direct-marketing-campaigns.csv")
df.columns = df.columns.str.lower()

#calcular la tasa de exito por analista
tasa_exito_analista = df.groupby('nr.employed')['poutcome'].apply(lambda x: round((x == 'success').sum() / len(x) * 100, 2))

#mostrar graficos de barras
fig2 = px.bar(
    tasa_exito_analista.reset_index(),
    x='nr.employed',
    y='poutcome',
    labels={'nr.employed': 'ID Analista', 'poutcome': 'Tasa de Éxito (%)'},
    title='Tasa de Éxito por Analista',
    text='poutcome'
)
fig2.update_traces(texttemplate='%{text}%', textposition='outside')
fig2.update_layout(yaxis_title="Tasa de Éxito (%)")
fig2.show()
