import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone", "Headphones"],
    "Price": [50000, 500, 1200, 12000, 20000, 1500],
    "Quantity": [5, 50, 30, 10, 8, 25],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Pune"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Sales Data Analysis")
print(df)

# Total Sales
df["Total Sales"] = df["Price"] * df["Quantity"]

# Highest Total Sales
Highest_Total_Sales = df["Total Sales"].max()
print("\nHighest Total Sales:", Highest_Total_Sales)

# Most Expensive Product
Most_Expensive = df.loc[df["Price"].idxmax()]
print("\nMost Expensive Product")
print(Most_Expensive)

# Highest Selling Product
Highest_Product = df.loc[df["Total Sales"].idxmax()]
print("\nHighest Selling Product")
print(Highest_Product)

# City Wise Total Sales
City_Sales = df.groupby("City")["Total Sales"].sum()
print("\nCity Wise Total Sales")
print(City_Sales)

# Percentage Contribution
Total_Sales = df["Total Sales"].sum()
df["Percentage Contribution"] = (
    df["Total Sales"] / Total_Sales
) * 100

print("\nPercentage Contribution")
print(df[["Product", "Percentage Contribution"]])

# Sort by Total Sales
df = df.sort_values("Total Sales", ascending=False)

print("\nSorted Data")
print(df)

# Product Wise Sales Graph
plt.bar(df["Product"], df["Total Sales"])
plt.title("Sales Data Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# City Wise Sales Graph
plt.bar(City_Sales.index, City_Sales.values)
plt.title("City Wise Sales Data Analysis")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()