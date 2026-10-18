# capstone

Data Quality & Cleaning Notes
If you are using this dataset for data cleaning projects, please note that it intentionally contains realistic real-world data anomalies:

Missing Values (NaNs): Features like Region, Salesperson, Unit_Price, Discount, and Sales contain scattered missing fields (e.g., missing revenue values or unattributed regional boundaries).
Calculated Columns: The Sales column follows the general formula:
[\text{Sales} = (\text{Quantity} \times \text{Unit_Price}) \times (1 - \text{Discount})] This relationship can be exploited to programmatically restore missing metrics.
Empty Rows: The raw structure contains blank structural divider rows (,,,,,,,,,) that should be filtered out during preprocessing.
