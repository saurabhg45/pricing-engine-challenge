import pandas as pd

# Load the CSV files
products_df = pd.read_csv('/mnt/data/products.csv')
sales_df = pd.read_csv('/mnt/data/sales.csv')

# Merge the dataframes on SKU
merged_df = pd.merge(products_df, sales_df, on='sku', how='left')
merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)

# Apply pricing rules
def apply_pricing_rules(row):
    old_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = old_price

    # Rule 1: Low Stock, High Demand
    if stock < 20 and quantity_sold > 30:
        new_price = old_price * 1.15
    # Rule 2: Dead Stock
    elif stock > 200 and quantity_sold == 0:
        new_price = old_price * 0.7
    # Rule 3: Overstocked Inventory
    elif stock > 100 and quantity_sold < 20:
        new_price = old_price * 0.9

    # Rule 4: Minimum Profit Constraint
    min_price = cost_price * 1.2
    if new_price < min_price:
        new_price = min_price

    # Final rounding
    return round(old_price, 2), round(new_price, 2)

# Apply rules to each row
merged_df[['old_price', 'new_price']] = merged_df.apply(
    lambda row: pd.Series(apply_pricing_rules(row)), axis=1
)

# Add currency units (INR assumed)
merged_df['old_price'] = merged_df['old_price'].apply(lambda x: f"{x:.2f} INR")
merged_df['new_price'] = merged_df['new_price'].apply(lambda x: f"{x:.2f} INR")

# Create the output DataFrame
output_df = merged_df[['sku', 'old_price', 'new_price']]
output_path = '/mnt/data/updated_prices.csv'
output_df.to_csv(output_path, index=False)

output_path
