from dash import Dash
from layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Walmart Project"
    app.layout = create_layout(app)
    app.run()

if __name__ == "__main__":
    main()