from dash import dcc, html
import ids

def render() -> html.Div:
    all_identifiers = ["All Types", "A", "B", "C"]
    
    return html.Div(
        children=[
            html.H5("Store Type", id=ids.FIRST_TAB_H5),
            dcc.Dropdown(
                id=ids.SELECTOR_DROPDOWN,
                options=[{
                        "label": html.Span([identifier], style={'color': '#1E88E5', 'font-size': 18}),
                        "value": identifier
                    } for identifier in all_identifiers],
                value="All Types",
                clearable=False,
                searchable=False,
            ),
        ]
    )
