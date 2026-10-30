
# STUDENT PERFORMANCE ANALYSIS

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Read CSV File
df = pd.read_csv("student_perf.csv")

# 3. Display First Five Records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display Dataset Information
print("\nDATASET INFORMATION:")
print(df.info())

# 4. Calculate Average, Maximum and Minimum G3
print("\nMarks ANALYSIS:")
print("Average Marks:", df["G3"].mean())
print("Maximum Marks:", df["G3"].max())
print("Minimum Marks:", df["G3"].min())

# 5. Identify Students Scoring More Than 75 G3
print("\nSTUDENTS SCORING MORE THAN 75:")
print(df[df["G3"] > 75])

# 6. Bar Chart - G3 Obtained by Each Student
plt.figure(figsize=(8, 5))
plt.bar(df["G3"], df["G3"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Histogram - Distribution of G3
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.show()

# 8. Scatter Plot - Study Hours vs G3
plt.figure(figsize=(8, 5))
plt.scatter(df["studytime"], df["G3"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs G3")
plt.show()

print("\nSTUDENT PERFORMANCE ANALYSIS COMPLETED!")
