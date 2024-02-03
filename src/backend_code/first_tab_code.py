import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.backend_code.constants import DATES, HOLIDAY_MAPPING, IDENTIFIER_MAP
from typing import Dict


def filter_and_rank_by_avg_sales(df: pd.DataFrame, mask, identifier:str="Dept", n: int=5, func=pd.DataFrame.head, select_type:str="All Types") -> pd.DataFrame:
    """
    identifier: can be Dept or Store
    select_type: can be All Types or A or B or C

    This function returns top 5/bottom 5 identifers based on select_type in terms of average weekly sales.

    For example, I want to get top 5 departments in Type A in terms of average weekly sales.
    """
    if select_type == "All Types":
        output_df = (df[mask]
                .groupby(identifier)["Weekly_Sales"]
                .mean()
                .sort_values(ascending=False))
        

    else:
        output_df = (df[(mask) & (df["Type"] == select_type)]
                .groupby(identifier)["Weekly_Sales"]
                .mean()
                .sort_values(ascending=False))
        
    output_df = func(output_df, n).reset_index()

    # Convert department identifiers to string (they are integers) to ensure they are treated as discrete categories when plotted, 
    # preventing them from being interpreted as continuous data on a number line.

    output_df[identifier] = output_df[identifier].astype(str)

    return output_df

def aggregate_sales_by_holiday_and_identifier(df, identifier: str, func, select_type: str) -> dict:
    return {
        holiday: filter_and_rank_by_avg_sales(df=df, mask=df['Date'].isin(date_list), identifier=identifier, func=func, select_type=select_type) 
        for holiday, date_list in DATES.items()
    }


def generate_holidays_sales_comparison(aggregated_data: Dict[str, pd.DataFrame], title: str) -> go.Figure:
    """
    This function return a figure which is subplots comparing between avg sales of the four holidays.
    """
    fig = make_subplots(rows=2, cols=2, subplot_titles=[info[0] for info in HOLIDAY_MAPPING.values()])
    
    for holiday_key, attrs in HOLIDAY_MAPPING.items():
        data = aggregated_data[holiday_key]
        holiday_name, color, row, col = attrs

        trace_kwargs = {"x": data.iloc[:, 0], "y": data["Weekly_Sales"], "marker_color": color, "name": holiday_name}

        fig.add_trace(go.Bar(**trace_kwargs), row=row, col=col)
    
    fig.update_layout(title=title, yaxis_title="Average Sales", autosize=True, template="plotly_dark")

    axes_kwargs = {"showgrid": True, "gridwidth": 1, "gridcolor": "Gray"}
    fig.update_xaxes(**axes_kwargs)
    fig.update_yaxes(**axes_kwargs)

    return fig


def assemble_holiday_vs_nonholiday_data(df, select_type, identifier, n=10, theme='dark'):
    assert identifier in ["Dept", "Store"], "Invalid identifier. Must be either 'Dept' or 'Store'."
    
    # Dark mode colors
    colors_dark = ['#FF6347', '#1E90FF']
    # Add more themes if needed
    themes = {'dark': colors_dark}
    
    if theme not in themes:
        raise ValueError("Invalid theme. Available themes are: " + ", ".join(themes.keys()))

    # print(df[holiday_mask])
    holiday_mask, non_holiday_mask = df["IsHoliday"], ~df["IsHoliday"]

    kwargs = {"df": df, "n": n, "identifier": identifier, "select_type": select_type}
    holiday_true_data = filter_and_rank_by_avg_sales(mask=holiday_mask, **kwargs)
    holiday_false_data = filter_and_rank_by_avg_sales(mask=non_holiday_mask, **kwargs)
    
    return holiday_true_data, holiday_false_data, themes[theme]


def generate_holiday_vs_nonholiday_subplot(holiday_data, non_holiday_data, identifier, theme) -> go.Figure:
    titles = ['Holiday Sales', 'Non-Holiday Sales']
    data = [holiday_data, non_holiday_data]

    fig = make_subplots(rows=1, cols=2, subplot_titles=titles)
    
    for i, (d, name) in enumerate(zip(data, titles)):
        trace_kwargs = {"x": d[identifier], "y": d["Weekly_Sales"], "marker_color": theme[i], "name": name}

        fig.add_trace(go.Bar(**trace_kwargs), row=1, col=i+1)
    
    layout_kwargs = {"yaxis_title": "Average Sales", "plot_bgcolor": "#333", "paper_bgcolor": "#333", "font": dict(color="white")}
    fig.update_layout(
        title=f"Sales Comparison based on {identifier}: Holiday vs Non-Holiday", **layout_kwargs
    )
    
    return fig


def select_and_prepare_dashboard_barcharts(df: pd.DataFrame, identifier: str, select_type: str) -> go.Figure:
    if identifier in ["Dept Sales: Holiday vs Non-Holiday", "Store Sales: Holiday vs Non-Holiday"]:
        key = IDENTIFIER_MAP[identifier]
        holiday_true_data, holiday_false_data, theme = assemble_holiday_vs_nonholiday_data(df=df, identifier=key, select_type=select_type)
        return generate_holiday_vs_nonholiday_subplot(holiday_true_data, holiday_false_data, key, theme)
    else:
        title, key, slice_func = IDENTIFIER_MAP[identifier]
        aggregated_data = aggregate_sales_by_holiday_and_identifier(df, key, slice_func, select_type)
        return generate_holidays_sales_comparison(aggregated_data, title)