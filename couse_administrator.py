# TODO 2.1 create 2 classes
# TODO 2.1.2 create Adress
class Address:

    def __init__(self, *args, **kwargs):
        self.address_name = kwargs["address_name"]
        self.number = kwargs["number"]
        self.postcode = kwargs["postcode"]
        self.city = kwargs["city"]


# TODO 2.1.1 create CourseAdministrator
class PersonalCard(Address):
    id = 0

    def __init__(self, telnum="", email="", url="", **kwargs):
        self.telnum = telnum
        self.email = email
        self.url = url
        PersonalCard.id += 1
        self.id = PersonalCard.id
        self.name = kwargs["name"]
        self.role = kwargs["role"]

        super().__init__(kwargs["address"])

    def __str__(self):
        return f"{self.name}: {self.role}, lives at {self.address_name, self.number, self.postcode}"

    def __repr__(self):
        return f"{self.name}: {self.role}, lives at {self.address_name, self.number, self.postcode}"

    def __call__(self, *args, **kwargs):
        return f"{self.name}: {self.role}, lives at {self.address_name, self.number, self.postcode}"

# TODO 2. construct main loop


def course_administrator():
    pass

#TODO 2.2 manage main loop