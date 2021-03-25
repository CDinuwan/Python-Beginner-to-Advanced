name = " "

if not name.strip():
    print("Name is empty")

age = 22
if 18 >= age < 65:
    print("Eligible")
else:
    print("Not eligible")

message = "Eligible" if age >= 18 else "Not Eligible"

# 18 <= age < 65
