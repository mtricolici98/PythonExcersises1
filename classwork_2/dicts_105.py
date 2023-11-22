employees_infos = {
    "Misha 1": {
        "age": 14,
        "experience": "Expert",
        "salary": 10000,
    },
    "Iva": {
        "age": 14,
        "experience": "Boss",
        "salary": 5000,
    },
    "Marius": {
        "age": 25,
        "experience": "Intern",
        "salary": 100,
    },
    "Misha 2": {
        "age": 62,
        "experience": "Super Boss",
        "salary": 10000,
    },
}

total_money_to_be_paid = 0
for employee in employees_infos:
    # employee is the key of the dict (example Iva)
    salary = employees_infos[employee]["salary"]
    total_money_to_be_paid += salary
    print(f"Salary of {employee} is {salary}")

print(f"In total, the company should pay {total_money_to_be_paid} in salaries.")
tax = total_money_to_be_paid * 0.20
print(f"Tax to be paid is {tax}")
print(f"In total, the comapny will pay {total_money_to_be_paid + tax}")
