students = {"Aarav": 85, "Priya": 92, "Rohan": 78, "Sneha": 95, "Vikram": 88, "Anjali": 80, "Kunal": 76, "Deepika": 90}
name = input("Enter student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")