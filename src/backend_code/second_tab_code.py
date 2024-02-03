import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from src.backend_code.constants import DATES
from typing import Dict

colors = {
    "A": "#26C6DA",
    "B": "#D4E157",
    "C": "#FF8A65"
}

def prepare_data(dataframe, filter_column=None, filter_value=None):
    if filter_column and filter_value is not None:
        dataframe = dataframe[dataframe[filter_column] == filter_value]
    return dataframe.groupby("Type")["Weekly_Sales"].mean().sort_values(ascending=False).to_frame()

def aggregate_sales_by_holiday(df):
    return {
        holiday: df[df['Date'].isin(date_list)].groupby("Type")["Weekly_Sales"].mean().sort_values(ascending=False).to_frame()
        for holiday, date_list in DATES.items()
    }


# Visualization function
def visualize_pie_charts(dataframe: pd.DataFrame, *aggregated_data: Dict[str, pd.DataFrame], subplot_titles: list=[]) -> go.Figure:
    num_charts = len(aggregated_data) + 1
    labels = ["A", "B", "C"]

    fig = make_subplots(rows=1, cols=num_charts, specs=[[{'type': 'domain'}]*num_charts], subplot_titles=subplot_titles)

    # Add store type count pie chart
    fig.add_trace(go.Pie(labels=labels, values=dataframe["Type"].value_counts(), marker=dict(colors=[colors[key] for key in labels])), 1, 1)
    
    # Add the rest of the data
    for index, data_dict in enumerate(aggregated_data, start=2):
        trace_kwargs = {"labels": labels, "values": data_dict["data"]["Weekly_Sales"], "marker": dict(colors=[colors[key] for key in labels])}
        fig.add_trace(go.Pie(**trace_kwargs), 1, index)
    
    fig.update_layout(autosize=True, template="plotly_dark")
    
    return fig


def prepare_data_for_stores_count_vs_sales(df):
    return [{"data": prepare_data(df)}]

def prepare_data_for_stores_count_vs_sales_holiday(df):
    return [
        {"data": prepare_data(df, "IsHoliday", True)},
        {"data": prepare_data(df, "IsHoliday", False)}
    ]

def prepare_data_for_stores_count_vs_sales_across_holidays(df):
    data_by_type = aggregate_sales_by_holiday(df=df)
    return [
        {"data": data_by_type['super_bowl']},
        {"data": data_by_type['labor_day']},
        {"data": data_by_type['thanksgiving']},
        {"data": data_by_type['christmas']}
    ]

def box_plot(df: pd.DataFrame):
    fig = px.box(df, x="Type", y="Size")
    fig.update_layout(yaxis_title="Type Footprint (sq ft)", autosize=True, template="plotly_dark")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    return fig


SELECTOR_MAP = {
    "Stores Count vs Sales": {
        "func": prepare_data_for_stores_count_vs_sales,
        "titles": ['Stores by Type: Count', 'AVG Weekly Sales by Type']
    },
    "Stores Count vs Sales [Holidays & Non-holidays]": {
        "func": prepare_data_for_stores_count_vs_sales_holiday,
        "titles": ['Stores by Type: Count', 'AVG Weekly Sales by Type: holidays', 'AVG Weekly Sales by Type: Non-Holidays']
    },
    "Stores Count vs Sales [Across Holidays]": {
        "func": prepare_data_for_stores_count_vs_sales_across_holidays,
        "titles": ['Stores by Type: Count', 'Super Bowl Sales: Type', 'Labor Day Sales: Type', 'Thanksgiving Sales: Type', 'Christmas Sales: Type']
    }
}


def prepare_pie_charts_for_dashboard(df: pd.DataFrame, selector: str):
    
    if selector == "Types' sizes comparison":
        return box_plot(df)
    else:
        if selector not in SELECTOR_MAP:
            raise ValueError(f"Invalid selector: {selector}")
        data_args = SELECTOR_MAP[selector]["func"](df)
        subplot_titles = SELECTOR_MAP[selector]["titles"]

        fig = visualize_pie_charts(df, *data_args, subplot_titles=subplot_titles)
        return fig
