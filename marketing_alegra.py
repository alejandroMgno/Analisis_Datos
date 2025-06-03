import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Leer CSV
df = pd.read_csv("direct-marketing-campaigns - bank-direct-marketing-campaigns.csv")
df.columns = df.columns.str.lower()

# Métricas
total_contactos = len(df)
contactos_exito = len(df[df['poutcome'] == 'success'])
tasa_contacto_efectivo = round((contactos_exito / total_contactos) * 100, 2)

tasa_exito_analista = df.groupby('nr.employed')['poutcome'].apply(
    lambda x: round((x == 'success').sum() / len(x) * 100, 2)).reset_index()

analista_top = tasa_exito_analista.sort_values('poutcome', ascending=False).iloc[0]
nombre_analista = analista_top['nr.employed']
tasa_analista = analista_top['poutcome']

fig_analista = px.bar(tasa_exito_analista, x='nr.employed', y='poutcome',
                      labels={'poutcome': 'Tasa de Éxito (%)', 'nr.employed': 'Analista'},
                      title='Tasa de Éxito por Analista',
                      color='poutcome', text='poutcome')
fig_analista.update_traces(textposition='outside')

clientes_previos = df[df['previous'] > 0]
conversion_previos = round(
    (len(clientes_previos[clientes_previos['poutcome'] == 'success']) / len(clientes_previos)) * 100, 2)

# App con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout con estilo
app.layout = dbc.Container([
    html.H1("📊 Dashboard de Campaña de Marketing", className="my-4 text-center"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Tasa de Contacto Efectivo"),
            dbc.CardBody(html.H3(f"{tasa_contacto_efectivo}%", className="card-title text-success"))
        ]), width=4),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Conversión de Clientes Previos"),
            dbc.CardBody(html.H3(f"{conversion_previos}%", className="card-title text-primary"))
        ]), width=4),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Total de Contactos"),
            dbc.CardBody(html.H3(f"{total_contactos}", className="card-title"))
        ]), width=4)
    ], className="mb-4"),

    html.Div([
        dbc.Alert(
            f"🎉 ¡Felicidades al analista {nombre_analista} por tener la mayor tasa de éxito: {tasa_analista}%!",
            color="info",
            className="text-center"
        )
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.H4("Tasa de Éxito por Analista"),
            dcc.Graph(figure=fig_analista)
        ])
    ])
], fluid=True)


if __name__ == '__main__':
    app.run(debug=True)
