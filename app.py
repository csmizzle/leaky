from layout import layout
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=['https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/flatly/bootstrap.min.css'],
    meta_tags=[
        {'name': 'viewport',
         'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}
    ],
)

app.layout = dbc.Container(layout, fluid=True)
app.title = "Facebook Leaked Dash"
server = app.server

if __name__ == "__main__":
    app.run_server()
