# TODO 2.1 create 2 classes
# TODO 2.1.2 create Adress

class Address:

    def __init__(self, *args,):
        args = args[0]
        self.address_name = args[0]
        self.number = args[1]
        self.postcode = args[2]
        self.city = args[3]


# TODO 2.1.1 create CourseAdministrator
class CourseAdministrator(Address):
    id = 0

    def __init__(self, telnum: str = "", email: str = "", url: str = "", **kwargs):
        self.telnum = telnum
        self.email = email
        self.url = url
        CourseAdministrator.id += 1
        self.id = CourseAdministrator.id
        self.first_name = kwargs["f_name"]
        self.name = kwargs["name"]
        self.full_name = self.first_name + " " + self.name
        self.role = kwargs["role"]
        address = [item for item in kwargs["addresse"].values()]

        super().__init__(address)

    def __str__(self):
        return f"{self.full_name}: {self.role}, lives at |{self.address_name} {self.number}, {self.postcode} {self.city}|"

    def __repr__(self):
        return f"{self.full_name}: {self.role}, lives at |{self.address_name} {self.number}, {self.postcode} {self.city}|"

    def __call__(self, *args, **kwargs):
        return f"{self.full_name}: {self.role}, lives at |{self.address_name} {self.number}, {self.postcode} {self.city}|"

# TODO 2. construct main loop


def course_administrator():
    print(CourseAdministrator(f_name="Alexander", name="Hopfgartner", role="Teilnehmer", addresse={"address_name": "Nikolsdorf", "number": 94, "postcode": 9782, "city": "Nikolsdorf"} ))


#TODO 2.2 manage main loop