# CS50P_Project
# ATM Card Printer Kiosk
#### Project Link: https://cs50.harvard.edu/python/2022/project/
#### Video Demo:  https://youtu.be/ONiEzxWovBw
#### Description:

    An ATM printer kios you can print your new ATM card
    by providing your ID and 4-digit code numbers

    intro_msg():

    you will be welcomed by an intro message using figlet libray
    than 3 choices will promot:
    1. New customer
    2. Existed customer
    3. Quit (using sys.exit)

    validate_user_input():

    Validate the user input of choices by using regex method. if the user didnt enter 1, 2 or 3 the system will raise an error and exit

    new_customer():

    if you choose a new customer this function will be called and you will asked to enter your name and 4-digit pin code
    to sign up for this service.
    The system will raise an error if input an invalid 4-digit code, I used regex to validate the rule of the 4-digit code:
    + must be 4 digit numbers
    + shoud not start with the number 0
    than an ID will generate and provided to you so you can use the service in the future.
    every successful sign up the system save the credentials to a csv file with filedsname "id, name, pin" rather than building a datebase system.

    existed_customer():

    This function will be validate if you are an existed customer or not by retrieving 'customers.csv' file to chedck your credentials by calling the function "validate_pin(n):"
    after you enter your ID and the 4-digit code.

    print_atm(name):

    After you enter your info successfully, you will asked to chooose 3 different colors for your ATM card
    after you pick your favourite color a new ATM card will be printed for you.
