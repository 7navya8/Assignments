# Assignment for today - 7th Feb 2026

# Create a strong code for password authentication using python. 
correct_password = "Python123"
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)
if attempts == 0:
    print("Account locked")
