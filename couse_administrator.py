from consts import INPUT_START


class Address:

    def __init__(self, *args, ):
        args = args[0]
        self.address_name = args[0]
        self.number = args[1]
        self.postcode = args[2]
        self.city = args[3]


# TODO 2.1.1 create CourseAdministrator
class CourseAdministrator(Address):
    id = 0

    def __init__(self, telnum: str = None, email: str = None, url: str = None, **kwargs):
        CourseAdministrator.id += 1
        self.id = CourseAdministrator.id
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
            line += "\t\t\t\tTel.: " + self.telnum
        if self.email:
            if line:
                line += "  E-Mail.: " + self.email
            else:
                line += "\t\t\t\tE-Mail.: " + self.email
        if self.url:
            if line:
                line += "  Url.: " + self.url
            else:
                line += "\t\t\t\tUrl.: " + self.url
        return f"{self.full_name}: {self.role}, lives at |{self.address_name} {self.number}, {self.postcode} {self.city}|" + line

    def __str__(self):
        return self.output

    def __repr__(self):
        return self.output

    def __call__(self, *args, **kwargs):
        return self.output


# TODO 2. construct main loop

user_list = []


def course_administrator():
    """Course_administrator main_loop

    Return q!"""
    user_list.append(CourseAdministrator(url="Website.com", f_name="Alexander", name="Hopfgartner", role="Teilnehmer",
                                         address={"address_name": "Nikolsdorf", "number": 94, "postcode": 9782,
                                                  "city": "Nikolsdorf"}))
    user_list.append(CourseAdministrator(telnum="123123123", email="email@email.com", url="Website.com",
                                         f_name="Milch", name="Milchiger", role="Teilnehmerin",
                                         address={"address_name": "Nikl", "number": 92, "postcode": 1110,
                                                  "city": "Wien"}))
    [print(user) for user in user_list]
    exit_key = input(f"exit_key?: (\"q!\"){INPUT_START}")
    if exit_key == "q!":
        return exit_key
    else:
        add_member()


def add_member():
    if input(f"Do you want to add a member? [yes/no]:\n{INPUT_START}", ).lower()[0] == "y":
        print("milch")
    else:
        return

