from backend_code.third_tab_code import prepare_visuals_for_dashboard
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import ids
from backend_code.data_loader import *


def render(app: Dash) -> html.Div:
    # Add controls to build the interaction
    @app.callback(
        Output(component_id=ids.THIRD_TAB_CHART, component_property="figure"),
        Input(component_id=ids.THIRD_TAB_RADIO_ITEMS, component_property='value'),
    )
    
    def update_chart(selector: str):
        return prepare_visuals_for_dashboard(load_data(), selector)

    
    return dcc.Graph(id=ids.THIRD_TAB_CHART)
