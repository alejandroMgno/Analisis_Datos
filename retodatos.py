import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv("./direct-marketing-campaigns - bank-direct-marketing-campaigns.csv")
df.columns = df.columns.str.lower()

# Métrica 1: Tasa de contacto efectivo
total_contactos = len(df)
contactos_exito = len(df[df['poutcome'] == 'success'])
tasa_contacto_efectivo = round((contactos_exito / total_contactos) * 100, 2)

# Métrica 2: Tasa de éxito por analista
tasa_exito_analista = df.groupby('nr.employed')['poutcome'].apply(lambda x: round((x == 'success').sum() / len(x) * 100, 2))

# Métrica 3: Conversión de clientes contactados previamente
clientes_previos = df[df['previous'] > 0]
conversion_previos = round((len(clientes_previos[clientes_previos['poutcome'] == 'success']) / len(clientes_previos)) * 100, 2)

# Métrica 4: Éxito por cantidad de intentos previos
exito_por_previous = df.groupby('previous')['poutcome'].apply(lambda x: round((x == 'success').sum() / len(x) * 100, 2)).reset_index()
exito_por_previous.columns = ['previous', 'tasa_exito']

# Métrica 5: Relación préstamo activo vs éxito
con_prestamo = df[df['loan'] == 'yes']
relacion_prestamo_exito = round((len(con_prestamo[con_prestamo['poutcome'] == 'success']) / len(con_prestamo)) * 100, 2)

# Gráfico 1: Tasa de contacto efectivo
fig1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=tasa_contacto_efectivo,
    number={'suffix': "%"},
    title={'text': "Tasa de Contacto Efectivo"},
    gauge={'axis': {'range': [0, 100]}}
))

# Gráfico 2: Tasa de éxito por analista
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

# Gráfico 3: Conversión de clientes contactados previamente
fig3 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=conversion_previos,
    number={'suffix': "%"},
    title={'text': "Conversión Clientes Contactados Previamente"},
    gauge={'axis': {'range': [0, 100]}}
))

# Gráfico 4: Éxito por cantidad de intentos previos
fig4 = px.bar(
    exito_por_previous,
    x='previous',
    y='tasa_exito',
    labels={'previous': 'Intentos Previos', 'tasa_exito': 'Tasa de Éxito (%)'},
    title='Tasa de Éxito por Cantidad de Intentos Previos',
    text='tasa_exito'
)
fig4.update_traces(texttemplate='%{text}%', textposition='outside')
fig4.update_layout(yaxis_title="Tasa de Éxito (%)")

# Gráfico 5: Relación préstamo activo vs éxito
fig5 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=relacion_prestamo_exito,
    number={'suffix': "%"},
    title={'text': "Relación Préstamo Activo vs Éxito"},
    gauge={'axis': {'range': [0, 100]}}
))

tasa_exito_analista_tabla = tasa_exito_analista.reset_index()
tasa_exito_analista_tabla.columns = ['id_analista', 'tasa_exito']
tasa_exito_analista_tabla['tasa_exito'] = (tasa_exito_analista_tabla['tasa_exito']).round(2).astype(str) + '%'

# Tabla de tasa de éxito por analista
fig_tabla = go.Figure(data=[go.Table(
    header=dict(values=["ID Analista", "Tasa de Éxito"],
                fill_color='lightblue',
                align='center'),
    cells=dict(values=[
        tasa_exito_analista_tabla['id_analista'],
        tasa_exito_analista_tabla['tasa_exito']
    ],
        fill_color='lavender',
        align='center'))
])

fig_tabla.update_layout(title='Tasa de Éxito por Analista (en %)')
fig_tabla.show()

# Mostrar todos los gráficos
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
