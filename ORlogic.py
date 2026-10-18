has_student_id = input("Do you have a student ID? (yes/no): ").lower()
has_library_card = input("Do you have a library card? (yes/no): ").lower()

if has_student_id == "yes" or has_library_card == "yes":
    print("You may enter the library.")
else:
    print("Access denied. You need a student ID or library card.")