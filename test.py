with open("documentation/checklist.txt", "r") as file:
    checklist = file.readlines()

script = "better_ac.py"
with open(script, "r") as file:
    car_code = file.readlines()

# print("ac.getCarState" in car_code[450])
# print(any("ac.getCarState" in line for line in car_code))

for func in checklist:
    pre_format = func
    func = func.strip()
    if func and not any(func in line for line in car_code):
        print(f"Function '{func}' is missing from {script}")
    else:
        checklist.remove(pre_format)

with open("documentation/checklist.txt", "w") as file:
    for func in checklist:
        file.write(func)