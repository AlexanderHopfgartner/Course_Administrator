from logic.validator import *
from consts import INPUT_END, clear, Form, AddressForm


def fill_member_form() -> Form:
    """Return a form for Member:
    f_name: requite
    name: requite
    role: requite
    addres: requite
        address_name: requite
        address_number: requite
        postcode: requite
        city: requite
    telnum: optional
    email: optional
    url: optional"""
    f_name = ""
    name = ""
    address_name = ""
    number = ""
    postcode = ""
    city = ""
    telnum = ""
    email = ""
    url = ""

    while not validate_name(f_name):
        f_name = input(f"Please Enter first name.{INPUT_END}")
    while not validate_name(name):
        name = input(f"Please Enter sirname.{INPUT_END}")
    clear()

    role = get_role()
    clear()

    while not validate_address_name(address_name):
        address_name = input(f"Please enter name of the street.{INPUT_END}")
    while not validate_street_number(number):
        number = input(f"Please Enter street number{INPUT_END}")
    while not validate_postcode(postcode):
        postcode = input(f"Please Enter postcode{INPUT_END}")
    while not validate_city(city):
        city = input(f"Please Enter city name{INPUT_END}")
    clear()

    telnum = input(f"Please Enter your Phonenumber (OPTIONAL) ['number'/'no']{INPUT_END}")
    if telnum[0].lower() == "n":
        telnum = False
    else:
        telnum = validate_telnum(telnum)

    email = input(f"Please Enter your email (OPTIONAL) ['email'/'no']{INPUT_END}")
    if email[0].lower() == "n":
        email = False
    else:
        email = validate_email(email)

    url = input(f"Please Enter your URL (OPTIONAL) ['URL'/'no']{INPUT_END}")
    if url[0].lower() == "n":
        url = False
    else:
        url = validate_url(url)

    address, form = dict(), dict()
    for key in dir():
        value = eval(key)
        if key == "address_name" or key == "number" or key == "postcode" or key == "city":
            address[key] = value
        else:
            form[key] = value

    address, form = dict(), dict()

    for key in dir():
        if key == "form" or key == address:
            continue
        value = eval(key)
        if key == "address_name" or key == "number" or key == "postcode" or key == "city":
            address[key] = value
        else:
            form[key] = value
    formiii = Form(**form)
    print(formiii)
    return formiii


roles = ["Teilnehmer:in", "Lektor:in", "Tutor:in"]


def get_role():
    while True:
        role = input(f"Please Enter Role.\n"
                     f"{[role for role in roles]}{INPUT_END}")
        short_role = role[0:4]
        for index in range(len(role)):
            if short_role == "Tei" or short_role == "tei":
                if input(f"Is {roles[index]} right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    return roles[0]

            if short_role == "Lek" or short_role == "lek":
                if input(f"Is {roles[index]} right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    return roles[1]

            if short_role == "Tut" or short_role == "tut":
                if input(f"Is {roles[index]} right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    return roles[2]

        print("Sorry not a role in the list.")
