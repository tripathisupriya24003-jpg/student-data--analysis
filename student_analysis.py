import pandas as pd

# Sample data
data = {
    "Name": ["Aman", "Riya", "Sita", "Rahul"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Add Grade column
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(get_grade)

# Average marks
avg = df["Marks"].mean()
print("Average Marks:", avg)

# Top student
top_student = df[df["Marks"] == df["Marks"].max()]
print("\nTop Student:\n", top_student)

# Students above average
above_avg = df[df["Marks"] > avg]
print("\nStudents Above Average:\n", above_avg)
