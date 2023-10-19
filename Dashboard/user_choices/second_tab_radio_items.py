from dash import dcc, html
import ids


def render() -> html.Div:
    all_identifiers = ["Types' sizes comparison", "Stores Count vs Sales", "Stores Count vs Sales [Holidays & Non-holidays]", "Stores Count vs Sales [Across Holidays]"]
    return html.Div(
        children=[
            html.H5("Choose a plot", style={"color": '#FFAA00'}),
            dcc.RadioItems(
                id=ids.PIE_CHARTS_SELECTOR,
                 options=[{"label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}), "value": identifier}
                          for identifier in all_identifiers],
                value="Types' sizes comparison"
            ),
        ]
    )
