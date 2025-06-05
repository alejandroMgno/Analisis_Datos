import dash
from dash import dcc, html, dash_table
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
tasa_exito_analista.columns = ['Analista', 'Tasa de Éxito (%)']

analista_top = tasa_exito_analista.sort_values('Tasa de Éxito (%)', ascending=False).iloc[0]
nombre_analista = analista_top['Analista']
tasa_analista = analista_top['Tasa de Éxito (%)']

fig_analista = px.bar(tasa_exito_analista, x='Analista', y='Tasa de Éxito (%)',
                      labels={'Tasa de Éxito (%)': 'Tasa de Éxito (%)', 'Analista': 'Analista'},
                      title='Tasa de Éxito por Analista',
                      color='Tasa de Éxito (%)', text='Tasa de Éxito (%)')
fig_analista.update_traces(textposition='outside')

clientes_previos = df[df['previous'] > 0]
conversion_previos = round(
    (len(clientes_previos[clientes_previos['poutcome'] == 'success']) / len(clientes_previos)) * 100, 2)

# App con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H1("📊 Dashboard de Campaña de Marketing", className="my-4 text-center"),

    dcc.Tabs([
        dcc.Tab(label="Resumen General", children=[
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

            dbc.Alert(
                f"🎉 ¡Felicidades al analista {nombre_analista} por tener la mayor tasa de éxito: {tasa_analista}%!",
                color="info",
                className="text-center mb-4"
            ),

            dbc.Row([
                dbc.Col([
                    html.H4("Tasa de Éxito por Analista"),
                    dcc.Graph(figure=fig_analista)
                ])
            ])
        ]),

        dcc.Tab(label="Tasa de Éxito por Analista", children=[
            dbc.Row([
                dbc.Col([
                    html.H4("Tabla de Tasa de Éxito por Analista"),
                    dash_table.DataTable(
                        data=tasa_exito_analista.to_dict('records'),
                        columns=[{'name': i, 'id': i} for i in tasa_exito_analista.columns],
                        style_table={'overflowX': 'auto'},
                        style_header={
                            'backgroundColor': 'rgb(30, 30, 30)',
                            'color': 'white',
                            'fontWeight': 'bold',
                            'textAlign': 'center'
                        },
                        style_data={
                            'backgroundColor': 'rgb(240, 240, 240)',
                            'color': 'black',
                            'textAlign': 'center'
                        },
                        page_size=20,
                    )
                ])
            ], className="mt-4")
        ])
    ])
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
