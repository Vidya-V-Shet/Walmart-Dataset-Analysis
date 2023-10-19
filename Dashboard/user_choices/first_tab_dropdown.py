from dash import dcc, html
import ids

def render() -> html.Div:
    all_identifiers = ["All Types", "A", "B", "C"]
    return html.Div(
        children=[
            html.H5("Store Type", style={"color": '#FFAA00'}),
            dcc.Dropdown(
                id=ids.SELECTOR_DROPDONW,
                options=[{
                        "label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}),
                        "value": identifier
                    } for identifier in all_identifiers],
                value="All Types",
                style={'width': '180px', 'background-color': '#343a40', 'color': '#1E88E5'},
                clearable=False,
                searchable=False
            ),
        ]
    )
