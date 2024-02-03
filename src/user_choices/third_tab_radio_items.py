from dash import dcc, html
import src.ids as ids


def render() -> html.Div:
    all_identifiers = ["Time-Series Sales Comparison: Store Type", "Time-Series Sales with markdowns", "Weekly sales decomposition", 
                       "Fuel Price", "CPI", "Temperature", "Unemployment"]
    return html.Div(
        children=[
            html.H5("Choose a plot", style={"color": '#FFAA00'}),
            dcc.RadioItems(
                id=ids.THIRD_TAB_RADIO_ITEMS,
                 options=[{"label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}), "value": identifier}
                          for identifier in all_identifiers],
                value="Time-Series Sales Comparison: Store Type"
            ),
        ]
    )
