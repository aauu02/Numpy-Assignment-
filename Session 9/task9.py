import numpy as np

# 1. Create prices array
prices = np.array([299, 499, 799, 0, 1599, -1, 899], dtype=float)

print("Original prices:", prices)
print("Data type:", prices.dtype)

# 2. Clean invalid prices
positive_prices = prices[prices > 0]
average_price = np.mean(positive_prices)

prices[prices <= 0] = average_price

print("\nAverage positive price:", average_price)
print("Cleaned prices:", prices)

# 3. Calculate item bills
quantities = np.array([2, 1, 3, 4, 2, 1, 5])
item_bills = prices * quantities

print("\nItem bills:", item_bills)

# 4. Summary report
print("\n--- Summary Report ---")
print("Minimum price:", np.min(prices))
print("Maximum price:", np.max(prices))
print("Average price:", np.mean(prices))
print("Total of prices:", np.sum(prices))
print("Total bill:", np.sum(item_bills))

# 5. Unique prices
unique_prices = np.unique(prices)

print("\nUnique prices:", unique_prices)
print("Number of unique prices:", len(unique_prices))
