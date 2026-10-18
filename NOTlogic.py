is_banned = input("Are you banned from the system? (yes/no): ").lower()
if not is_banned == "yes":
    print("You may access the system.")
else:
    print("Access denied due to ban.")