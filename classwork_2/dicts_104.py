employees_infos = {
    "Misha 1": {
        "age": 14,
        "experience": "Expert"
    },
    "Iva": {
        "age": 14,
        "experience": "Boss"
    },
    "Marius": {
        "age": 25,
        "experience": "Intern"
    },
    "Misha 2": {
        "age": 62,
        "experience": "Super Boss"
    },
}

for employee in employees_infos:
    # employee is the key of the dict (example Iva)
    experience = employees_infos[employee]["age"]
    print(f"Age of {employee} is {experience}")
