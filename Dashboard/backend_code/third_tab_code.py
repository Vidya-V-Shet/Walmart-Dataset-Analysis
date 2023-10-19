import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
from plotly.subplots import make_subplots


def first_graph(df):
    data = df.groupby(["Date", "Type"])["Weekly_Sales"].mean().reset_index()
    # Create the area plot
    fig = px.area(data, x="Date", y="Weekly_Sales", color="Type", facet_col="Type", title="Weekly Sales by Store Type Over Time",
                   color_discrete_sequence=['#E056FD', '#4ECDC4', '#F7DC6F'] # Electric Purple, Vibrant Turquoise, Bright Gold
)
    fig.update_layout(autosize=True, template="plotly_dark")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    return fig

def second_graph(df):
    # Group by Date and sum up each markdown and sales
    df_grouped = df.groupby('Date').agg({
        'MarkDown1': 'mean',
        'MarkDown2': 'mean',
        'MarkDown3': 'mean',
        'MarkDown4': 'mean',
        'MarkDown5': 'mean',
        'Weekly_Sales': 'mean'
    }).reset_index()

    # Create a line chart
    fig = go.Figure()

    # Add traces for each markdown
    markdowns_list = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
    for markdown in markdowns_list:
        fig.add_trace(go.Scatter(x=df_grouped['Date'], y=df_grouped[markdown], mode='lines', name=markdown))

    # Add trace for sales
    fig.add_trace(go.Scatter(x=df_grouped['Date'], y=df_grouped['Weekly_Sales'], mode='lines+markers', name='Weekly Sales', line=dict(width=2)))

    # Add layout details
    fig.update_layout(title='Markdowns & Weekly Sales Over Time',
                    xaxis_title='Date',
                    yaxis_title='Value',
                    hovermode='closest',
                    autosize=True,
                    template="plotly_dark")
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    return fig

def third_graph(df):
    df = df.groupby("Date")["Weekly_Sales"].mean().reset_index()
    result = seasonal_decompose(df['Weekly_Sales'].dropna(), model='additive', period=4)

    y_s = [result.observed, result.trend, result.seasonal, result.resid]
    names = ['Observed', 'Trend', 'Seasonal', 'Residual']

    fig = make_subplots(rows=4, cols=1, shared_xaxes=True)

    for row_num, (y, name) in enumerate(zip(y_s, names), start=1):
        fig.add_trace(go.Scatter(x=df['Date'], y=y, mode='lines', name=name), row_num, 1)

    fig.update_layout(title='Weekly sales decomposition', autosize=True, template="plotly_dark")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    return fig

def prepare_visuals_for_dashboard(df, selector: str):
    if selector == "Time-Series Sales Comparison: Store Type":
        return first_graph(df)
    elif selector == "Time-Series Sales with markdowns":
        return second_graph(df)
    elif selector == "Weekly sales decomposition":
        return third_graph(df)