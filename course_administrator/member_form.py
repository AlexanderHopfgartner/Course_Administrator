from logic.validator import *
from consts import INPUT_END


def member_form() -> dict:
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
    form = {
        "telnum": None,
        "email": None,
        "url": None,
        "f_name": None,
        "name": None,
        "role": None,
        "address": {
            "address_name": None,
            "number": None,
            "postcode": None,
            "city": None
        }
    }
    while form["f_name"] is None and form["name"] is None and form["role"] is None:

        while form["f_name"] is None:
            f_name = input(f"Please Enter first name.{INPUT_END}")
            if validate_name(f_name):
                form["f_name"] = f_name

        while form["name"] is None:
            name = input(f"Please Enter name.{INPUT_END}")
            if validate_name(name):
                form["name"] = name

        while form["role"] is None:
            ###########################################  hilfe  ######################################################
            role = input(f"Please Enter Role.\n"
                         f"['Ter' = Teilnehmer:in/ {'TXX'} = {'das weiß ich nicht mehr'}/ {'XXX'} ="
                         f" {'keine ahnung'}]{INPUT_END}")
            print(role[0:4])
            if role[0:4] == "Ter":
                if input(f"Is Teilnehmer:in right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = "Teilnehmer:in"
                    continue
            if role[0:4] == "Ler":
                if input(f"Is Lektor:in right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = "Lektor:in"
                    continue
            if role[0:4] == "Tur":
                if input(f"Is Tutor:in right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = "Tutor:in"
                    continue
            print("Sorry not a role in the list.")

        while form["address"]["address_name"] is None and form["address"]["number"] is None and\
                form["address"]["postcode"] is None and form["address"]["city"] is None:

            while form["address"]["address_name"] is None:
                address_name = input(f"Please Enter name of the street{INPUT_END}")
                if validate_address_name(address_name):
                    form["address"]["address_name"] = address_name

            while form["address"]["number"] is None:
                street_number = input(f"Please Enter street number{INPUT_END}")
                if validate_street_number(street_number):
                    form["address"]["number"] = street_number

            while form["address"]["postcode"] is None:
                postcode = input(f"Please Enter postcode{INPUT_END}")
                if validate_postcode(postcode):
                    form["address"]["postcode"] = int(postcode)

            while form["address"]["city"] is None:
                city = input(f"Please Enter city name{INPUT_END}")
                if validate_city(city):
                    form["address"]["city"] = city

        if form["telnum"] is None:
            number = input(f"Please Enter your Phonenumber (OPTIONAL) ['number'/'no']{INPUT_END}")
            if number[0].lower() == "n":
                form["telnum"] = False
            else:
                form["telnum"] = validate_telnum(number)

        if form["email"] is None:
            email = input(f"Please Enter your email (OPTIONAL) ['email'/'no']{INPUT_END}")
            if email[0].lower() == "n":
                form["email"] = False
            else:
                form["email"] = validate_email(email)

        if form["url"] is None:
            url = input(f"Please Enter your URL (OPTIONAL) ['URL'/'no']{INPUT_END}")
            if url[0].lower() == "n":
                form["url"] = False
            else:
                form["url"] = validate_url(url)

    return form
