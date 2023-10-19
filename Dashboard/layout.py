from dash import Dash, html, dcc
import graph_elements.first_tab_graph as first_tab_graph
import graph_elements.second_tab_graph as second_tab_graph
import graph_elements.third_tab_graph as third_tab_graph
import graph_elements.fourth_tab_graph as fourth_tab_graph


import user_choices.first_tab_dropdown as first_tab_dropdown

import user_choices.first_tab_radio_items as first_tab_radio_items
import user_choices.second_tab_radio_items as second_tab_radio_items
import user_choices.third_tab_radio_items as third_tab_radio_items
import user_choices.fourth_tab_radio_items as fourth_tab_radio_items


def first_tab(app: Dash) -> html.Div:
    return html.Div(
        className="container-fluid",
        children=[
            html.Div(
                className="row", 
                children=[
                    html.Div(
                        first_tab_radio_items.render(),
                        className="col-md-2 mb-2 align-items-center d-flex align-self-center mt-5",
                    ),
                    html.Div(
                        first_tab_dropdown.render(),
                        className="col-md-2 mb-1 align-items-center d-flex align-self-center mt-5",
                    ),
                    html.Div(
                        first_tab_graph.render(app),
                        className="col-md-8 flex-column mt-5",
                    ),
                ],
            ),
        ],
    )

def second_tab(app) -> html.Div:
    return html.Div(
        className="container-fluid",
        children=[
            html.Div(
                className="row", 
                children=[
                    html.Div(
                        second_tab_radio_items.render(),
                        className="col-md-2 mb-2 align-items-center d-flex align-self-center mt-5",
                    ),
                    html.Div(
                        second_tab_graph.render(app),
                        className="col-md-10 flex-column mt-5",
                    ),
                ],
            ),
        ],
    )


def third_tab(app) -> html.Div:
    return html.Div(
        className="container-fluid",
        children=[
            html.Div(
                className="row", 
                children=[
                    html.Div(
                        third_tab_radio_items.render(),
                        className="col-md-2 mb-2 align-items-center d-flex align-self-center mt-5",
                    )                    ,
                    html.Div(
                        third_tab_graph.render(app),
                        className="col-md-10 flex-column mt-5",
                    ),
                ],
            ),
        ],
    )
def fourth_tab(app):
    return html.Div(
        className="container-fluid",
        children=[
            html.Div(
                className="row", 
                children=[
                    html.Div(
                        fourth_tab_radio_items.render(),
                        className="col-md-2 mb-2 align-items-center d-flex align-self-center mt-5",
                    )                    ,
                    html.Div(
                        fourth_tab_graph.render(app),
                        className="col-md-10 flex-column mt-5",
                    ),
                ],
            ),
        ],
    )



def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="min-vh-100 bg-dark text-white",
        children=[
            html.Div(
                children=[html.H1(app.title, className="text-lg-center")]
                ),
            html.Hr(),
            dcc.Tabs(id="tabs", className="text-black", children=[
                dcc.Tab(label='Dept & Store', children=[first_tab(app)]),
                dcc.Tab(label='Types in depth', children=[second_tab(app)]),
                dcc.Tab(label='Time Series', children=[third_tab(app)]),
                dcc.Tab(label='External Factors', children=[fourth_tab(app)])]
            ),
        ]
    )
