from dash import Dash
from src.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP

app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
server = app.server
app.title = "Walmart Project"
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run_server()