###### NOW WE WILL CREATE A DASHBOARD FOR THE DATA------

pip install dash
pip install pyngrok

from pyngrok import ngrok
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Set your ngrok authentication token
ngrok.set_auth_token("YOUR NGROK TOKEN")

# Sample DataFrame (replace this with your cleaned data)
data = {
    'City': ['City A', 'City B', 'City C', 'City D'],
    'Delivery Time': [30, 45, 20, 35],
    'Order Count': [100, 200, 150, 120]
}
df = pd.DataFrame(data)

# Create a simple bar chart
fig = px.bar(df, x='City', y='Delivery Time', title="Delivery Time by City")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Food Delivery Dashboard"),
    html.Div(children="This is a simple dashboard using Plotly and Dash."),

    # Graph section
    dcc.Graph(
        id='delivery-time-bar',
        figure=fig
    ),
])

# Open a ngrok tunnel to the Dash app
public_url = ngrok.connect(8050)
print('Dash app is live at:', public_url)

# Run the app
app.run(debug=True, use_reloader=False)
