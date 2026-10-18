# Capstone - Global Economic Indicators Analytics


## Problem statement
How can education, healthcare, labor participation, and renewable energy be leveraged to increase GDP per capita, while understanding the global economic, social, and environmental patterns that drive differences in development across countries?

## Research Objectives
**1.Assess the Role of Education in Economic Growth**

Objective: Evaluate how literacy rate (%) and education expenditure as % of GDP influence GDP per capita across countries.
 
**2. Measure the Impact of Healthcare on Development Outcomes**

Objective: Analyze how healthcare expenditure per capita and doctor-to-patient ratio correlate with life expectancy and GDP per capita.

**3. Examine Labor Force Participation and Productivity**

Objective: Investigate how labor force participation rate (%) and unemployment rate (%) affect GDP per capita across different economies.

5. Evaluate Renewable Energy Adoption and Sustainable Growth

Objective: Determine how renewable energy share (%) in total energy consumption relates to GDP per capita and CO₂ emissions.

6. Identify key global development patterns that explains differences in GDP per capita

Objective: Use descriptive analytics to identify key global development patterns that explain differences in GDP per capita across countries.



## Data Quality & Cleaning Notes



# Electronics Retail Sales Dataset 📊

<p align="center">
 <img width="266" height="205" alt="image_1e16842e_edited" src="https://github.com/user-attachments/assets/699034ae-2410-4f06-ae9d-66dd5003594f" />
</p>

<h1 align="center">Electronics Retail Sales Dataset</h1>

This repository contains a transactional dataset capturing retail sales performance for consumer electronics products throughout the first half of **2026**. The data includes granular details on order parameters, product categories, geographic regions, salesperson mapping, and promotional discounts.

It serves as an excellent resource for exploratory data analysis (EDA), sales performance forecasting, regional market analysis, and missing data imputation practice.

<img width="1317" height="742" alt="image" src="https://github.com/user-attachments/assets/fd2d0b2f-b7d0-4953-8c8b-868132c2485a" />

## 📋 Dataset Overview

* **File Name:** `product_sales_practice.csv`
* **Time Horizon:** January 2026 – June 2026
* **Target Category:** Electronics
* **Key Entities:** Products, Sales Team, Regional Markets, Revenue Metrics

  Link to Jupyter Notebook in Google Colab:
  https://colab.research.google.com/drive/1zdPR2ig9qFp6Q1gPrZvky3Ac7UITW3Mv?usp=sharing
   
## 🗂️ Data Dictionary

The dataset consists of the following 10 features:

| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| **Order_ID** | String | A unique alphanumeric identifier for each transaction. | `ORD078` |
| **Date** | Date | The transaction date formatted as `YYYY-MM-DD`. | `2026-04-09` |
| **Product** | String | The name of the electronic item sold. | `Laptop`, `Mouse`, `Webcam` |
| **Category** | String | The high-level category classification. | `Electronics` |
| **Region** | String | The geographic sales territory. | `North`, `East`, `West`, `South` |
| **Salesperson** | String | The name of the account representative. | `Alice`, `Bob`, `Charlie`, `Diana`, `Ethan` |
| **Quantity** | Integer | The total units purchased in the order. | `7.0` |
| **Unit_Price** | Float | The retail price per single unit of the product. | `997.67` |
| **Discount** | Float | The promotional deduction percentage applied (0.0 to 0.15). | `0.15` (equivalent to 15%) |
| **Sales** | Float | The final calculated gross revenue earned from the order. | `6983.69` |

## 🔍 Data Quality & Cleaning Notes

If you are using this dataset for data cleaning projects, please note that it intentionally contains realistic real-world data anomalies:
* **Missing Values (NaNs):** Features like `Region`, `Salesperson`, `Unit_Price`, `Discount`, and `Sales` contain scattered missing fields (e.g., missing revenue values or unattributed regional boundaries).
* **Calculated Columns:** The `Sales` column follows the general formula:  
  \[\text{Sales} = (\text{Quantity} \times \text{Unit\_Price}) \times (1 - \text{Discount})\]
  This relationship can be exploited to programmatically restore missing metrics.
* **Empty Rows:** The raw structure contains blank structural divider rows (`,,,,,,,,,`) that should be filtered out during preprocessing.

## 🛠️ Usage Example (Python & Pandas)

Get started analyzing this dataset quickly using Python:

```python
import pandas as pd

# Load the dataset and drop completely empty structural lines
df = pd.read_csv('sales_data.csv').dropna(how='all')

# Convert date column to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Quick view of total sales revenue by product
revenue_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("Revenue by Product:\n", revenue_by_product)
```

## 💡 Potential Projects & Analysis Directions
1. **Sales Performance Dashboards:** Create interactive Tableau or Power BI visualizations mapping regional performance by salesperson.
2. **Predictive Modeling:** Build machine learning regression models to predict expected order values or customer quantity demands.
3. **Discount Impact Studies:** Assess whether offering a $10\%$ vs $15\%$ discount yields a statistically significant increase in total items sold.
