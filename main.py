print("Are you human?")

response = input("Please type 'y' for yes and 'n' for no: \n")

if response.lower() in ['yes', 'y']:
    print("Welcome, human!")
else:
    print("Access denied. Only humans are allowed.")