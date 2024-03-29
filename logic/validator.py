from consts import INPUT_END, YON


def change_letters(text: str) -> str:  # Function for replacing ß->ss, ä->ae, ü->ue and ö->oe
    """Takes a string and checks it for ä, ö, ü and ß.
    Each gets replaced with 'normal' letters"""
    if not text:
        return text
    special_chars = ['ä', 'ü', 'ö', 'ß']
    text = text.lower()
    for char in special_chars:
        if char in text:
            match char:  # match case to check for the letter that needs to be changed
                case 'ß':  # change ß to ss
                    split_word = text.split('ß')
                    new_text = ""
                    for i in range(len(split_word)):
                        if len(split_word) == 2:
                            new_text += split_word[0] + 'ss' + split_word[-1]
                            break
                        elif len(split_word) == i + 1:
                            new_text += split_word[-1]
                        else:
                            new_text += split_word[i] + 'ss'
                    text = new_text
                case 'ä':
                    split_word = text.split('ä')
                    new_text = ""
                    for i in range(len(split_word)):
                        if len(split_word) == 2:
                            new_text += split_word[0] + 'ae' + split_word[-1]
                            break
                        elif len(split_word) == i + 1:
                            new_text += split_word[-1]
                        else:
                            new_text += split_word[i] + 'ae'
                    text = new_text
                case 'ü':
                    split_word = text.split('ü')
                    new_text = ""
                    for i in range(len(split_word)):
                        if len(split_word) == 2:
                            new_text += split_word[0] + 'ue' + split_word[-1]
                            break
                        elif len(split_word) == i + 1:
                            new_text += split_word[-1]
                        else:
                            new_text += split_word[i] + 'ue'
                    text = new_text
                case 'ö':
                    split_word = text.split('ö')
                    new_text = ""
                    for i in range(len(split_word)):
                        if len(split_word) == 2:
                            new_text += split_word[0] + 'oe' + split_word[-1]
                            break
                        elif len(split_word) == i + 1:
                            new_text += split_word[-1]
                        else:
                            new_text += split_word[i] + 'oe'
                    text = new_text
    # Checks if any special character is left inside the text, if not it returns the changed string
    if special_chars[0] not in text and \
            special_chars[1] not in text and \
            special_chars[2] not in text and \
            special_chars[3] not in text:
        new_text = text.split(' ')
        text = ""
        for word in new_text:
            if word == new_text[-1]:
                text += word.capitalize()
            else:
                text += word.capitalize() + ' '
        return text


# print("Changed Letters :",change_letters("Teßt"))
# print("Changed Letters :",change_letters("spaßeß"))
# print("Changed Letters :",change_letters("spaßeßeßß"))
# print("Changed Letters :",change_letters("ßßßß"))
#
# print("Changed Letters :",change_letters("äpfel"))
# print("Changed Letters :",change_letters("ääh"))
# print("Changed Letters :",change_letters("Gärtnerstraße"))
# print("Changed Letters :",change_letters("Vorgärtnerlücke1"))
#
# print("Changed Letters :",change_letters("Längen Möbe"))
# print("Changed Letters :",change_letters("Läöüß"))
# print("Changed Letters :",change_letters("Pöbäl"))
# print("Changed Letters :",change_letters("Iß däß äin dümmer Sätzö, dü Bößä Mänßch"))

def validate_name(name: str) -> bool:
    """Return True if the name is valid\n Returns False otherwise"""
    if not name:
        return False
    # name = change_letters(name)
    for name in name.split():
        if name.isalpha():
            return True
    print(f"The name entered: '{name}' is not correct\nOnly letters and spaces are allowed\n")
    return False


def validate_address_name(address_name: str) -> bool:
    """Return True if address_name is valid\nReturns False otherwise"""
    if not address_name:
        return False
    # address_name = change_letters(address_name)
    if len(address_name) > 1:
        new_address = address_name
        address = new_address.split(' ')
        if address[0].isalpha() and address[-1].isalpha() and len(address) > 1:
            # print("Im IF IF IF IF IF")
            # print(address[0], address[-1])
            if input(f"Is this address name: '{address_name}' {YON}{INPUT_END}").lower()[0] == "y":
                return True
    if len(address_name) > 1:
        if address_name.isalpha():
            if input(f"Is this address name: '{address_name}' {YON}{INPUT_END}").lower()[0] == "y":
                return True
    print(f"The address name: {address_name} is not valid\nOnly letters and spaces are allowed\n")
    return False


def validate_street_number(street_number: str) -> bool:
    """Return True if street_number is valid\n Returns False otherwise"""
    if not street_number:
        return False
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
    if not postcode:
        return False
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
    if not city:
        return False
    # city = change_letters(city)
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
    if not telnum:
        return False
    telnum2 = telnum.split(' ')
    try:
        if len(telnum2) > 1:
            # print("telnum gets splited:", telnum, telnum2)
            telnum = ""
            for tel in telnum2:
                telnum += tel
        print("telnum:", telnum)
        # type(int(telnum[1:len(telnum)])) == int
        if int(telnum[1:]):
            if telnum[0] == "+":
                new_tel = telnum[0:3] + " " + telnum[3:6] + " " + telnum[6:9] + " " + telnum[9:11] + " " + \
                          telnum[11:13] + " " + telnum[13:15]
                if len(telnum) > 18:
                    diff = len(telnum) - 15
                    begin = 15
                    diff_by_three = diff // 3
                    diff_remainder = diff % 3
                    for i in range(diff_by_three):
                        if i == diff_by_three:
                            new_tel += " " + telnum[begin:begin + diff_remainder]
                            break
                        new_tel += " " + telnum[begin:begin + 3]
                        begin += 3

                else:
                    new_tel += " " + telnum[15:len(telnum)]
                print("new telnum:", new_tel)
                return new_tel
            elif telnum[0] == "0":
                if telnum[0:2] == "01":
                    # print(len(telnum))
                    # print(telnum[0:2])
                    new_tel = telnum[0:2] + " " + telnum[2:5] + " " + telnum[5:7] + " " + telnum[7:9] + " " + telnum[
                                                                                                              9:12]
                    if len(telnum) > 15:
                        diff = len(telnum) - 12
                        begin = 12
                        diff_by_three = diff // 3
                        diff_remainder = diff % 3
                        for i in range(diff_by_three):
                            if i == diff_by_three:
                                new_tel += " " + telnum[begin:begin + diff_remainder]
                                break
                            new_tel += " " + telnum[begin:begin + 3]
                            begin += 3

                    else:
                        new_tel += " " + telnum[12:len(telnum)]
                    print("new telnum:", new_tel)
                    return new_tel

                else:
                    new_tel = telnum[0:4] + " " + telnum[4:7] + " " + telnum[7:9] + " " + telnum[9:11]
                    if len(telnum) > 14:
                        diff = len(telnum) - 11
                        begin = 11
                        diff_by_three = diff // 3
                        diff_remainder = diff % 3
                        for i in range(diff_by_three):
                            if i == diff_by_three:
                                new_tel += " " + telnum[begin:begin + diff_remainder]
                                break
                            new_tel += " " + telnum[begin:begin + 3]
                            begin += 3

                    else:
                        new_tel += " " + telnum[11:len(telnum)]
                    print("new telnum:", new_tel)
                    return new_tel
    except ValueError:
        print(
            f"The number: {telnum} is invalid. Please only enter numbers and you can add a '+' to the beginning "
            f"for your country code\nExample:+43 6991 234 56 78\n")
        return False
    return False


def validate_email(email: str) -> bool | str:
    """Return True if email is valid\n Returns False otherwise"""
    if not email:
        return False
    tld_bool, domain_bool, name_bool = False, False, False
    tld_check = ["at", "ac.at", "de", "com", "org", "us", "uk", "ru", "ua", "au", "in", "ir", "net"]
    new_mail = email.split(' ')
    if len(new_mail) > 1:
        email = ""
        for section in new_mail:
            email += section
    if "@" in email:
        mail = email.split("@")
        tld = mail[-1].split(".")
        if tld[-1] in tld_check:
            # print("tld_check", tld[-1] in tld_check)
            tld_bool = True
        if len(tld[0]) > 1:
            # print(tld[0], len(tld[0]))
            # print("domain check:", len(tld[0]) > 1)
            domain_bool = True
        if len(mail[0]) > 1:
            name_bool = True
        # print("Bools:", tld_bool, domain_bool)
        if domain_bool and tld_bool and name_bool:
            # print("Email variable:", email)
            return email
    print(f"The entered Email: {email} is not valid. \nPlease enter at least 2 characters for the domain-name, the "
          f"email-name and a correct Top-Level-Domain (example:'.at')!!\n")
    return False


def validate_url(url: str) -> bool | str:
    if not url:
        return False
    url = url.lower()
    tld_bool = False
    tld_check = ["at", "ac.at", "de", "com", "org", "us", "uk", "ua", "ru", "au", "in", "ir", "net"]
    world_wide_web = "www"
    wo_wi_we_bool = False
    list_url = url.split('.')
    if len(url) > 1:
        if len(list_url) > 1:
            if list_url[-1] in tld_check:
                tld_bool = True
            if list_url[0] == world_wide_web:
                wo_wi_we_bool = True
            if list_url[0] == "ww":
                list_url[0] = ""
            if not wo_wi_we_bool and tld_bool:
                if input(f"Do you want to add 'www.' to your URL('{url}')? {YON}{INPUT_END}").lower()[0] == "y":
                    url = ""
                    if not list_url[0] == "www.":
                        url = world_wide_web + "."
                    for ele in list_url:
                        if len(ele) > 0:
                            url += ele + "."
                    # print("URLURLURL:", url)
            if tld_bool:
                return url
    print(f"Your URL ({url}) is invalid, please enter a valid URL")
    if not tld_bool:
        print(f"Your Top-Level-Domain ('{list_url[-1]}') seems to be wrong!\n")
    return False
