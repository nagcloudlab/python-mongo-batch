
csvReport=[
    "Emp1",1000.00,"Dep1",
    "Emp2",2000.00,"Dep2",
    "Emp3",3000.00,"Dep1",
    "Emp4",4000.00,"Dep4",
    "Emp5",5000.00,"Dep3",
]

# find total salary of each department 

depSal = {}
for i in range(0,len(csvReport),3):
    if csvReport[i+2] in depSal:
        depSal[csvReport[i+2]] += csvReport[i+1]
    else:
        depSal[csvReport[i+2]] = csvReport[i+1]
print(depSal)

