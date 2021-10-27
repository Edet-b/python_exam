from models import user_crud

db_path = "db_handler/users.json"

def init():
    print("\n*****************************WELCOME TO TECH MINDS*****************************\n")
    print("Enter 1 to register for participation")
    print("Enter 2 to exit")

    responses = input("Choose an option: ")
    try:
        if responses == "1":
            register()
        elif response == "2":
            print("Thanks for trying to register")
        else:
            print("\nInvalid response \nTry again")
            init()
    except NameError:
        print("\nAN ERROR OCCURED\n")
        init()

# pop up a message to give directions
def prompt(message, home_func, retry_func):
        response = input(message)
        if response == "1":
            retry_func()
        else:
            home_func()

# where the registaration of the participants  
def register():
    print("\nProvide the following details to create an account")
    name = input("Enter your full name\n")
    email = input("Enter your email\n")

    # trying to set a limit for the json file
    # if len(users) < 20:
    if name == "" or email == "":
                print("\nThese fields cannot be blank")
    else:
                user_details = {
                    "name":name,
                    "email":email,
                }
                response = user_crud.create_user(db_path,user_details)
    # elif len(users) == 20:
    #     return("\nApply next month\n No more space\n Thank you")
                if response == 1:
                    print("\nUser creation success")
                    print("\nYOUR ID IS: \n" + user_details['id'])
                    init()
                else:
                    print("\nUser with such email account already exist")
                    prompt("Enter 1 to retry \nEnter anything to go home", init, register)


init()

