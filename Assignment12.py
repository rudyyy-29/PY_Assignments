
# CUSTOMER CHURN - EXPLORATORY DATA ANALYSIS (EDA)

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 2. Load Dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print("FIRST FIVE ROWS:")
print(df.head())

# 3. Dataset Information
print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nDATASET INFORMATION:")
df.info()

# 4. Statistical Summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe(include="all"))

# 5. Check Missing Values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Visualize Missing Values
plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Dataset")
plt.show()

# 6. Check Duplicate Records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# 7. Data Cleaning
# Remove unnecessary customer ID column if present
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric if present
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

# Replace infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill missing numeric values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

# 8. Churn Distribution
if "Churn" in df.columns:
    print("\nCHURN DISTRIBUTION:")
    print(df["Churn"].value_counts())

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Churn")
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.show()

# 9. Numerical Feature Distribution
numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols].hist(figsize=(12, 8), bins=20)
plt.suptitle("Distribution of Numerical Features")
plt.tight_layout()
plt.show()

# 10. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()

# 11. Churn Based on Contract Type
if "Contract" in df.columns and "Churn" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Contract", hue="Churn")
    plt.title("Churn Based on Contract Type")
    plt.xticks(rotation=20)
    plt.show()

# 12. Churn Based on Internet Service
if "InternetService" in df.columns and "Churn" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="InternetService", hue="Churn")
    plt.title("Churn Based on Internet Service")
    plt.show()

# 13. Monthly Charges vs Churn
if "MonthlyCharges" in df.columns and "Churn" in df.columns:
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
    plt.title("Monthly Charges vs Customer Churn")
    plt.show()

# 14. Tenure vs Churn
if "tenure" in df.columns and "Churn" in df.columns:
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="Churn", y="tenure")
    plt.title("Customer Tenure vs Churn")
    plt.show()

# 15. Calculate Churn Percentage
if "Churn" in df.columns:
    churn_percentage = (
        df["Churn"].value_counts(normalize=True) * 100
    )

    print("\nCHURN PERCENTAGE:")
    print(churn_percentage)

# 16. Final Cleaned Dataset
print("\nFINAL DATASET SHAPE:")
print(df.shape)

print("\nFINAL DATASET:")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nEDA COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as cleaned_customer_churn.csv")
