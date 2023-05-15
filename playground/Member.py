from consts import YON, INPUT_END, itis, clear
from typing import TypedDict, Optional
import codecs
import json
import pandas as pd

PATH = "db_.json"


class AddressForm(TypedDict):
    address_name: str
    number: str
    postcode: int
    city: str


class DefaultForm(TypedDict):
    telnum: str
    email: str
    url: str
    f_name: str
    last_name: str
    address: AddressForm
    id: Optional[int]


class Address(object):
    # Variable for the display_address.
    space_a_n = 6
    space_s_n = 2
    space_c = 4

    def __init__(self, **kwargs):
        self.address_name: str = kwargs["address_name"]
        self.street_number: str = str(kwargs["number"])
        self.postcode: int = kwargs["postcode"]
        self.city: str = kwargs["city"]

    def display_address(self) -> str:
        """Return the Address fully formatted and checks
        if any new entry is longer then the last oneand replaces the hold placeholder value."""
        # Check if any new entry is longer than the last before.
        if len(self.address_name) > Address.space_a_n: Address.space_a_n = len(self.address_name)
        if len(self.street_number) > Address.space_s_n: Address.space_s_n = len(self.street_number)
        if len(self.city) > Address.space_c: Address.space_c = len(self.city)

        return f"|{self.address_name:<{Address.space_a_n}} {self.street_number:<{Address.space_s_n}}|" \
               f"{self.postcode:<4} {self.city:<{Address.space_c}}|"

    def display_plain_address(self):
        return [f"{self.address_name} {self.street_number}", str(self.postcode), self.city]

    def __str__(self):
        return self.display_address()

    def __repr__(self):
        return self.display_address()


class Member(object):
    """Base Class for

    Participant | Lector | Tutor"""
    id = 0

    def __init__(self, form: DefaultForm, **kwargs):
        # Try if ID was given.
        try:
            self.id = form["id"]
        except KeyError:
            Member.id += 1
            self.id = Member.id
        self.first_name = form["f_name"]
        self.last_name = form["last_name"]
        self.address = Address(**form["address"])
        self.telnum = form["telnum"]
        self.email = form["email"]
        self.url = form["url"]
        self.full_name = self.rename()
    def member_form(self) -> DefaultForm:
        """Return the Object as a Dict in the class DefaultForm."""
        return DefaultForm(
            telnum=self.telnum,
            email=self.email,
            url=self.url,
            f_name=self.first_name,
           last_name=self.last_name,
            address=AddressForm(
                address_name=self.address.address_name,
                number=self.address.street_number,
                postcode=self.address.postcode,
                city=self.address.city),
            id=self.id)

    def rename(self):
        """Reorganize the current full_name."""
        return self.first_name + " " + self.last_name

    def structure(self):
        """Return a full structured string with the data from the Object."""
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
        return f"|{self.full_name:<25} | lives at |{self.address.display_address():<45}|" + f"{line} |"

    def __str__(self):
        return self.structure()

    def __repr__(self):
        return self.rename()

    def __call__(self, *args, **kwargs):
        return self.structure()


class Participant(Member):
    def __init__(self, form: DefaultForm, **kwargs):
        super().__init__(form, **kwargs)


class Tutor(Member):
    def __init__(self, form: DefaultForm, **kwargs):
        super().__init__(form, **kwargs)

    def _add(self) -> bool:
        return True

    def _edit(self) -> bool:
        return True

    def _delete(self) -> bool:
        return True

    def _save(self) -> bool:
        return True


class Lector(Tutor):
    def __init__(self, form: DefaultForm, **kwargs):
        super().__init__(form, **kwargs)


member_class_list = {"participant": Participant, "lector": Lector, "tutor": Tutor}


def config_df(df):
    """Configer the pandas DataFrame"""
    pd.set_option('display.unicode.east_asian_width', True)
    pd.set_option('display.colheader_justify', 'left')


class DB:

    def add_member(self):
        pass

    def db_log_on(self):
        """Read the DB and construct the members to it's given roles and append it to the members list."""

        # Open the file as db_json
        pd.set_option('display.max_colwidth', 0)
        pd.set_option('display.colheader_justify', 'left')
        with codecs.open(PATH, "r", encoding="utf-8") as db_json:
            db_read = json.load(db_json)
            for member in db_read["ids"]["members"]:
                # Get hold of the class name
                member_class = list(member.keys())[0]

                # Append the member as it's given class
                self.members.append(member_class_list[member_class](member[member_class]))

            # Reset the Member.id
            Member.id = db_read["ids"]["last_id"]
            self.df = pd.DataFrame([member.__dict__ for member in self.members])
            self.df = self.df.set_index("id")
            self.df.drop('full_name', axis=1, inplace=True)
            config_df(self.df)

    def db_save(self):
        """Overwrite the local DB back to the Json"""
        member_list = []
        for member in self.members:
            # Append the objects reformatted as dict to the list
            member_list.append({member.__class__.__name__.lower(): member.member_form()})

        # Build around the base structure of the dict
        json_dict = {"ids": {"last_id": Member.id, "members": member_list}}

        # Open the file in write mode and dump the dict
        with codecs.open(PATH, 'w', encoding="utf-8") as file_object:
            json.dump(json_dict, file_object, ensure_ascii=False)

    def login(self) -> None:
        """Set a selected Member to the current_user."""
        # Until a user is found
        while True:
            user_name = input(f"Please Enter your username ['first_name surname']{INPUT_END}")

            # Creates a list of all users with the same name
            current_users = [member for member in self.members if member.full_name == user_name]
            match len(current_users):

                # When the list is empty
                case 0:
                    clear()
                    print("Sorry no user found.\n")

                # Users found
                case _:

                    # Loop through all users and asks for the right one
                    for user in current_users:
                        if itis(f"\n{user} found.\nIDNumber is: {user.id}\nLogin with this User? {YON}{INPUT_END}"):
                            clear()

                            # Print a login message and assign the user tu the current_user
                            print(f"Logged in with <<{user.full_name}>>")
                            self.current_user = user
                            return
            clear()
            print(f"No user left with the username {user_name}")

    def main_loop(self):
        [print(f"{member.id:<4}\t{member}") for member in self.members]
        clear()
        course_administation = True
        while course_administation:
            if action := input("Please Enter 'help' for help"):
                match action.lower():
                    case "a" | "add":
                        if self.current_user._add():
                            if self.add_member:
                                pass
                    case "c" | "clear":
                        clear()
                    case "e" | "edit":
                        if self.current_user._edit():
                            if self.get_user_to("edit"):
                                pass
                    case "d" | "del" | "delete":
                        if self.current_user._delete():
                            if self.get_user_to("delete"):
                                pass
                    case "h" | "help":
                        print("help")
                    case "s" | "if self.current_user: save":
                        self.db_save()
                    case "q" | "quit":
                        return
                    case "v" | "view":
                        [print(f"{member.id:<4}\t{member}") for member in self.members]

    def get_user_to(self, keyword) -> Member | None:
        """Return a chosen member from members"""
        user_get = True
        while user_get:
            if user_get := itis(f"Do you want to {keyword} a user? {YON}{INPUT_END}"):

                # Display all members with the id.
                [print(f"{member.id:<4}|\t {member}") for member in self.members]
                user_id = input(f"Please Enter the \"ID\".{INPUT_END}")

                # If no input or "q" "Q" to exit
                if not user_id or user_id == "q" or user_id == "Q":
                    return
                users_by_id = [member for member in self.members if member.id == int(user_id)][0]
                if users_by_id:

                    # Return if the correct user is found
                    if itis(f"Do you want to {keyword} the user: {users_by_id}.\n{YON}{INPUT_END}"):
                        return users_by_id
                else:
                    print("Sorry no user with this \"ID\".")

    def __init__(self):
        self.members: list[Participant | Lector | Tutor] = []
        self.current_user: Participant | Lector | Tutor | None = None
        self.df: pd.DataFrame | None = None
        self.db_log_on()
        self.login()

    def __str__(self):
        return [member.full_name for member in self.members]

    def __repr__(self):
        return [member.full_name for member in self.members]


db = DB()
db.main_loop()
