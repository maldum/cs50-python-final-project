from pyfiglet import Figlet
import pwinput
import csv
import re
import datetime
from PIL import Image, ImageFont, ImageDraw
import sys


def main():
    intro_msg()
    user_select = validate_user_input(input(">> "))
    if user_select == "1":
        new_customer()
    elif user_select == "2":
        existed_customer()
    elif user_select == "3":
        sys.exit("Thank You.")


def intro_msg():
    f = Figlet(font="doom")
    print(
        "----------------------------------------------------------------------------\n"
    )
    print(f.renderText("ATM Card Printer"))
    print(
        "----------------------------------------------------------------------------\n"
    )
    print("Please Select from the below list:\n")
    print("1. New Customer.")
    print("2. Existed Customer.")
    print("3. Quit")


def validate_user_input(n):
    if re.fullmatch(r"[1-3]{1}", n):
        return n
    else:
        sys.exit("Please input a valid option 1, 2 or 3")


def new_customer():
    name = input("Your Name: ")
    pin = validate_pin(pwinput.pwinput(prompt="Create 4-digit pin: "))

    with open("customers.csv") as file:
        row_count = sum(1 for row in file) + 100

    with open("customers.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "pin"])
        writer.writerow({"id": row_count, "name": name, "pin": pin})
    print(
        f"Thank you for registering with us {name}\nThis is you ID number >>> {row_count}"
    )


def existed_customer():
    customers = {}
    with open("customers.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers[row["id"]] = [row["name"], row["pin"]]
    id_input = input("Please enter you ID number: ")
    if id_input in customers:
        pin = pwinput.pwinput(prompt="Enter 4-digit pin: ")
    else:
        sys.exit("Invalid ID number")

    if customers[id_input][1] == pin:
        print(f"\nWelcome back {customers[id_input][0]}!\n")
    else:
        sys.exit("Invalid pin")

    print_atm(customers[id_input][0])


def validate_pin(n):
    if re.fullmatch(r"[1-9]{1}[0-9]{3}", n):
        return n
    else:
        sys.exit(
            "Invalid pin:\n + Enter only 4 digit numbers\n + dont start with number 0"
        )


def print_atm(name):
    print("Select from the colors below to print your new ATM card\n")
    print("1. Green\n2. Red\n3. Blue")
    user_color = input(">> ")
    while user_color not in ["1", "2", "3"]:
        print("Please input valid option 1, 2 or 3")
        user_color = input()

    if user_color == "1":
        img = Image.open("green.jpg")
    elif user_color == "2":
        img = Image.open("red.jpg")
    elif user_color == "3":
        img = Image.open("blue.jpg")
    date = datetime.datetime.now()
    year = str(date.year + 3)
    month = str(date.month)
    expire = f"EXPIRE 0{month}/{year[-2:]}"
    font = ImageFont.truetype("averia-serif-libre.regular.ttf", 24)
    font1 = ImageFont.truetype("averia-serif-libre.regular.ttf", 14)
    draw = ImageDraw.Draw(img)
    draw.text((10, 200), name, (0, 0, 0), font=font)
    draw.text((320, 150), expire, (0, 0, 0), font=font1)
    img.save("card.jpg")
    print("Your new ATM card is ready, check 'card.png'\nThank you.")


if __name__ == "__main__":
    main()
