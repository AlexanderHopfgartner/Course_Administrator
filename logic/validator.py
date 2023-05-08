from consts import INPUT_END

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
    """Return True if the name is valid\n Returns False otherwise"""
    for name in name.split():
        if name.isalpha():
            return True
    print(f"The name entered: '{name}' is not correct\nOnly letters and spaces are allowed\n")
    return False


def validate_address_name(address_name: str) -> bool:
    """Return True if address_name is valid\nReturns False otherwise"""
    if len(address_name)> 1:
        new_address = address_name
        address = new_address.split(' ')
        if address[0].isalpha() and address[-1].isalpha() and len(address)>1:
            print("Im IF IF IF IF IF")
            print(address[0], address[-1])
            if input(f"Is this address name: '{address_name}' correct?{INPUT_END}").lower()[0] == "y":
                return True
    if len(address_name) > 1:
        if address_name.isalpha():
            if input(f"Is this address name: '{address_name}' correct?{INPUT_END}").lower()[0] == "y":
                return True
    print(f"The address name: {address_name} is not valid\nOnly letters and spaces are allowed")
    return False


def validate_street_number(street_number: str) -> bool:
    """Return True if street_number is valid\n Returns False otherwise"""
    numbers = street_number.split('/')
    try:
        if type(int(numbers[0][0])) == int and type(int(numbers[0][-1])) == int:
            return True
    except ValueError:
        print("Please enter your streetnumber in this format:\n123-456/78/9")
        return False
    print("Please enter your streetnumber in this format:\n123-456/78/9")
    return False


def validate_postcode(postcode: int) -> bool:
    """Return True if it is a valid postcode\n Returns False otherwise"""
    if postcode > 1009 and postcode < 9991:
        return True
    print(f"Your entered Postcode: {postcode} is invalid. Please enter a number between 1010 - 9990!")
    return False


def validate_city(city: str) -> bool:
    """Return True if it is a valid city\n Returns False otherwise"""
    new_city = city.split()
    if len(new_city) > 1:
        if city[0].isalpha() and city[-1].isalpha():
            return True
    if city.isalpha():
        return True
    print(f"Your entered City: {city} is invalid. Please only enter letters and spaces.")
    return False


def validate_telnum(telnum: str) -> bool | str:
    """Retruns True if telnum is valid\n Returns False otherwise"""
    print("telnum[0]:", telnum[0])
    if telnum[0] == "+":
        print("length:", len(telnum))
        print(telnum[9:11])
        new_tel = telnum[0:6]+ " " + telnum[6:9] + " " + telnum[9:11] + " " + telnum[11:13]
        print("new Tel:", new_tel)
    elif telnum[0] == "0":
        print("length:", len(telnum))
        print()



def validate_email(email: str) -> bool | str:
    """Return True if email is valid\n Returns False otherwise"""
    print("not finished")
    # return email
    pass



def validate_url(url: str) -> bool | str:
    """Return True if url is valid\n Returns False otherwise"""
    print("not finished")
    # return url
    pass

liste = ["a"]

validate_telnum("+436602736800")
print("".center(80,'*'))
validate_telnum("06602736800")
"""print("##################### Name ############################")

print(validate_name("Melcher Christoph"))
print(validate_name("Melche***"))
print(validate_name("Mel1234"))
print("##################### street_address_name ############################")
print(validate_address_name("Penzinger Straße"))
print(validate_address_name("12345567"))
print(validate_address_name("Penzinger %%Straße"))
print("###################### Street_number ###########################")
print(validate_street_number("100-104/21/17"))
print(validate_street_number("2"))
print(validate_street_number("33"))
print(validate_street_number("dreiunddreißig Strich zwei strich"))

print("##################### postcode ############################")
print(validate_postcode(10000))
print(validate_postcode(133))
print(validate_postcode(1330))
print("#########################City check########################")
print(validate_city("TEST City"))
print(validate_city("New Jersey"))
print(validate_city("Vienna"))

print(validate_city("1 City"))
print(validate_city("New 1"))
print(validate_city("Vienna!"))
"""
