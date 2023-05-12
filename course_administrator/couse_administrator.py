from consts import INPUT_END, yon, clear, Form, AddressForm, MemberForm
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
        self.full_name = self.rename()
        self.role = kwargs["role"]
        address = [item for item in kwargs["address"].values()]
        super().__init__(address)
        if telnum:
            self.telnum = None
        self.telnum = telnum
        if email:
            self.email = None
        self.email = email
        if url:
            self.url = None
        self.url = url
        self.output = self.structure()

    def display_address(self):
        return f"{self.address_name:<18} {self.street_number:<6}| {self.postcode:<4} {self.city}"

    def display_plain_address(self):
        return [f"{self.address_name} {self.street_number}",str(self.postcode), self.city]

    def member_form(self):
        return MemberForm(
            telnum=self.telnum,
            email=self.email,
            url=self.url,
            f_name=self.first_name,
            name=self.name,
            role=self.role,
            address=AddressForm(
                address_name=self.address_name,
                number=self.street_number,
                postcode=self.postcode,
                city=self.city),
            id=self.id)

    def rename(self):
        return self.first_name + " " + self.name

    def restructure(self):
        self.full_name = self.rename()
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
        return f"|{self.full_name:<25} | {self.role:<14}, lives at |{self.display_address():<45}|" + f"{line}|"

    def __str__(self):
        return self.output

    def __repr__(self):
        return self.output

    def __call__(self, *args, **kwargs):
        return self.output


user_list = []


def course_administration(db, user) -> str | None:
    """Course_administrator main_loop

    Return q!"""

    from course_administrator.member_edit import find_user, edit
    #
    # db.members.append(Member(url="Website.com", f_name="Alexander", name="Hopfgartner", role="Teilnehmer:in",
    #                          address={"address_name": "Nikolsdorf", "number": 94, "postcode": 9782,
    #                                   "city": "Nikolsdorf"}))
    # db.members.append(Member(telnum="123123123", email="email@email.com", url="Website.com",
    #                          f_name="Milch", name="Milchiger", role="Teilnehmer:in",
    #                          address={"address_name": "Nikl", "number": 92, "postcode": 1110,
    #                                   "city": "Wien"}))
    print(f"\nwelcome in the DataBase administration. <<<{user.full_name}>>>")
    key = ""
    while key != "q!":
        while not key or (not key.isalpha() and not key == "q!"):
            key = input(f"Current user: <<<{user.full_name}>>>\n\nEnter \"Help\" for help.{INPUT_END}")
        if key.lower()[0] == "h":
            if user.id == 0:
                print(f"[h/Help]: Help:\tSee all current options.\n\n[a/Add]: Add: Add a member to the DataBase.\n"
                      f"[c/Clear]: Clear\tClears the console.\n[d/Del] Delete:\tRemove a Member by ID form "
                      f"the DataBase.\n[e/Edit] Edit:\t Edit a Member by ID from the DataBase\n"
                      f"[s/Save] Save:\tSave the current Database to the local.\n[v / View]: View:\tshow"
                      f"all user on the DataBase\n\n[q!] Log out: Logs out the current user\n")
            else:
                print(f"[h/Help]: Help:\tSee all current options.\n\n[c/Clear]: Clear\tClears the console.\n[v/View]: "
                      f"View:\tshow all user.\n\n[q!] Log out: Logs out the current user\n")

        if key.lower()[0] == "v":
            print(f"{'_'*220:<10}")
            [print(f"You >>> {member.id}" if member == user else member.id, ":|\t", member) for member in db.members]
            print(f"{'_'*220:<10}")

        if user.id == 0 and key.lower()[0] == "a":
            """Add a member"""
            new_member_form = add_member()
            if new_member_form:
                db.members.append(Member(**new_member_form))

        if user.id == 0 and key.lower()[0] == "e":
            """Edit a member"""
            edit_member = find_user(db, "edit")
            print("if")
            if type(edit_member) == Member:
                print("true")
                edit(edit_member)

        if user.id == 0 and key.lower()[0] == "d":
            """Delete a member"""
            del_member = find_user(db, "delete")
            if type(del_member) == Member:
                db.members.pop(db.members.index(del_member))

        if user.id == 0 and key.lower()[0] == "s":
            """save the DataBase"""
            db.db_save()
            print("DataBase saved.")

        if key.lower()[0] == "c":
            """clear console"""
            clear()

        if key == "q!":
            clear()
            save_massage = "Did you save, last change!" if user.id == 0 else ""
            if itis(f"{save_massage}\n\n\nDo you want do leave [yes?]{INPUT_END}"):
                return key
            clear()
        key = ""


def add_member():
    from course_administrator.member_form import fill_member_form
    if itis(f"Do you want to add a member? {yon}:\n{INPUT_END}", ):
        return fill_member_form()
    else:
        return
