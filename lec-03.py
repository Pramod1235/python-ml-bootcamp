import pandas as pd
import numpy as np

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

#Add a new column called Bonus, calculated as 10% of salary.

df = pd.DataFrame(data)

df["Bonus"] = (df["Salary"] * 10 ) / 100

print(df)

df["Total_Compensation"] = (df["Salary"] + df["Bonus"])
print(df)

def assign_exp_lev(df):

    conditions = [
        df["Experience"] < 3,
        df["Experience"].between(3, 6),
        df["Experience"] > 6
    ]

    choices = ["Junior", "Mid-Level", "Senior"]

    df["Experience_Level"] = np.select(
        conditions,
        choices,
        default="Unknown"
    )

    return df

df = assign_exp_lev(df)

print(df)

df.loc[df["Employee"] == "Rahul", "Salary"] = 50000
