import pandas as pd

# Load dataset
df = pd.read_csv("sales_location_data.csv")

print("===== GEOSPATIAL DATA ANALYSIS =====")
print(df.head())

# Dataset Information
print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Total Sales
total_sales = df["Sales"].sum()

# Average Sales
avg_sales = df["Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", round(avg_sales, 2))

# High Demand, Low Presence Areas
opportunities = df[
    (df["Demand"] == "High") &
    (df["Presence"] == "No")
]

print("\nPotential Expansion Regions:")
print(opportunities[["Region", "Sales", "Demand"]])

# Save Report
report = opportunities[["Region", "Sales", "Demand"]]

report.to_csv("geospatial_report.csv", index=False)

print("\nAnalysis Completed Successfully!")
print("Report saved as geospatial_report.csv")