Roles = ["Doctor", "Nurse"]
role = input("Enter your role:").strip().capitalize()
if role in Roles:
   print(" Access granted")
else:
   print("Access denied")
   