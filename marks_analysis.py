import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Calculate total & average

df["Total"]=df[["Maths","Science","English"]].sum(axis=1)
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Find topper in each subject

topper_math = df.loc[df["Maths"].idxmax(), "Name"]
topper_science = df.loc[df["Science"].idxmax(), "Name"]
topper_english = df.loc[df["English"].idxmax(), "Name"]


# Print summary
print("=== Student Marks Analysis ===")
print(df)
print("\nToppers:")
print(f"Maths: {topper_math}")
print(f"Science: {topper_science}")
print(f"English: {topper_english}")

# Plot subject-wise average performance
df[["Maths", "Science", "English"]].mean().plot(
    kind="bar", title="Subject-wise Average Marks", color=["blue", "green", "orange"]
)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
