gpa = float(input("Enter your GPA: "))
volunteer_hours = int(input("Enter your volunteer hours: "))
leadership = input("Do you hold a leadership role? (yes/no): ").lower()

if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"):
    print("You qualify for the scholarship.")
else:
    print("You do not qualify for the scholarship.")