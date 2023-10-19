# Walmart Sales Forecasting 🛍️

![Walmart Image](Wallmart1.jpg)

**Description:** As one of the leading retail giants in the US, Walmart aims to accurately predict sales and demand. Events and holidays can affect daily sales. With 45 Walmart stores' sales data at hand, the challenge is dealing with unforeseen demands and stockouts due to less-than-optimal machine learning models. An ideal model should account for economic indicators like the CPI and Unemployment Index.

Prominent holidays like the Super Bowl, Labour Day, Thanksgiving, and Christmas affect sales. In the evaluation, holiday weeks are given 5x weightage. Part of this challenge is factoring in the effects of promotional markdown events, especially during these holiday weeks, despite incomplete historical data.

**Acknowledgements:** The dataset originates from [Kaggle](https://www.kaggle.com/).

## 🎯 Objective:
1. Understand and clean the dataset if needed.
2. Build Regression models for sales prediction considering single & multiple features.
3. Evaluate models using metrics like R2, RMSE, etc.

## 🚀 Project Phases:
1. EDA and statistical analysis
2. Time Series Predictive modeling
3. Cross-sectional Predictive modeling

📩 **Contact:** [medoxz543@gmail.com](mailto:medoxz543@gmail.com)

**Dashboard Sample:** ![Dashboard Image](dashboard_example.png)

---

# Insights:

## 📊 Walmart Store Insights

### Comparative Analysis:

| Features         | Supercenter                                              | Discount Store                                | Neighborhood Market                               |
|------------------|----------------------------------------------------------|------------------------------------------------|--------------------------------------------------|
| **Founded In**   | 1988                                                     | 1962                                           | 1998                                               |
| **Size**         | 182,000 sq ft                                            | 106,000 sq ft                                  | 38,000 sq ft                                       |
| **Key Products** | Grocery, electronics, apparel, home decor, fresh produce | Electronics, apparel, home decor, health/beauty| Pharmacy, groceries, fresh produce, dairy, bakery |
| **Unique Features**| 24/7 ops; Potential for banks, salons, etc.           | Spacious, well-lit ambiance                   | -                                                  |

_[Source](https://corporate.walmart.com/about)_

From analyzing the sizes of the stores, I concluded that
- 🅰️ Supercenter
- 🅱️ Discount Store
- 🅲️ Neighborhood Market

### Deep Dive Insights:
- 🌟 Dept 72 peaks during holidays; Dept 92 leads during non-holidays.
- For 🅱️, Dept 38 dominates non-holiday sales.
- 🅲️: Dept 92 is the holiday sales leader.
- 📉 Dept 78 consistently records the lowest sales.

### Store Performance:
- 🌟 Top Stores: 20, 4, 14, 10, 2, 13.
- Super Bowl Stars: Stores 20, 4
- Labor Day Stars: Stores 14, 20
- 📉 Lowest sales from Stores 33 & 5.

## 📊 Walmart Store Types Insights:
<h5> 🏪 Store Type Distribution

- **Type A Stores**: 💼 
    - Composition: 51.2% 
    - Average Weekly Sales Contribution: 48%

- **Type B Stores**: 🎒 
    - Composition: 38.7% 
    - Average Weekly Sales Contribution: 29.3%

- **Type C Stores**: 📦 
    - Composition: 10.1%
    - Average Weekly Sales Contribution: 22.7%
    - Type C, with 23% sales, sees a dip to 17% on Thanksgiving. However, this performance is still significant compared to the 10.1% of other store types.

## 📊 Walmart Time Series Insights:
- **Seasonal Trends**:
  - Types A & B experience noticeable sales spikes in November and December, unlike Type C.
  - Sales drop for Types A and B in January due to prior heavy spending during the holidays. Sales rebound in February due to events like Groundhog Day, Valentine's Day, etc. The trend also reflects in October as customers anticipate holiday deals in November and December.
- **Promotions & Sales**:
  - At a glance, markdowns may seem ineffectual or even counterproductive. However, deeper statistical analyses reveal that markdowns do provide a modest boost to sales.
- **Economic Events Influence**:
  - Other factors, such as the 2012 US presidential election, the Great Recession from 2008 to 2012, and the real estate crisis, affected sales. While sales marginally increased, they were effective given these unprecedented challenges.
- **Difference in Means (With Markdowns - Without Markdowns**):
  - Temperature     1.535219
  - Fuel_Price      0.160912
  - CPI             4.436657
  - Unemployment   -0.745140

## 📊 Regression Analysis: Economic Factors vs. Weekly Sales 🛒

| Predictor        | Without Markdowns | With Markdowns | Difference |
|------------------|:-----------------:|:--------------:|:----------:|
| **Intercept**    | 33,390            | 30,990         | -2,400     |
| **Type[B]**      | -7,881.85         | -8,096.13      | -214.28    |
| **Type[C]**      | -10,800           | -10,810        | -10        |
| **IsHoliday**    | 821.67            | 1,479.77       | +658.10    |
| **Temperature**  | 32.76             | 11.68          | -21.08     |
| **Fuel_Price**   | -2,214.07         | -1,206.98      | +1,007.09  |
| **CPI**          | -32.74            | -27.65         | +5.09      |
| **Unemployment** | -231.28           | -280.45        | -49.17     |

---

## 📝 Key Observations

1. **🛍️ Store Types' Impact**: 
   - **Type A** serves as our benchmark.
   - **Type B** stores, during the non-markdown period, showed higher average sales than Type A. However, the advantage they had slightly reduced when markdowns were introduced.
   - **Type C** stores stand out. They are fewer but significantly efficient in terms of sales, consistently outperforming Type A.

2. **🎉 IsHoliday Influence**: The holiday effect is unmissable. Sales are higher during holidays, and the effect becomes even more pronounced during markdown periods, suggesting that holiday shoppers are particularly sensitive to price reductions.

3. **🌡️ Temperature's Role**: Temperature had a discernible influence on sales without markdowns. However, its effect waned during markdowns, indicating that the allure of discounts might overshadow shopping preferences influenced by weather.

4. **⛽ Fuel_Price's Impact**: The adverse effect of fuel prices on sales is clear. However, the markdowns appear to have offset some of this negativity, possibly suggesting that consumers were willing to travel to stores despite higher fuel costs if they expected to find good deals.

5. **📉 Unemployment and Sales**: Unemployment usually deters sales. The more pronounced decline in sales with increasing unemployment during markdowns could indicate that the discounting strategy might not be as effective during high unemployment periods.

6. **🛒 CPI's Influence**: As general price levels (CPI) rise, sales tend to drop. However, the markdowns provided a buffer against this trend, underscoring the importance of pricing strategies in countering broader economic pressures.

---

# Cluster Analysis Report for Store Departments 📊

## Introduction 🚀

This report presents an analysis of store data segmented into 4 clusters. The primary metrics used for segmentation include Weekly Sales, Temperature, Fuel Price, CPI, Unemployment rates, and Total Markdowns. Additionally, we analyze the distribution of departments and stores within these clusters.

## Overall Cluster Statistics 📈

| Cluster | Weekly Sales         | Temperature | Fuel Price | CPI          | Unemployment | Total Markdown |
|---------|----------------------|-------------|------------|--------------|--------------|----------------|
| 0       | 565,701.40           | 60.67       | 3.84       | 141.57       | 8.94         | 19,519.14      |
| 1       | 3,725,462.00         | 59.87       | 3.64       | 176.67       | 7.03         | 25,563.22      |
| 2       | 482,855.60           | 49.16       | 3.61       | 166.08       | 6.35         | 19,325.06      |
| 3       | 486,091.40           | 68.01       | 3.49       | 221.11       | 6.73         | 15,247.30      |

## Department Distribution Across Clusters 🛒

### Cluster 0:
- 📌 Departments: 80/81 (majority of departments)
- 📌 Stores: 17/45

### Cluster 1:
- 📌 Departments: 28/81 (focused set of departments, suggesting specialized stores or niche markets)
- 📌 Stores: 34/45 (majority of stores)

### Cluster 2:
- 📌 Departments: 80/81 (majority of departments, similar to Cluster 0)
- 📌 Stores: 31/45 

### Cluster 3:
- 📌 Departments: 77/81 (almost similar to Cluster 0 & 2)
- 📌 Stores: 23/45 

## Comparative Analysis 🕵️

### 1. **Department Diversity and Store Specialization:**
- **Clusters 0 and 2** showcase vast department representation, indicative of general or hypermarket stores. Such stores usually cater to diverse product categories and aim to be a one-stop solution.
  
- **Cluster 1**, with its concentrated departmental coverage, could represent niche markets or specialty stores. Despite the limited product range, this strategy is implemented in a majority of the stores.

### 2. **Economic Indicators and Store Performance:**
- **Cluster 3** operates in areas with the highest CPI, suggesting reduced purchasing power for consumers. Nevertheless, it also boasts the lowest unemployment rate. This could infer that these stores are in economically growing areas with a relatively higher cost of living.
  
- **Cluster 0** presents a unique situation with the lowest CPI but one of the highest unemployment rates. This scenario might indicate that even though products are more affordable, fewer individuals have the means to purchase.
  
- **Cluster 1** represents a balanced economic state with moderate values for both CPI and unemployment, possibly hinting at stable economic areas.

### 3. **Sales Dynamics and Revenue Trends:**
- **Cluster 2** demonstrates sales figures similar to clusters 0 and 3 despite offering a broad range of products. This suggests that variety doesn't always lead to higher sales.
  
- **Cluster 1** excels in sales, further solidifying the idea that a specialized product range coupled with widespread store coverage can drive better revenue.

### 4. **Environmental Factors and Sales:**
- **Cluster 0 and Cluster 1** operate under similar average temperatures. This might suggest stores in similar geographical regions but with differing strategies.
  
- **Cluster 3** stands out with stores operating under the warmest conditions, which could influence their product offerings.

### 5. **Promotional Activities and Sales:**
- **Cluster 1** reports the highest markdowns, aligning with its high sales, suggesting effective promotional strategies. In contrast, **Cluster 3**, despite having the least markdowns, does not lag far behind in sales, hinting at other factors driving its revenue.