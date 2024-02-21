csvReport = [
    "Emp1,1000.00,Dep1",
    "Emp2,2000.00,Dep2",
    "Emp3,3000.00,Dep1",
    "Emp4,4000.00,Dep4",
    "Emp5,5000.00,Dep3",
]

# find total salary of each department
departmentSalary = {}
for record in csvReport:
    tokens = record.split(",")
    salary = float(tokens[1])
    department = tokens[2]
    if department in departmentSalary:
        departmentSalary[department] += salary
    else:
        departmentSalary[department] = salary

for department, salary in departmentSalary.items():
    print(department, salary)