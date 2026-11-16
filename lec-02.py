import pandas as pd
data = {
    "Employee": [
        "Rahul", "Priya", "Arjun", "Sneha",
        "Rahul", "Kiran", "Meena", "Ravi",
        "Anil", "Priya", "Kavya", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT",
        "Sales", "HR", "Sales", "IT"
    ],
    "Age": [
        25, 28, 30, 26, 25, 29,
        None, 32, 27, 28, 31, 35
    ],
    "Salary": [
        45000, 38000, 65000, 42000,
        45000, 40000, 52000, None,
        35000, 38000, 58000, 90000
    ],
    "City": [
        "Hyderabad", "Mumbai", "Hyderabad",
        "Delhi", "Hyderabad", "Mumbai",
        "Delhi", None, "Pune", "Mumbai",
        "Pune", "Hyderabad"
    ],
    "Experience": [
        2, 4, 6, 3, 2, 5, 7, 8, 1, 4, 6, 10
    ]
}

#Display the first 5 employees.

df = pd.DataFrame(data)
print(df.head())

# Display the last 3 employees

print("Print last 3 records" , df.tail(3))

#Display complete information about the DataFrame.
print(df.info())

#Generate statistical summaries of numerical columns.
print(df.describe())

#Find all unique departments.
print(df["Department"].unique())

#Find the number of employees in each department.

print(df["Department"].value_counts())

print(df["Employee"] , df["Salary"] , df["Department"])

print(df[df["Salary"] > 50000])

print(df[df["City"] == "Hyderabad"])

df[ ( df["City"].isin(["Hyderabad", "Mumbai"])) & df["Salary"] >= 40000 ]

