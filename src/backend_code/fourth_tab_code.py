import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def first_graph(df: pd.DataFrame, basis: str = "month"):
    # Group by 'month' and compute the mean for each variable
    aggregated_data = df.groupby(basis).agg({
        'Weekly_Sales': 'mean',
        'Fuel_Price': 'mean',
        'Unemployment': 'mean',
        'CPI': 'mean',
        "Temperature": "mean"
    }).reset_index()

    # Calculate the correlation matrix for the change values
    correlation_matrix = aggregated_data[['Weekly_Sales', 'Fuel_Price', 'Unemployment', 'CPI', "Temperature"]].corr("spearman")

    # Create a heatmap to visualize the correlation matrix
    fig = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=list(correlation_matrix.columns),
        y=list(correlation_matrix.index),
        annotation_text=correlation_matrix.round(2).values,
        showscale=True,
        colorscale='Viridis'
    )
    if basis == "month":
        basis_text = "Monthly"
    elif basis == "Date":
        basis_text = "Weekly"

    fig.update_layout(title=f"Correlation Heatmap of {basis_text} Values", autosize=True, template="plotly_dark")

    return fig

def second_graph(df):
    fig = make_subplots(rows=1, cols=4)
    external_factors = ["CPI", "Fuel_Price", "Unemployment", "Temperature"]
    names = ["CPI", "Fuel_Price", "Unemployment", "Temperature"]
    
    colors = ["#FF6B6B", "#4ECDC4", "#FFD166", "#95E1D3"]

    for col_num, (factor, name, color) in enumerate(zip(external_factors, names, colors), start=1):
        fig.add_trace(go.Box(y=df[factor], name=name, marker_color=color), 1, col_num)

    
    fig.update_layout(title="External Factors", autosize=True, template="plotly_dark")
    
    axes_kwargs = {"showgrid": True, "gridwidth": 1, "gridcolor": "Gray"}
    fig.update_xaxes(**axes_kwargs)
    fig.update_yaxes(**axes_kwargs)

    return fig

def prepare_visuals_for_dashboard(df, selector):
    if selector == "Correlation Matrix on Weekly basis":
        return first_graph(df, "Date")
    elif selector == "Correlation Matrix on Monthly basis":
        return first_graph(df, "month")
    elif selector == "External Factors distributions":
        return second_graph(df)