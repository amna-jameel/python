# Q3. Highest and lowest price
# Find the highest and lowest price with a loop. Don’t use max() or min().
# Expected: Highest: 1200, Lowest: 75

prices = [450, 1200, 300, 980, 75]
high = prices[0]
low = prices[0]
for price in prices:
    if price>high:
        high=price
    if  price<low:
        low=price
print(f"Highest= {high} and Lowest= {low}")
