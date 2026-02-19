import os

user = input("Enter your username: ")
action = input("Proceed with build? (yes/no): ").lower()

if action == "yes":
    status = f"User {user} approved the build."
else:
    status = f"User {user} cancelled the build."

with open("status.txt", "w") as f:
    f.write(status)

print(f"Update: {status}")
print("File 'status.txt' has been updated.")