from backend_code.first_tab_code import select_and_prepare_dashboard_barcharts
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import ids
from backend_code.data_loader import *


def render(app: Dash) -> html.Div:
    # Add controls to build the interaction
    @app.callback(
        Output(component_id=ids.BAR_CHART, component_property="figure"),
        Input(component_id=ids.IDENTIFIER_RADIO_ITEMS, component_property='value'),
        Input(component_id=ids.SELECTOR_DROPDONW, component_property='value')
    )
    
    def update_chart(identifier: str, select_type:str):
        return select_and_prepare_dashboard_barcharts(load_data(), identifier, select_type)

    
    return dcc.Graph(id=ids.BAR_CHART)
