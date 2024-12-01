import pandas as pd

# Paths to input files
orders_file = "retail-superstore-analysis/orders.csv"
returns_file = "retail-superstore-analysis/returns.csv"
people_file = "retail-superstore-analysis/people.csv"

# Step 1: Load datasets
orders_df = pd.read_csv(orders_file)
returns_df = pd.read_csv(returns_file)
people_df = pd.read_csv(people_file)

# Step 2: Standardize column names
orders_df.columns = orders_df.columns.str.lower().str.replace(' ', '_')
returns_df.columns = returns_df.columns.str.lower().str.replace(' ', '_')
people_df.columns = people_df.columns.str.lower().str.replace(' ', '_')

# Step 3: Ensure 'returned' column exists
if 'returned' not in returns_df.columns:
    returns_df['returned'] = 'Yes'

# Step 4: Add calculated fields
# Add Profit Margin
orders_df['profit_margin'] = (orders_df['profit'] / orders_df['sales']).round(2)

# Merge Returns Data
orders_df = orders_df.merge(returns_df[['order_id', 'returned']], on='order_id', how='left')
orders_df['returned'] = orders_df['returned'].fillna('No')

# Extract and format time-based features
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
orders_df['ship_date'] = pd.to_datetime(orders_df['ship_date'])
orders_df['order_year'] = orders_df['order_date'].dt.year
orders_df['order_month'] = orders_df['order_date'].dt.month
orders_df['order_quarter'] = orders_df['order_date'].dt.quarter

# Ensure consistent date format
orders_df['order_date'] = orders_df['order_date'].dt.strftime('%Y-%m-%d')
orders_df['ship_date'] = orders_df['ship_date'].dt.strftime('%Y-%m-%d')

# Step 5: Remove duplicate rows
orders_df = orders_df.drop_duplicates()

# Step 6: Save the cleaned dataset
cleaned_file = "retail-superstore-analysis/cleaned_data.csv"
orders_df.to_csv(cleaned_file, index=False)

print(f"\nCleaned data saved to: {cleaned_file}")