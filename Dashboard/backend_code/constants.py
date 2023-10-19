import pandas as pd


# Dates related to holidays
DATES = {
    'super_bowl': ['2010-02-12', '2011-02-11', '2012-02-10'],
    'labor_day': ['2010-09-10', '2011-09-09', '2012-09-07'],
    'thanksgiving': ['2010-11-26', '2011-11-25'],
    'christmas': ['2010-12-31', '2011-12-30']
}

# Mapping of holidays to their respective attributes
HOLIDAY_MAPPING = {
    'super_bowl': ('Super Bowl', '#1E90FF', 1, 1),  # Dodger Blue
    'labor_day': ('Labor Day', '#FF6347', 1, 2),  # Tomato
    'thanksgiving': ('Thanksgiving', '#3CB371', 2, 1),  # Medium Sea Green
    'christmas': ('Christmas', '#D3D3D3', 2, 2)  # Light Gray (used in place of Black for visibility in dark mode)
}

# Mapping of identifiers to their respective attributes
IDENTIFIER_MAP = {
    "Top 5 Departments": ("Sales Comparison across different holidays based on Top 5 Departments", "Dept", pd.DataFrame.head),
    "Bottom 5 Departments": ("Sales Comparison across different holidays based on Bottom 5 Departments", "Dept", pd.DataFrame.tail),
    "Top 5 Stores": ("Sales Comparison across different holidays based on Top 5 Stores", "Store", pd.DataFrame.head),
    "Bottom 5 Stores": ("Sales Comparison across different holidays based on Bottom 5 Stores", "Store", pd.DataFrame.tail),
    "Dept Sales: Holiday vs Non-Holiday": "Dept",
    "Store Sales: Holiday vs Non-Holiday": "Store"
}
