# CS50 Python Final Project
[Link Text](https://cs50.harvard.edu/python/2022/)

# ATM Card Printer Kiosk
#### Project Link: https://cs50.harvard.edu/python/2022/project/
#### Video Demo:  https://youtu.be/ONiEzxWovBw
#### Description:

This is an ATM printer kiosk where you can print a new ATM card by providing your ID and a 4-digit code number.

Intro_msg():
When you approach the kiosk, you will be welcomed with an introductory message created using the figlet library. After that, you will be prompted with three choices:
1- New customer
2- Existing customer
3- Quit (using sys.exit)

Validate_user_input():
The system will validate the user's input of choices using the regex method. If the user doesn't enter 1, 2, or 3, the system will raise an error and exit.

New_customer():
If you choose to be a new customer, this function will be called, and you will be asked to enter your name and a 4-digit pin code to sign up for the service. The system will raise an error if you input an invalid 4-digit code. I used regex to validate the rule of the 4-digit code:

* It must be a 4-digit number
* It should not start with the number 0

An ID will be generated and provided to you after a successful sign-up, so you can use the service in the future. Rather than building a database system, every successful sign-up will save the credentials to a CSV file with the field names "id, name, pin".

Existed_customer():
This function will validate if you are an existing customer or not by retrieving the "customers.csv" file to check your credentials by calling the function "validate_pin(n)" after you enter your ID and the 4-digit code.

Print_atm(name):
After you successfully enter your info, you will be asked to choose from three different colors for your ATM card. After you pick your favorite color, a new ATM card will be printed for you.
