from dash import dcc, html
import ids

def render() -> html.Div:
    all_identifiers = ["Dept Sales: Holiday vs Non-Holiday", "Top 5 Departments", "Bottom 5 Departments",
                       "Store Sales: Holiday vs Non-Holiday", "Top 5 Stores", "Bottom 5 Stores"]
    return html.Div(
        children=[
            html.H5("Choose a plot", style={"color": '#FFAA00'}),
            dcc.RadioItems(
                id=ids.IDENTIFIER_RADIO_ITEMS,
                 options=[{"label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}), "value": identifier}
                          for identifier in all_identifiers],
                value="Dept Sales: Holiday vs Non-Holiday"
            ),
        ]
    )