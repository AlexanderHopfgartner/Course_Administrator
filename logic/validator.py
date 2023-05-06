# TODO 3. create all validation checks

"""########################################################################################################################
ich hab etwas die validater abgändert kannst du sie zum funktionieren bringe.
Sie müssen in den meisten fällen NUR True zurück geben.
Oder Ture or False
wenn er invalide ist bitte auch eine nachricht dazu

aktuell kannst du sie sogar testen, indem du zuerst die '#' entfernst im validator.py und dann die main.py runst dann
musst du dich erst anmelden (du kannst dich dann auch hinzufügen mit der id 0)
melde dich mit meinem namen an "Alexander Hopfgartner" dann hast du "admin_rechte"
oder mit "Alexander Hopf" dann bist du ein normaler user
dann kannst du (a/add) nutzen um nutzer hinzu zu fügen die die validations nutzen

telnum/email/url sollte optional bleiben, dahei sollten die True or False returnen
damit man bei einem invalid input nicht mehr gefragt wird.

Admin check ist im course_administrator
was dann noch fehlt ist beim course_administrator die restlichen input möglichkeiten
(e/edit) user editieren (wenn man admin ist)
(h/help) kann jeder was dir dann deine möglichkeinen anzeigt als aktueller user
(d/delete) user löschen (wenn man admin ist
(s/save) um die aktuelle DataBase zu speichern (wenn man admin ist)

was ich dir noch lasse zum üben/lernen ist die BD
dort kannst du selbst dann versuchen die logik hinzubekommen für
db_save (also die aktuelle db mit der alten überschrieben
db_log_on die Member.id ändern auf die db_read.ids.last_id


ich hab den code für db_log_on geschrieben um die DB nutzen zu können und um sich anzu melden
und damit du etwa beispiel code dafür hast
########################################################################################################################"""
def validate_name(name: str) -> bool:
    """Return True if the name is valid

       if name invalid print an error message.
    """
    for name in name.split():
        if name.isalpha():
            print("The name is valid")
            return True
    print("The name entered is not correct\nOnly letters and spaces are allowed\n")


def validate_address_name(address_name: str) -> bool:
    """Return False if the address_name is invalid\n\nReturn True"""
    if type(address_name) == str:
        return True, "The address name is valid"
    return False, "The address name is not valid\nOnly letters and spaces are allowed"


def validate_street_number(street_number: str) -> bool:
    """Return False if the street_number is invalid\n\nReturn True"""
    new_list = []
    numbers = street_number.split('/')
    print(numbers[0][0], type(int(numbers[0][0])))
    print(numbers[0][-1], type(int(numbers[0][-1])))

    if type(int(numbers[0][0])) == int and type(int(numbers[0][-1])) == int:
        print("Bin im IF drinnen", "")
        # new_list.append(int(num))
        # print(new_list)
        # print("Please enter your streetnumber in this format:\n123-124/12/1")
    print(numbers)
    # return True
    pass


def validate_postcode(postcode: str) -> bool:
    """Return tuple with boolean and error message as a string"""
    print("not finished")
    # return True


def validate_city(city: str) -> bool:
    """Return True if it is a valid city"""
    print("not finished")
    # return True
    pass


def validate_telnum(telnum: str) -> bool | str:
    """Return False if the phonenumber is invalid\n\nReturn True"""
    print("not finsihed")
    # return telnum
    pass


def validate_email(email: str) -> bool | str:
    """Return False if the email is invalid\n\nReturn True"""
    print("not finished")
    # return email
    pass



def validate_url(url: str) -> bool | str:
    """Return False if the url is invalid\n\nReturn True"""
    print("not finished")
    # return url
    pass


# validate_street_number("33-37/12/17")
validate_name("Melcher Christoph")
validate_name("Melche***")
validate_name("Mel1234")
