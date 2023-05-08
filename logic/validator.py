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
    if len(address_name) > 1:
        new_address = address_name
        address = new_address.split(' ')
        if address[0].isalpha() and address[-1].isalpha() and len(address) > 1:
            print("Im IF IF IF IF IF")
            print(address[0], address[-1])
            if input(f"Is this address name: '{address_name}' correct?{INPUT_END}").lower()[0] == "y":
                return True
    if len(address_name) > 1:
        if address_name.isalpha():
            if input(f"Is this address name: '{address_name}' correct?{INPUT_END}").lower()[0] == "y":
                return True
    print(f"The address name: {address_name} is not valid\nOnly letters and spaces are allowed\n")
    return False


def validate_street_number(street_number: str) -> bool:
    """Return True if street_number is valid\n Returns False otherwise"""
    numbers = street_number.split('/')
    try:
        if type(int(numbers[0][0])) == int and type(int(numbers[0][-1])) == int:
            return True
    except ValueError:
        print("Please enter your streetnumber in this format:\n123-456/78/9\n")
        return False
    print("Please enter your streetnumber in this format:\n123-456/78/9\n")
    return False


def validate_postcode(postcode: str) -> bool:
    """Return True if it is a valid postcode\n Returns False otherwise"""
    try:
        postcode = int(postcode)
    except ValueError:
        print(f"Your entered postcode: {postcode}, needs to be numbers only!")
        return False

    if 1009 < postcode < 9991:
        return True
    print(f"Your entered Postcode: {postcode} is invalid. Please enter a number between 1010 - 9990!\n")
    return False


def validate_city(city: str) -> bool:
    """Return True if it is a valid city\n Returns False otherwise"""
    new_city = city.split()
    if len(new_city) > 1:
        if city[0].isalpha() and city[-1].isalpha():
            return True
    if city.isalpha():
        return True
    print(f"Your entered City: {city} is invalid. Please only enter letters and spaces.\n")
    return False


def validate_telnum(telnum: str) -> bool | str:
    """Retruns True if telnum is valid\n Returns False otherwise"""
    telnum2 = telnum.split(' ')
    try:
        if len(telnum2) > 1:
            print("telnum gets splited:", telnum, telnum2)
            telnum = ""
            for tel in telnum2:
                telnum += tel
            print("new telnum:", telnum)
        if type(int(telnum[1:len(telnum)])) == int:
            if telnum[0] == "+":
                new_tel = telnum[0:3] + " " + telnum[3:6] + " " + telnum[6:9] + " " + telnum[9:11] + " " + \
                          telnum[11:13] + " " + telnum[13:15]
                return new_tel
            elif telnum[0] == "0":
                if telnum[0:2] == "01":
                    print(len(telnum))
                    print(telnum[0:2])
                    new_tel = telnum[0:2] + " " + telnum[2:5] + " " + telnum[5:7] + " " + telnum[7:9] + " " + telnum[9:12]
                    print("not finsihed", new_tel)
                    return new_tel

                else:
                    new_tel = telnum[0:4] + " " + telnum[4:7] + " " + telnum[7:9] + " " + telnum[9:11]
                    return new_tel
    except ValueError:
        print(f"The number: {telnum} is invalid. Please only enter numbers and you can add a '+' to the beginning for your country code\nExample:+43 6991 234 56 78\n")
        return False
    return False

def validate_email(email: str) -> bool | str:
    """Return True if email is valid\n Returns False otherwise"""
    tld_bool,domain_bool = False, False
    tld_check = ["at", "ac.at", "de", "com", "org", "us", "uk", "ru", "ua", "au", "in", "ir", "net"]
    domain_check = ["hotmail", "gmail", "gmx", "sms", "yahoo", "fh-campuswien", "live", "outlook", "AOL", "Zoho", "mail", "ProtonMail","CounterMail","Hushmail","Tutanota"]
    new_mail = email.split(' ')
    if len(new_mail) > 1:
        email = ""
        for section in new_mail:
            email += section
    if "@" in email:
        mail = email.split("@")
        tld = mail[-1].split(".")
        if tld[-1] in tld_check:
            print("tld_check",tld[-1] in tld_check)
            tld_bool = True
        if tld[0] in domain_check:
            print("domain check:", tld[0] in domain_check)
            domain_bool = True
        print("Bools:", tld_bool, domain_bool)
        if domain_bool and tld_bool:
            print("Email variable:", email)
            return email
    print(f"The entered Email: {email} is not valid. \nPlease enter the correct domain(example:'gmail') and Top-Level-Domain (example:'.at')!!\n")
    return False





def validate_url(url: str) -> bool | str:
    """Return True if url is valid\n Returns False otherwise"""
    tld_check = ["at", "ac.at", "de", "com", "org", "us", "uk", "ru", "ua", "au", "in", "ir", "net"]


liste = ["a"]

print(validate_postcode("9923"))
print("'abcd' Postcode".center(40, '*'))
print(validate_postcode("abcd"))

"""print(validate_email("test_mail@gmail.com"))
print()
print(validate_email("test.mail@yahoo.at"))
print()
print(validate_email("test-mail@hotmail.com"))
print()
print(validate_email("test_mail@ gmail. com"))
"""

"""print(validate_telnum("+4363848%%1"))
print("new number".center(40, '*'))
print(validate_telnum("abcd"))
print("new number".center(40, '*'))
print(validate_telnum("+436602736800"))
print("new number".center(40, '*'))
print(validate_telnum("06602736800"))
print("new number".center(40, '*'))
print(validate_telnum("019121817"))
print(validate_telnum("0660   273 68    00"))
print("new number".center(40, '*'))"""
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
