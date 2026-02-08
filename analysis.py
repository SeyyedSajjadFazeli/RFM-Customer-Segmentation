import sqlite3
import pandas as pd
import numpy as np

# 1. SETUP & DATA LOADING
# Load the dataset (Assuming you downloaded 'online_retail_II.csv' from Kaggle)
# For demonstration, we load a subset or the full file
print("Loading Data...")
df = pd.read_csv('online_retail_II.csv')

# Clean Data: Remove null Customer IDs and negative quantities
df = df.dropna(subset=['Customer ID'])
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 2. SQL INTEGRATION (Simulating a Real Database)
# We dump the dataframe into a local SQLite database to show SQL skills
conn = sqlite3.connect('ecommerce.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Data loaded into SQL Database successfully.")

# 3. SQL QUERY FOR AGGREGATION
# We use SQL to calculate Recency, Frequency, and Monetary value per customer
# This is much more efficient than pure Pandas for large datasets in production
query = """
SELECT 
    "Customer ID" as customer_id,
    MAX(InvoiceDate) as last_purchase_date,
    COUNT(DISTINCT Invoice) as frequency,
    SUM(Quantity * Price) as monetary
FROM transactions
GROUP BY "Customer ID"
"""

rfm_df = pd.read_sql(query, conn)
conn.close()

# 4. PANDAS & NUMPY FOR ANALYTICS
# Calculate Recency (Days since last purchase)
# Note: In a real scenario, use today's date. Here we use the max date in data + 1 day
max_date = pd.to_datetime(df['InvoiceDate']).max() + pd.Timedelta(days=1)
rfm_df['last_purchase_date'] = pd.to_datetime(rfm_df['last_purchase_date'])
rfm_df['recency'] = (max_date - rfm_df['last_purchase_date']).dt.days

# Use NumPy/Pandas qcut to score customers (1 to 5)
labels = range(1, 6)
rfm_df['R_Score'] = pd.qcut(rfm_df['recency'], q=5, labels=list(reversed(labels))) # Lower recency is better
rfm_df['F_Score'] = pd.qcut(rfm_df['frequency'].rank(method='first'), q=5, labels=labels)
rfm_df['M_Score'] = pd.qcut(rfm_df['monetary'], q=5, labels=labels)

# Create a combined segment score
rfm_df['RFM_Segment'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)
rfm_df['RFM_Score'] = rfm_df[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

# Define Customer Segments based on Score using NumPy select (Vectorized operation)
conditions = [
    (rfm_df['RFM_Score'] >= 13),
    (rfm_df['RFM_Score'] >= 9),
    (rfm_df['RFM_Score'] >= 5)
]
choices = ['Top Customer', 'Loyal Customer', 'Needs Attention']
rfm_df['Customer_Type'] = np.select(conditions, choices, default='At Risk')

# 5. EXPORT RESULTS
print(rfm_df.head())
rfm_df.to_csv('rfm_analysis_result.csv', index=False)
print("Analysis Complete. Results saved.")