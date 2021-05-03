from datetime import datetime


def new_user():
    print("\nREGISTER NOW! FILL IN YOUR DETAILS.")
    first_name = input("Whats your first name? ")
    lastName = input("Whats your last name? ")
    Username = input("What would you like your username to be? ")
    Password = input("Create password ")
    Confirm_password = input("Re-enter password ")
    print("Your account number will be automatically generated!")
    if Password == Confirm_password:
        name_details = {"firstName": first_name, "lastName": lastName,
                        "Username": Username, "password":
                            Password, "AccountNo": generateAccountNo()}
        print(name_details)
        confirmation = input("Confirm Details yes or no?")
        if confirmation == "yes":
            with open("moduleNames.txt", "a") as txt:
                txt.write(str(name_details) + '\n')
            print("Your details has being saved")
            login()
        else:
            new_user()
    else:
        print("Password doesnt match!\n".upper())
        new_user()


def generateAccountNo():
    from random import shuffle
    digits = [str(num) for num in range(10)]
    shuffle(digits)
    account_number = "".join(digits)
    return account_number


def login():
    print("\nSIGN IN \nNOTE USERNAME AND PASSWORD ARE CASE SENSITIVE!!!")
    username = input("Enter Username: ")
    password = input("Enter password: ")
    with open("moduleNames.txt") as file:
        finder = []
        content = file.readlines()
        for i in range(len(content)):
            if username in content[i] and password in content[i]:
                finder.append("True")
            else:
                finder.append("False")
        if "True" in finder:
            print(f"\nWelcome, {username.upper()}")
            MenuOptions()
        else:
            print("Details not found. Invalid username or password.\n")
            response = input("Do you want to try again? yes or no ")
            if response == "yes":
                login()
            else:
                new_user()


def register():
    existing_user = input("Are you a new user (yes or no)? ")
    if existing_user.lower() == "yes":
        new_user()
    else:
        login()


def generateTimeAndDate():
    time, date = datetime.now().strftime("%H:%M:%S"), datetime.now().date()
    print(f"Todays' time is {time}\nTodays' date is {date}\n")


def MenuOptions():
    print("Please Select an option below\n-Option 1\n-Option 2\n-Complains\n")
    user_response = input("Enter Option? ")
    if user_response.lower() == "option 1":
        print(f"Take your cash.")
    elif user_response.lower() == "option 2":
        user_response3 = input("How much would you like to deposit? ")
        print(f"Current balance is: {user_response3}.")
    elif user_response.lower() == "complains":
        user_response4 = input("What issue will you like to report? ")
        print(f"Thank you for contacting us '{user_response4}' will be reviewed.")
    else:
        print("Read The Options Again, Thanks.")
        MenuOptions()


generateTimeAndDate()
register()
