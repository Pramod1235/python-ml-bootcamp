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

df = pd.DataFrame(data)
print(df)

employee_names = pd.Series(df['Employee'])
print(employee_names)
employee_salaries = pd.Series(df['Salary'])
print(employee_salaries)

employee_id = [1,2,3,4,5,6,7,8,9,10,11,12]


df1 = pd.DataFrame(data , index=employee_id)
print(df1)

print(df1.iloc[2,::])

print(df1.iloc[4]["Salary"])

print(df1.shape)

print(df1.info())

print(df1["Salary"].mean())