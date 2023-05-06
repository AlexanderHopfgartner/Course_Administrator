from consts import INPUT_END
from logic.validator import *


class Address(object):

    def __init__(self, *args, ):
        args = args[0]
        self.address_name = args[0]
        self.street_number = args[1]
        self.postcode = args[2]
        self.city = args[3]


# TODO 2.1.1 create CourseAdministrator
class Member(Address, object):
    id = 0

    def __init__(self, telnum: str = None, email: str = None, url: str = None, **kwargs):
        try:
            Member.id = kwargs["id"]
        except KeyError:
            Member.id += 1
        self.id = Member.id
        self.first_name = kwargs["f_name"]
        self.name = kwargs["name"]
        self.full_name = self.first_name + " " + self.name
        self.role = kwargs["role"]
        address = [item for item in kwargs["address"].values()]
        super().__init__(address)
        self.telnum = telnum
        self.email = email
        self.url = url
        self.output = self.structure()

    def structure(self):
        line = ""
        if self.telnum:
            line += "\t\t\t\tTel.: " + str(self.telnum)
        if self.email:
            if line:
                line += "  E-Mail.: " + str(self.email)
            else:
                line += "\t\t\t\tE-Mail.: " + str(self.email)
        if self.url:
            if line:
                line += "  Url.: " + str(self.url)
            else:
                line += "\t\t\t\tUrl.: " + str(self.url)
        return f"{self.full_name}: {self.role}, lives at |{self.address_name} {self.street_number}," \
               f"{self.postcode} {self.city}|" + f"{line:>80} "

    def __str__(self):
        return self.output

    def __repr__(self):
        return self.output

    def __call__(self, *args, **kwargs):
        return self.output


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
                         f"['Ter' = Teilnehmer:in/ {'TXX'} = {'das weiß ich nicht mehr'}/ {'XXX'} = {'keine ahnung'}]{INPUT_END}")
            print(role[0:4])
            if role[0:4] == "Ter":
                if input(f"Is Teilnehmer:in right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = "Teilnehmer:in"
                    continue
                    #################################  geschwungenen klammer tauschen  ##############################
            if role[0:4] == f"{'XXX'}":
                if input(f"Is {'Teilnehmer:in'} right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = f"{'Teilnehmer:in'}"
                    continue
                    ##################################  hier auch  ##################################################
            if role[0:4] == f"{'XXX'}":
                if input(f"Is {'Teilnehmer:in'} right? [yes/no]{INPUT_END}").lower()[0] == "y":
                    form["role"] = f"{'Teilnehmer:in'}"
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


# TODO 2. construct main loop

user_list = []


def course_administration(db):
    """Course_administrator main_loop

    Return q!"""
    db.members.append(Member(url="Website.com", f_name="Alexander", name="Hopfgartner", role="Teilnehmer",
                             address={"address_name": "Nikolsdorf", "number": 94, "postcode": 9782,
                                      "city": "Nikolsdorf"}))
    db.members.append(Member(telnum="123123123", email="email@email.com", url="Website.com",
                             f_name="Milch", name="Milchiger", role="Teilnehmerin",
                             address={"address_name": "Nikl", "number": 92, "postcode": 1110,
                                      "city": "Wien"}))
    exit_key = input(f"exit_key?: (\"q!\"){INPUT_END}")
    if exit_key == "q!":
        return exit_key
    elif exit_key.lower()[0] == "h":
        # TODO 2.2 add help report
        pass
    elif exit_key.lower()[0] == "a":
        new_member_form = add_member()
        if new_member_form:
            db.members.append(Member(**new_member_form))

        [print(mem) for mem in db.members]


def add_member():
    if input(f"Do you want to add a member? [yes/no]:\n{INPUT_END}", ).lower()[0] == "y":
        return member_form()
    else:
        return
