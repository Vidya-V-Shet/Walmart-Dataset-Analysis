from backend_code.first_tab_code import select_and_prepare_dashboard_barcharts
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import ids
from backend_code.data_loader import *


def render(app: Dash) -> html.Div:
    # Add controls to build the interaction
    @app.callback(
        Output(component_id=ids.BAR_CHART, component_property="figure"),
        Output(component_id=ids.SELECTOR_DROPDOWN, component_property='style'),
        Output(component_id=ids.FIRST_TAB_H5, component_property='style'),
        Input(component_id=ids.IDENTIFIER_RADIO_ITEMS, component_property='value'),
        Input(component_id=ids.SELECTOR_DROPDOWN, component_property='value')
    )
    
    def update_chart(identifier: str, select_type: str):
        # Your existing code for chart update
        figure = select_and_prepare_dashboard_barcharts(load_data(), identifier, select_type)
        
        # Modify this line to update dropdown visibility based on the condition
        dropdown_style = {'width': '180px', 'background-color': '#343a40', 'color': '#1E88E5'}
        h5_style = {"color": '#FFAA00'}

        if identifier in ["Dept Sales: Holiday vs Non-Holiday", "Top 5 Departments", "Bottom 5 Departments"]:
            dropdown_style['display'] = 'none' 
            h5_style['display'] = 'none' 

        return figure, dropdown_style, h5_style
    
    return dcc.Graph(id=ids.BAR_CHART)
