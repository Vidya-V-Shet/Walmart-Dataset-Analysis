from dash import dcc, html
import src.ids as ids

def render() -> html.Div:
    all_identifiers = ["Correlation Matrix on Weekly basis", "Correlation Matrix on Monthly basis", "External Factors distributions"]
    return html.Div(
        children=[
            html.H5("Choose a plot", style={"color": '#FFAA00'}),
            dcc.RadioItems(
                id=ids.FOURTH_TAB_RADIO_ITEMS,
                 options=[{"label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}), "value": identifier}
                          for identifier in all_identifiers],
                value="Correlation Matrix on Weekly basis"
            ),
        ]
    )