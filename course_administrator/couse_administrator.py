from consts import INPUT_END
from logic.validator import *
from course_administrator.member_form import member_form


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
        return f"|{self.address_name} {self.street_number}, {self.postcode} {self.city}|"

    def rename(self):
        return self.first_name + " " + self.name

    def restructure(self):
        print("restructure")
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
        return f"{self.full_name}: {self.role}, lives at {self.display_address()}" + f"{line:>80} "

    def __str__(self):
        return self.output

    def __repr__(self):
        return self.output

    def __call__(self, *args, **kwargs):
        return self.output

# TODO 2. construct main loop

user_list = []


def course_administration(db, user):
    """Course_administrator main_loop

    Return q!"""

    from course_administrator.member_edit import find_edit_user, edit

    db.members.append(Member(url="Website.com", f_name="Alexander", name="Hopfgartner", role="Teilnehmer",
                             address={"address_name": "Nikolsdorf", "number": 94, "postcode": 9782,
                                      "city": "Nikolsdorf"}))
    db.members.append(Member(telnum="123123123", email="email@email.com", url="Website.com",
                             f_name="Milch", name="Milchiger", role="Teilnehmerin",
                             address={"address_name": "Nikl", "number": 92, "postcode": 1110,
                                      "city": "Wien"}))
    print(f"welcome in the DataBase administration, {user.full_name}")
    key = ""
    while key != "q!":
        key = input(f"Enter \"Help\" for help.{INPUT_END}")
        if key.lower()[0] == "h":
            if user.id == 0:
                print(f"[h/Help]: Help:\tSee all current options\n[v/View]: View:\tshow all user\n[a/Add]: Add: "
                      f"Add a member to the DataBase\n[d/Del] Delete:\tRemove a Member by ID/full_name form the "
                      f"DataBase\n[s/Save] Save:\tSave the current Database to the local")
            else:
                print(f"[h/Help]: Help:\tSee all current options\n[v/View]: View:\tshow all user")
        if key.lower()[0] == "v":
            pass
        if user.id == 0 and key.lower()[0] == "a":
            """Add a member"""
            new_member_form = add_member()
            if new_member_form:
                db.members.append(Member(**new_member_form))
        if user.id == 0 and key.lower()[0] == "e":
            """Edit a member"""
            edit_member = find_edit_user(db)
            edit(edit_member)
            if edit_member:
                print(edit_member)
            else:
                print("invalid")

            pass
        if user.id == 0 and key.lower()[0] == "d":
            print("delete")
            """Delete a member"""
            pass
        if user.id == 0 and key.lower()[0] == "s":
            print("save")
            """save the DataBase"""
            pass

        [print(mem) for mem in db.members]

    if key == "!q":
        if input(f"Did you save, last change!\nDo you want do leave [yes/no]{INPUT_END}") == "y":
            return key


def add_member():
    if input(f"Do you want to add a member? [yes/no]:\n{INPUT_END}", ).lower()[0] == "y":
        return member_form()
    else:
        return
